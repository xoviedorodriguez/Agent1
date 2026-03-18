# SharePoint Configuration

## Site Details

| Setting | Value |
|---------|-------|
| **SharePoint Site URL** | `https://epam.sharepoint.com/sites/CPGOpportunities` |
| **Target Folder Path** | `/Shared Documents/AI Agent MVP/PPTS` |
| **Full Folder URL** | `https://epam.sharepoint.com/sites/CPGOpportunities/Shared%20Documents/AI%20Agent%20MVP/PPTS` |

---

## Upload Behavior

Default mode (free no-Entra):

1. Generate `.pptx` locally
2. Save to local OneDrive-synced folder
3. OneDrive sync uploads to SharePoint automatically

When the deck arrives in SharePoint, it will be available at:

```
https://epam.sharepoint.com/sites/CPGOpportunities/Shared Documents/AI Agent MVP/PPTS/[CAPABILITY-NAME]-deck-[YYYY-MM-DD].pptx
```

Example:
```
Data-Analytics-deck-2026-03-18.pptx
```

---

## Authentication Modes

### Default Mode: No Entra App Registration

No Graph credentials are required in this mode.
Set only these environment values in the portal runtime:

```
SHAREPOINT_SYNC_DIR=C:\Path\To\Synced\PPTS
SHAREPOINT_FOLDER_URL=https://epam.sharepoint.com/sites/CPGOpportunities/Shared%20Documents/AI%20Agent%20MVP/PPTS
```

### Optional Advanced Mode: Microsoft Graph API

Use this only if you need server-side direct uploads without local OneDrive sync.

### Option 1: Microsoft Graph API with App Registration
This is the recommended approach for shared/automated workflows.

1. Create an **Azure App Registration** in your EPAM tenant
2. Grant it these permissions:
   - `Sites.ReadWrite.All` (or scoped to the specific site)
3. Store these as environment variables (never commit them):
   ```
   AZURE_CLIENT_ID=your-app-id
   AZURE_CLIENT_SECRET=your-app-secret
   AZURE_TENANT_ID=your-tenant-id
   ```
4. The agent will use the Microsoft Graph API to upload files

### Optional Delegated Mode (User-based)
For manual workflows:
1. The app generates the `.pptx` file locally
2. User authenticates to SharePoint via browser
3. User uploads manually if needed

---

## Status

- [x] SharePoint folder identified
- [x] Free no-Entra mode documented (OneDrive sync)
- [ ] Azure App Registration created (optional advanced mode)
- [ ] Service principal secrets configured (optional advanced mode)
- [ ] Power Automate flow created (optional)

---

## Notes

- The URL provided includes query parameters and view IDs — these are for direct browsing
- The clean path for sync and links is: `/Shared Documents/AI Agent MVP/PPTS`
- In default mode, folder structure must already exist in the synced SharePoint library

---

## Contact

For questions about SharePoint permissions or setup, reach out to your EPAM IT/Cloud team.

---

## Version

v1.0 — March 2026
