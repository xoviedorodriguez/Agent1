# Free PPT Portal (Local Save)

This portal gives your team a simple web page:
1. Fill in topic and audience
2. Choose an output folder on that computer
3. Click **Generate Deck**
4. Open the saved `.pptx` from the path shown in the success message

## How It Works

- The app generates a `.pptx` file using `python-pptx`
- The user enters a local folder path in the form
- The app saves the deck directly in that folder
- The UI confirms the exact saved file path

## Prerequisites

1. A machine that runs this app
2. Python 3.10+

## Setup

From repository root:

```powershell
cd apps/free-ppt-portal
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Optional environment variables:

```powershell
$env:DEFAULT_OUTPUT_DIR="C:\Path\For\Default\Decks"
$env:PPT_TEMPLATE_PATH="C:\Users\XimenaOviedo\BMAD-XVOR\docs\brand\EPAM_PresalesTemplate.potx"
```

Run:

```powershell
python app.py
```

Open:

```text
http://localhost:8000
```

## Share With Team

### Option A: Same Network
Share your machine IP URL (e.g. `http://10.0.0.20:8000`).

### Option B: Public URL (free)
Use Cloudflare Tunnel free plan:

```powershell
"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:8000
```

Share the generated HTTPS URL with the team.

## Notes

- This is MVP mode and intentionally simple.
- Current version creates a structured 9-slide draft deck.
- You can later connect the full research/agent pipeline behind the same form.
- `python-pptx` does not open `.potx` directly. For strict template fidelity,
  save a `.pptx` version of the template and point `PPT_TEMPLATE_PATH` to it.

## Troubleshooting

### "Deck is not being created"

Check the "Saved locally at" path shown after generation.

If no output folder is entered, the app uses:

```text
C:\Users\<your-user>\Downloads\Generated-PPT-Decks\
```

### "Folder path does not work"

Use a full Windows path, for example:

```text
C:\Users\XimenaOviedo\Documents\GeneratedDecks
```

Tip: Open the folder in File Explorer and copy the path from the address bar.
