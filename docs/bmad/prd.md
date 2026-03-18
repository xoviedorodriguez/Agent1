# PRD - BMAD XVOR PPT Builder MVP

## Problem

Consultants are spending too much time creating capability decks manually, which reduces selling time and causes inconsistent quality. Current outputs can be too generic, may miss citations, and may not reliably apply branding/template standards.

## Users

- Primary users: Consulting team members preparing capability decks for client conversations
- Secondary users: Team leads reviewing deck quality and consistency
- Stakeholders: Sales leadership, solution architects, and delivery managers

## Outcome

Success means a team member can submit a topic brief and receive a high-quality, branded PPT with source-backed content saved locally in a selected folder, ready for review and client tailoring.

## Scope

MVP includes:
- Browser-based portal for request intake
- Online research collection with visible sources
- Content generation for executive-quality capability decks
- Brand application (colors, logo)
- Template usage when compatible template file is available
- Local folder selection for deck output
- Quality gate status shown after generation

## Non-Goals

- Full autonomous proposal writing beyond deck scope
- Deep data validation against paid analyst APIs
- Multi-user authentication and role-based access control
- Enterprise orchestration workflows and approval routing

## Requirements

1. Functional requirements
- User can enter topic, audience, industry, and specific needs
- User must provide output folder path
- System gathers online information and stores source links
- System generates a deck with structured storyline and meaningful content
- System applies brand rules and logo when assets exist
- System uses a compatible PPTX template if available
- System saves generated deck in user-selected local folder

2. Quality requirements
- Deck includes citations and a dedicated Sources slide
- Speaker notes include source references for factual slides
- Content avoids placeholder-only or low-value generic bullets
- Generation errors are surfaced clearly to user
- Output path and quality status are clearly reported

3. Corporate standards requirements
- Use approved brand palette and typography defaults
- Use approved logo placement on key slides
- Preserve corporate storyline structure
- Use template-driven layout when compatible

## Acceptance Criteria

1. Given a valid request, the system creates a PPT in the selected local folder and confirms file path.
2. Generated deck includes source-backed content with visible sources in UI and in deck.
3. Brand styling is applied, and logo is included when logo file is available.
4. System reports template mode: compatible template used or branded fallback.
5. Deck quality is reviewable via QA gate checklist.
