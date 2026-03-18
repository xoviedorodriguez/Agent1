# Architecture - BMAD XVOR PPT Builder MVP

## System Overview

A local web portal receives a deck request, gathers online research, synthesizes slide content, applies brand and template rules, and writes a PPT file to a user-selected local folder.

## Components

- Request UI
: Form-based input for topic, audience, industry, specific needs, and output folder.
- Research collector
: Performs online search and fallback content retrieval, returning source records.
- Content synthesizer
: Converts research into executive storyline bullets and supporting narrative.
- Standards engine
: Applies brand colors, typography defaults, title bars, and logo usage rules.
- Template resolver
: Uses compatible PPTX template if available; otherwise applies branded fallback layout.
- PPT renderer
: Builds slides, notes, and Sources slide with python-pptx.
- Local storage writer
: Saves output to user-selected folder and returns file path.
- Quality status reporter
: Reports research count, template mode, and branding status.

## Data Flow

1. User submits form input in portal UI.
2. Backend validates required fields.
3. Research collector gathers online results and source metadata.
4. Content synthesizer produces slide-level storyline and bullets.
5. Template resolver selects rendering mode.
6. Standards engine applies brand rules and logo.
7. PPT renderer generates final deck and embeds sources in notes and Sources slide.
8. Local storage writer saves deck in selected folder.
9. UI returns generation result, file path, template mode, and source list.

## Quality Controls

- Approved source validation
: Prefer diverse sources, keep source URLs, and expose references in output.
- Citation strategy
: Add source links to notes and Sources slide.
- Template enforcement
: Use compatible PPTX template when available; clearly report fallback mode.
- Brand enforcement
: Apply configured color and logo rules consistently.
- Review checkpoints
: Quality status shown in UI and evaluated with QA gate.

## Risks

- Search provider variability may reduce source yield.
- Template incompatibility if only POTX is available.
- Local file permission issues on selected output folder.
- Inconsistent internet access can degrade research quality.
- Basic narrative quality may still require human editing for high-stakes pitches.
