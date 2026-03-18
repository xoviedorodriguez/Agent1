# SharePoint Configuration

## Site Details

| Setting | Value |
|---------|-------|
| **SharePoint Site URL** | `https://epam.sharepoint.com/sites/CPGOpportunities` |
| **Target Folder Path** | `/Shared Documents/AI Agent MVP/PPTS` |
| **Full Folder URL** | `https://epam.sharepoint.com/sites/CPGOpportunities/Shared%20Documents/AI%20Agent%20MVP/PPTS` |

---

## Upload Behavior

When the agent generates a `.pptx` file, it will be saved to:

```
https://epam.sharepoint.com/sites/CPGOpportunities/Shared Documents/AI Agent MVP/PPTS/[CAPABILITY-NAME]-deck-[YYYY-MM-DD].pptx
```

Example:
```
Data-Analytics-deck-2026-03-18.pptx
```

---

## Authentication (For Automated Uploads)

To enable automatic uploads to SharePoint, you need:

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

### Option 2: Delegated Authentication (User-based)
For manual workflows where the user uploads manually:
1. The agent generates the `.pptx` file locally
2. User authenticates to SharePoint via browser
3. User or Power Automate flow uploads the file

---

## Status

- [x] SharePoint folder identified
- [ ] Azure App Registration created (for automated uploads)
- [ ] Service principal secrets configured (in GitHub Secrets, never in code)
- [ ] Power Automate flow created (optional — for hands-free uploads)

---

## Notes

- The URL provided includes query parameters and view IDs — these are for direct browsing and are ignored during API uploads
- The clean path for API calls is: `/sites/CPGOpportunities/Shared Documents/AI Agent MVP/PPTS`
- The agent will create the folder structure if it doesn't exist (provided it has write permissions)

---

## Contact

For questions about SharePoint permissions or setup, reach out to your EPAM IT/Cloud team.

---

## Version

v1.0 — March 2026
