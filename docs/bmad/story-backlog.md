# Story Backlog - BMAD XVOR PPT Builder MVP

## Story 1 - Research and Citation Pipeline

### Story

As a consultant, I want the system to gather online information and show sources, so that deck claims are traceable and credible.

### Context

- PRD: docs/bmad/prd.md (Requirements, Acceptance Criteria 2)
- Architecture: docs/bmad/architecture.md (Research collector, Citation strategy)

### Tasks

1. Implement primary web search and source parsing.
2. Implement fallback research source path.
3. Add source list to UI result panel.
4. Add source links to notes and Sources slide in deck.

### Acceptance Criteria

1. At least one source is shown when online access exists.
2. Generated deck contains a Sources slide.
3. Notes include source references for evidence-based slides.

### Definition Of Done

- Code reviewed
- Validation completed
- QA gate updated

## Story 2 - Template and Brand Enforcement

### Story

As a consulting lead, I want decks to follow brand and template rules, so that outputs look corporate-ready.

### Context

- PRD: docs/bmad/prd.md (Corporate standards requirements)
- Architecture: docs/bmad/architecture.md (Standards engine, Template resolver)

### Tasks

1. Resolve template mode with explicit compatibility check.
2. Apply title bars, color palette, and typography defaults.
3. Apply logo on key slides when file is available.
4. Report template and logo status in UI.

### Acceptance Criteria

1. Deck shows brand styling in generated slides.
2. Logo appears when logo asset exists.
3. UI shows whether template or fallback mode was used.

### Definition Of Done

- Code reviewed
- Validation completed
- QA gate updated

## Story 3 - Content Quality Upgrade

### Story

As a consultant, I want richer, executive-quality slide content, so that I can use outputs with minimal rewriting.

### Context

- PRD: docs/bmad/prd.md (Outcome, Quality requirements)
- Architecture: docs/bmad/architecture.md (Content synthesizer)

### Tasks

1. Improve storyline logic across capability narrative.
2. Use research snippets to strengthen market and proof slides.
3. Add quality checks for weak or generic text.
4. Expose quality status indicators in UI.

### Acceptance Criteria

1. Slides include substantive, non-placeholder messaging.
2. Market context reflects retrieved source content.
3. Output quality status is visible after generation.

### Definition Of Done

- Code reviewed
- Validation completed
- QA gate updated

## Story 4 - Local Save Reliability

### Story

As any team member, I want to choose my output folder, so that generated decks are saved where I need them on my computer.

### Context

- PRD: docs/bmad/prd.md (Functional requirements)
- Architecture: docs/bmad/architecture.md (Local storage writer)

### Tasks

1. Require output folder field in form.
2. Validate writable path.
3. Return full local file path on success.
4. Handle common path errors gracefully.

### Acceptance Criteria

1. Deck is saved in the chosen folder.
2. User sees explicit file path on success.
3. Invalid folder path gives actionable error message.

### Definition Of Done

- Code reviewed
- Validation completed
- QA gate updated
