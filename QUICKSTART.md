# Quick Start — Free PPT Portal (Local Save)

This is the easiest team path now.
No VS Code required for end users.

---

## What Team Members Do

1. Open the portal URL in a browser
2. Fill topic, audience, and industry
3. Choose the output folder on their computer
3. Click **Generate Deck**
4. Open the local file path shown in the success message

---

## One-Time Setup (Owner/Admin)

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
$env:PPT_TEMPLATE_PATH="C:\Users\XimenaOviedo\BMAD-XVOR\docs\brand\EPAM_PresalesTemplate.pptx"
```

Run:

```powershell
python app.py
```

Open:

```text
http://localhost:8000
```

---

## Share With Team

Option A: Same network
- Share `http://<your-machine-ip>:8000`

Option B: Public HTTPS URL (free)

```powershell
cloudflared tunnel --url http://localhost:8000
```

Share the generated HTTPS URL with the team.

---

## Notes

- Free mode saves directly to a local folder selected by the user.
- For best template fidelity, point `PPT_TEMPLATE_PATH` to a `.pptx` copy of your template.
- Current portal generates a branded 9-slide draft and shows the local saved path.

---

## Repository

https://github.com/xoviedorodriguez/Agent1

---

## Version

v1.2 — March 2026 — Local Save Edition
