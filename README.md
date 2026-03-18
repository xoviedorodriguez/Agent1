# BMAD XVOR

BMAD XVOR is a lightweight BMAD-style workspace prepared for a documentation-to-PPT/PDF MVP.

It includes:
- BMAD planning templates for PRD, architecture, stories, and QA gates
- GitHub issue and pull request templates for team collaboration
- Local agent instruction files for consistent AI-assisted work in VS Code
- A free web portal for team PPT requests with local save per user computer

## Free Team Portal (Recommended)

Use the free portal when you want non-technical teammates to request decks from a browser.

Path: `apps/free-ppt-portal/`

What users do:
1. Open the portal URL
2. Fill in topic, audience, and industry
3. Choose the output folder on their computer
3. Click **Generate Deck**
4. Open the local path shown in the success message

How save works in free mode:
- The app writes deck files directly to the folder selected by the user
- No SharePoint setup is required
- No Entra app registration is required

See setup details in `apps/free-ppt-portal/README.md`.

## Suggested Workflow

1. Capture the product request in `docs/bmad/prd-template.md`.
2. Translate the approach into `docs/bmad/architecture-template.md`.
3. Break execution into work items using `docs/bmad/story-template.md`.
4. Validate readiness and quality with `docs/bmad/qa-gate-template.md`.
5. Open GitHub issues and PRs using the templates in `.github/`.

## Publish To GitHub

After opening this folder in VS Code, you can publish it by either:

1. Using the Source Control view and selecting `Publish to GitHub`
2. Running these commands in a terminal after creating the remote repository:

```powershell
git remote add origin https://github.com/<your-user-or-org>/BMAD-XVOR.git
git branch -M main
git push -u origin main
```

## Notes

- This is a starter installation, not a full mirror of the upstream BMAD-METHOD repository.
- The files are tailored for your AI-documentation-to-PPT/PDF MVP so your team can start with a narrower process.