# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""Tests for generate.py with a small fixture specification (no network access).

Run from the repository root: python -m unittest discover -s eng/spec-knowledge-graph
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generate  # noqa: E402

RESOURCES = {
    'tags': [
        {'name': 'schools', 'description': 'A school. It has students.'},
        {'name': 'sections', 'description': 'A section of a course, e.g. Algebra I period 2. Taught by staff.'},
    ],
    'paths': {
        '/ed-fi/sections': {
            'get': {'tags': ['sections']},
            'post': {'tags': ['sections'], 'requestBody': {'content': {'application/json': {'schema': {
                '$ref': '#/components/schemas/edFi_section'}}}}},
        },
        '/ed-fi/sections/{id}': {'get': {'tags': ['sections']}, 'put': {'tags': ['sections']},
                                 'delete': {'tags': ['sections']}},
        '/ed-fi/sections/deletes': {'get': {'tags': ['sections']}},
        '/ed-fi/schools': {'get': {'tags': ['schools']}},
    },
    'components': {'schemas': {
        'edFi_section': {
            'required': ['sectionIdentifier', 'schoolReference'],
            'properties': {
                'id': {'type': 'string'},
                'sectionIdentifier': {'type': 'string', 'maxLength': 255, 'x-Ed-Fi-isIdentity': True,
                                      'description': 'The section identifier.'},
                'schoolReference': {'$ref': '#/components/schemas/edFi_schoolReference'},
                'sectionName': {'type': 'string', 'description': 'A name.'},
                'classPeriods': {'type': 'array', 'items': {'$ref': '#/components/schemas/edFi_sectionClassPeriod'}},
            }},
        'edFi_schoolReference': {'properties': {'schoolId': {'type': 'integer'}, 'link': {}}},
        'edFi_sectionClassPeriod': {
            'required': ['classPeriodName'],
            'properties': {'classPeriodName': {'type': 'string', 'description': 'The period name.'}}},
    }},
}
DESCRIPTORS = {'tags': [{'name': 'gradeLevelDescriptors', 'description': 'Grade levels, i.e. the grades.'}]}


class GenerateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        paths = {}
        for name, data in (('resources', RESOURCES), ('descriptors', DESCRIPTORS)):
            paths[name] = os.path.join(cls.tmp.name, f'{name}.json')
            with open(paths[name], 'w', encoding='utf-8') as fh:
                json.dump(data, fh)
        synonyms = os.path.join(cls.tmp.name, 'synonyms.json')
        with open(synonyms, 'w', encoding='utf-8') as fh:
            json.dump({'synonyms': {'class': ['sections']}}, fh)
        cls.out = os.path.join(cls.tmp.name, 'out')
        subprocess.run([sys.executable, os.path.join(HERE, 'generate.py'), '--resources', paths['resources'],
                        '--descriptors', paths['descriptors'], '--out', cls.out, '--synonyms', synonyms],
                       check=True, capture_output=True)

        def read(*parts):
            with open(os.path.join(cls.out, *parts), encoding='utf-8') as fh:
                return fh.read()
        cls.section, cls.index, cls.descriptors = read('resources', 'sections.md'), read('index.md'), read(
            'descriptors.md')

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_required_flags_without_key_claims(self):
        self.assertIn('| `sectionIdentifier` | yes |', self.section)
        self.assertIn('| `sectionName` |  |', self.section)
        self.assertNotIn('Natural key', self.section)
        self.assertNotIn('| key |', self.section)

    def test_reference_lists_fields_to_supply_and_falls_back_to_resource_description(self):
        self.assertIn('reference; supply `schoolId` | A school.', self.section)

    def test_collection_items_are_expanded(self):
        self.assertIn('### Items in `classPeriods`', self.section)
        self.assertIn('| `classPeriodName` | yes |', self.section)

    def test_collection_endpoint_comes_first(self):
        endpoints = [line for line in self.section.splitlines() if line.startswith('- `')]
        self.assertEqual(endpoints[0], '- `GET /ed-fi/sections`')
        self.assertTrue(endpoints[-1].endswith('/{id}`'))

    def test_index_keeps_abbreviations_and_synonyms(self):
        self.assertIn('e.g. Algebra I period 2.', self.index)
        self.assertIn('Also: class.', self.index)
        self.assertIn('i.e. the grades.', self.descriptors)

    def test_skips_server_fields(self):
        self.assertNotIn('| `id` |', self.section)

    def test_load_rejects_non_https_urls(self):
        with self.assertRaises(SystemExit):
            generate.load('http://example.org/swagger.json')


if __name__ == '__main__':
    unittest.main()
