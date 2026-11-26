// SPDX-License-Identifier: Apache-2.0
// Licensed to the Ed-Fi Alliance under one or more agreements.
// The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
// See the LICENSE and NOTICES files in the project root for more information.

// Each skill is installed on its own, so a reference file that two skills need is copied into both.
// This check fails when the copies differ. Edit one copy, then copy it over the other.

import { readFileSync } from "node:fs";

const sharedFiles = [
  [
    "skills/ed-fi-extension-builder/references/rules.md",
    "skills/ed-fi-extension-review/references/rules.md",
  ],
  [
    "skills/ed-fi-extension-builder/references/build.md",
    "skills/ed-fi-extension-review/references/build.md",
  ],
];

let failed = false;
for (const [source, copy] of sharedFiles) {
  if (readFileSync(source, "utf8") !== readFileSync(copy, "utf8")) {
    console.error(`${copy} differs from ${source}. Copy one over the other.`);
    failed = true;
  }
}

if (failed) {
  process.exit(1);
}
console.log(`${sharedFiles.length} shared files match.`);
