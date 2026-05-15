# Dynamical Threshold Theory of Sleep v0.1.1-zenodo-safe-public-gate

This is the initial Zenodo-safe public-gate release package for the Dynamical Threshold Theory of Sleep (DTTS) project.

## Scope

This release provides a reproducibility-oriented public archive for DTTS, a mathematical and computational prototype that models sleep-like transitions as recovery phase dynamics in adaptive multicellular networks.

The package is intended for documentation, inspection, citation, independent review, and DOI archival through Zenodo.

DTTS is not a clinical sleep model, not medical advice, not a diagnostic or treatment tool, not a human-subject validation package, and not a complete biological theory of sleep.

## Central interpretation

The archive supports the limited claim that sleep-like recovery transitions can be represented as qualitative phase dynamics in an adaptive oscillator-network prototype.

The included numerical materials illustrate qualitative motifs such as heterogeneous homeostatic burden, growth of sleep propensity, bounded coupling downscaling, relaxation of a sleep-dominant free-energy proxy, and preferential preservation of protected edges.

The central claim is mathematical and diagnostic, not clinical or therapeutic.

## Included materials

- Manuscript PDF and Jxiv metadata draft
- README and Japanese README
- Evaluation-only license
- Root LICENSE file
- File manifest with SHA-256 hashes
- Claim-boundary and medical-claim-boundary documents
- AI-assistance disclosure
- Practical positioning and publication-strategy notes
- Selected proof-of-concept simulation scripts and figures
- Result-summary CSV and JSON files
- Zenodo-safe draft citation metadata under `docs/citation_metadata/`

## Claim boundary

This release supports the limited claim that DTTS is a mathematical network prototype for sleep-like recovery phase transitions.

It does not claim:

- clinical sleep diagnosis;
- medical advice;
- sleep-disorder treatment;
- human-subject or animal-subject validation;
- direct brain-data fitting;
- prediction of individual sleep states;
- proof of the biological function of sleep;
- a complete neuroscientific model of the brain.

## Zenodo-safe citation handling

The active root `CITATION.cff` file has been intentionally omitted from this pre-DOI release to avoid metadata-validation conflicts during Zenodo archival.

Draft citation metadata is preserved at:

`docs/citation_metadata/CITATION_DRAFT_pre_doi.cff`

After Zenodo DOI assignment, DOI metadata should be added to README, manuscript metadata, and citation files in a follow-up DOI-metadata release.

## Integrity check

The public package was checked before release.

- Manifest verification: PASS
- JSON parse: PASS
- Draft CFF YAML parse: PASS
- Root CITATION.cff: intentionally omitted
- Root LICENSE: present
- Git-ignore included-file conflict: 0
- Large files over 100 MB: none detected
- Compiled binaries: none detected
- Python syntax check: PASS
- AI assistance disclosure: present
- Claim-boundary documents: present
- Medical-claim-boundary document: present

## Recommended citation status

This is a pre-DOI GitHub release prepared for Zenodo archival.

Suggested tag:

`v0.1.1-zenodo-safe-public-gate`
