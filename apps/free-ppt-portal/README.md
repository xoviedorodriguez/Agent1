# Free PPT Portal (No Entra)

This portal gives your team a simple public-like web page:
1. Fill in topic and audience
2. Click **Generate Deck**
3. See a message with the SharePoint folder link

## How It Works

- The app generates a `.pptx` file using `python-pptx`
- It saves the file into a **local SharePoint-synced folder**
- OneDrive sync uploads the deck to SharePoint automatically
- The UI shows users where to find the deck

No Entra app registration is required.

## Prerequisites

1. A machine that stays online and runs this app
2. OneDrive signed in with access to your SharePoint library
3. SharePoint library synced locally (Folder path visible in File Explorer)
4. Python 3.10+

## Setup

From repository root:

```powershell
cd apps/free-ppt-portal
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set environment variables:

```powershell
$env:SHAREPOINT_SYNC_DIR="C:\\Path\\To\\Synced\\PPTS"
$env:SHAREPOINT_FOLDER_URL="https://epam.sharepoint.com/sites/CPGOpportunities/Shared%20Documents/AI%20Agent%20MVP/PPTS"
$env:PPT_TEMPLATE_PATH="C:\\Users\\XimenaOviedo\\BMAD-XVOR\\docs\\brand\\EPAM_PresalesTemplate.potx"
```

Run:

```powershell
python app.py
```

Open:

```text
http://localhost:8000
```

## Share With Team For Free

### Option A: Same Network
Share your machine IP URL (e.g. `http://10.0.0.20:8000`).

### Option B: Public URL (free)
Use Cloudflare Tunnel free plan:

```powershell
cloudflared tunnel --url http://localhost:8000
```

Share the generated HTTPS URL with the team.

## Notes

- This is MVP mode and intentionally simple.
- Current version creates a structured 9-slide draft deck.
- You can later connect the full research/agent pipeline behind the same form.
- `python-pptx` does not open `.potx` directly. For strict template fidelity,
  save a `.pptx` version of the template and point `PPT_TEMPLATE_PATH` to it.
