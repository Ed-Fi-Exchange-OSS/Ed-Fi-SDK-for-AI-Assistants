# educationContents

`/ed-fi/educationContents`

This entity represents materials for students or teachers that can be used for teaching, learning, research,
and more. Education content includes full courses, course materials, modules, intervention descriptions,
textbooks, streaming videos, tests, software, and any other tools, materials, or techniques used to support
access to knowledge.

## Natural key

`contentIdentifier`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `contentIdentifier` | key | string max 225 | A unique identifier for the education content. |
| `learningStandardReference` |  | reference: `learningStandardId` |  |
| `additionalAuthorsIndicator` |  | boolean | Indicates whether there are additional un-named authors. |
| `appropriateGradeLevels` |  | array of edFi_educationContentAppropriateGradeLevel | An unordered collection of educationContentAppropriateGradeLevels. |
| `appropriateSexes` |  | array of edFi_educationContentAppropriateSex | An unordered collection of educationContentAppropriateSexes. |
| `authors` |  | array of edFi_educationContentAuthor | An unordered collection of educationContentAuthors. |
| `contentClassDescriptor` |  | descriptor URI | The predominate type or kind characterizing the learning resource. |
| `cost` |  | number (double) | An amount that has to be paid or spent to buy or obtain the education content. |
| `costRateDescriptor` |  | descriptor URI | The rate by which the cost applies. |
| `derivativeSourceEducationContents` |  | array of edFi_educationContentDerivativeSourceEducationContent | An unordered collection of educationContentDerivativeSourceEducationContents. |
| `derivativeSourceLearningResourceMetadataURIs` |  | array of edFi_educationContentDerivativeSourceLearningResourceMetadataURI | An unordered collection of educationContentDerivativeSourceLearningResourceMetadataURIs. |
| `derivativeSourceURIs` |  | array of edFi_educationContentDerivativeSourceURI | An unordered collection of educationContentDerivativeSourceURIs. |
| `description` |  | string max 1024 | An extended written representation of the education content. |
| `interactivityStyleDescriptor` |  | descriptor URI | The predominate mode of learning supported by the learning resource. |
| `languages` |  | array of edFi_educationContentLanguage | An unordered collection of educationContentLanguages. |
| `learningResourceMetadataURI` |  | string max 255 | The URI (typical a URL) pointing to the metadata entry in a LRMI metadata repository, which describes this content item. |
| `namespace` | yes | string max 255 | Namespace for the education content. |
| `publicationDate` |  | string (date) | The date on which this content was first published. |
| `publicationYear` |  | integer (int32) | The year at which this content was first published. |
| `publisher` |  | string max 50 | The organization credited with publishing the resource. |
| `shortDescription` |  | string max 75 | A short description or name of the entity. |
| `timeRequired` |  | string max 30 | Approximate or typical time that it takes to work with or through this learning resource for the typical intended target audience expressed in minutes. |
| `useRightsURL` |  | string max 255 | The URL where the owner specifies permissions for using the resource. |
| `version` |  | string max 10 | The version identifier for the content. |

## Endpoints

- `DELETE /ed-fi/educationContents/{id}`
- `GET /ed-fi/educationContents/deletes`
- `GET /ed-fi/educationContents/keyChanges`
- `GET /ed-fi/educationContents/partitions`
- `GET /ed-fi/educationContents/{id}`
- `GET /ed-fi/educationContents`
- `POST /ed-fi/educationContents`
- `PUT /ed-fi/educationContents/{id}`
