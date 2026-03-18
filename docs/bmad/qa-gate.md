# QA Gate - BMAD XVOR PPT Builder MVP

## Scope

Stories under docs/bmad/story-backlog.md for research-backed, branded, template-aware local deck generation.

## Checks

- Requirements implemented
: Verify PRD functional, quality, and standards requirements are covered.
- Output matches corporate standards
: Confirm brand colors, logo behavior, and template mode reporting.
- Inputs are traceable to source documents
: Confirm source URLs are present in UI, notes, and Sources slide.
- Failure cases are handled
: Confirm behavior for missing internet, missing logo, incompatible template, and invalid output folder.
- Review notes are documented
: Capture observed defects and required follow-up actions.

## Result

- Pass with conditions

## Notes

Observed status at BMAD start:
- BMAD artifacts created and aligned to current portal objective.
- Code baseline already includes research, source reporting, and branded fallback behavior.
- Template fidelity depends on availability of compatible PPTX template.

Open conditions before full Pass:
1. Validate against at least three real user topics and audiences.
2. Confirm final slide quality with consulting lead review.
3. Add stricter quality threshold for minimum source count if required.
4. Validate template mode using a confirmed compatible PPTX template file.
