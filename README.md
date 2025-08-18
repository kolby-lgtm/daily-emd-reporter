# Daily EMD Reporter - GitHub Actions Automation

🏠 **Automated Daily EMD Due Report for OneRoof Real Estate**

This repository contains a fully automated system that runs daily in GitHub's cloud infrastructure to fetch EMD due properties from Podio and post them to Slack.

## 🚀 **Features**

- ✅ **100% Cloud-Based:** Runs in GitHub Actions (no local computer required)
- ✅ **Daily Automation:** Executes every day at 7:00 AM MST (14:00 UTC)
- ✅ **Reliable:** GitHub's enterprise infrastructure with 99.9% uptime
- ✅ **Free:** No cost for this usage level
- ✅ **Secure:** All credentials stored as encrypted GitHub secrets
- ✅ **Monitoring:** Built-in logging and error reporting
- ✅ **Manual Trigger:** Can be run manually anytime

## 📅 **Schedule**

- **Frequency:** Every day (Monday through Sunday)
- **Time:** 7:00 AM MST (14:00 UTC)
- **Target:** #dispositions channel in Slack
- **Data Source:** Daily EMD Due Report from Podio

## 🔧 **Setup Instructions**

### **Step 1: Create GitHub Repository**

1. Go to [GitHub.com](https://github.com) and sign in
2. Click "New repository"
3. Name it: `daily-emd-reporter`
4. Make it **Private** (recommended for business automation)
5. Click "Create repository"

### **Step 2: Upload Files**

Upload all the files from this folder to your new GitHub repository:
- `daily_emd_reporter.py`
- `requirements.txt`
- `.github/workflows/daily-emd-report.yml`
- `README.md`

### **Step 3: Configure Secrets**

In your GitHub repository, go to **Settings > Secrets and variables > Actions** and add these secrets:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `PODIO_CLIENT_ID` | `daily-emd-reporter` | Your Podio API client ID |
| `PODIO_CLIENT_SECRET` | `mJ0OTDhO3jZTL56hxzWVG21plqO6ruwSgyNPU1FkYJbF7z4rjMxq7cXBubaGY1Om` | Your Podio API client secret |
| `PODIO_USERNAME` | `kolby@oneroofrealestate.com` | Your Podio username |
| `PODIO_PASSWORD` | `Renata0413!` | Your Podio password |
| `PODIO_APP_ID` | `28097914` | Deals 2.0 app ID |
| `PODIO_VIEW_ID` | `61038989` | Daily EMD Due Report view ID |
| `SLACK_WEBHOOK_URL` | `https://hooks.slack.com/services/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` | Your Slack webhook URL |

### **Step 4: Test the Automation**

1. Go to **Actions** tab in your repository
2. Click on "Daily EMD Reporter" workflow
3. Click "Run workflow" button
4. Click "Run workflow" to trigger a manual test
5. Check your #dispositions Slack channel for the report

### **Step 5: Verify Daily Schedule**

The automation will now run automatically every day at 7:00 AM MST. You can monitor executions in the **Actions** tab.

## 🛠️ **Management**

### **Manual Execution**
- Go to **Actions** tab
- Click "Daily EMD Reporter"
- Click "Run workflow"

### **View Execution History**
- Go to **Actions** tab
- See all past executions with success/failure status

### **Monitor Logs**
- Click on any execution in the Actions tab
- View detailed logs for troubleshooting

### **Update Credentials**
- Go to **Settings > Secrets and variables > Actions**
- Update any secret values as needed

## 📊 **What Gets Posted**

The system automatically posts a formatted message to #dispositions containing:

```
📋 Daily EMD Due Report - Property Addresses

1. 4456 Thunder Rd, Dallas, TX 75244
2. 15414 Empanada Dr, Houston, TX 77083
3. 4220 Kent Dr, Powder Springs, GA 30127

Total: 3 properties with EMD due
```

## 🔍 **Troubleshooting**

### **If the automation stops working:**
1. Check the **Actions** tab for error messages
2. Verify all secrets are still valid
3. Check if Podio API credentials have changed
4. Verify Slack webhook is still active

### **Common Issues:**
- **Authentication errors:** Update Podio credentials in secrets
- **Slack posting fails:** Verify webhook URL in secrets
- **No data found:** Check if Podio view ID is correct

## 🎯 **Advantages**

- ✅ **No Computer Required:** Runs entirely in the cloud
- ✅ **Always Available:** GitHub's 99.9% uptime guarantee
- ✅ **Free Operation:** No monthly costs
- ✅ **Secure:** Enterprise-grade security for credentials
- ✅ **Reliable:** Automatic retry and error handling
- ✅ **Maintainable:** Easy to update and monitor
- ✅ **Version Controlled:** All changes tracked in Git

## 📞 **Support**

This automation system is designed to run maintenance-free. If you need to make changes:

1. **Update schedule:** Edit `.github/workflows/daily-emd-report.yml`
2. **Update credentials:** Modify secrets in repository settings
3. **Update logic:** Edit `daily_emd_reporter.py`

---

**🏠 Built for OneRoof Real Estate - Automated EMD Due Reporting**

