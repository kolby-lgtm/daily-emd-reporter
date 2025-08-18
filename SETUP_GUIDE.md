# 🚀 GitHub Actions Setup Guide - Step by Step

## **Complete Setup Instructions for 24/7 Automation**

Follow these steps to set up your Daily EMD Reporter to run automatically in GitHub's cloud infrastructure.

---

## **Step 1: Create GitHub Account (if needed)**

1. Go to [github.com](https://github.com)
2. Click "Sign up" if you don't have an account
3. Choose a username and create your account
4. Verify your email address

---

## **Step 2: Create New Repository**

1. **Sign in to GitHub**
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Fill in repository details:**
   - Repository name: `daily-emd-reporter`
   - Description: `Automated Daily EMD Due Report for OneRoof Real Estate`
   - **Make it Private** (recommended for business use)
   - ✅ Check "Add a README file"
5. **Click "Create repository"**

---

## **Step 3: Upload Files to Repository**

### **Option A: Web Interface (Easier)**

1. **In your new repository, click "uploading an existing file"**
2. **Drag and drop these files:**
   - `daily_emd_reporter.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
3. **Create the workflow directory:**
   - Click "Create new file"
   - Type: `.github/workflows/daily-emd-report.yml`
   - Copy and paste the workflow content
4. **Commit the files**

### **Option B: Git Commands (Advanced)**

```bash
git clone https://github.com/YOUR_USERNAME/daily-emd-reporter.git
cd daily-emd-reporter
# Copy all files to this directory
git add .
git commit -m "Initial setup of Daily EMD Reporter"
git push origin main
```

---

## **Step 4: Configure Secrets (CRITICAL)**

1. **Go to your repository on GitHub**
2. **Click "Settings" tab**
3. **Click "Secrets and variables" > "Actions"**
4. **Click "New repository secret"**
5. **Add each secret one by one:**

### **Required Secrets:**

| Secret Name | Value |
|-------------|-------|
| `PODIO_CLIENT_ID` | `daily-emd-reporter` |
| `PODIO_CLIENT_SECRET` | `mJ0OTDhO3jZTL56hxzWVG21plqO6ruwSgyNPU1FkYJbF7z4rjMxq7cXBubaGY1Om` |
| `PODIO_USERNAME` | `kolby@oneroofrealestate.com` |
| `PODIO_PASSWORD` | `Renata0413!` |
| `PODIO_APP_ID` | `28097914` |
| `PODIO_VIEW_ID` | `61038989` |
| `SLACK_WEBHOOK_URL` | `https://hooks.slack.com/services/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` |

**For each secret:**
1. Click "New repository secret"
2. Enter the "Name" (exactly as shown above)
3. Enter the "Secret" value
4. Click "Add secret"

---

## **Step 5: Test the Automation**

1. **Go to "Actions" tab** in your repository
2. **You should see "Daily EMD Reporter" workflow**
3. **Click on the workflow name**
4. **Click "Run workflow" button** (on the right)
5. **Click "Run workflow"** to start a test
6. **Wait 1-2 minutes** for execution to complete
7. **Check your #dispositions Slack channel** for the report

---

## **Step 6: Verify Daily Schedule**

1. **The automation is now active!**
2. **It will run every day at 7:00 AM MST**
3. **Monitor executions in the "Actions" tab**
4. **Check Slack daily for reports**

---

## **🎯 Success Indicators**

### **✅ Setup Complete When:**
- Repository created with all files
- All 7 secrets configured
- Test execution successful (green checkmark)
- Report appears in #dispositions channel

### **📊 Daily Operation:**
- Check "Actions" tab for execution history
- Green checkmarks = successful runs
- Red X = failed runs (check logs)
- Reports appear in Slack at 7:00 AM MST

---

## **🔧 Maintenance**

### **Update Credentials:**
1. Go to Settings > Secrets and variables > Actions
2. Click on the secret to update
3. Enter new value
4. Click "Update secret"

### **Change Schedule:**
1. Edit `.github/workflows/daily-emd-report.yml`
2. Modify the cron expression: `'0 14 * * *'`
3. Commit the changes

### **View Logs:**
1. Go to Actions tab
2. Click on any execution
3. Click on "run-daily-report"
4. Expand "Run Daily EMD Reporter" to see logs

---

## **🆘 Troubleshooting**

### **Common Issues:**

**❌ "Authentication failed"**
- Check PODIO_USERNAME and PODIO_PASSWORD secrets
- Verify credentials are correct

**❌ "Slack posting failed"**
- Check SLACK_WEBHOOK_URL secret
- Verify webhook is still active

**❌ "No data found"**
- Check PODIO_APP_ID and PODIO_VIEW_ID
- Verify the view exists in Podio

**❌ "Workflow not running"**
- Check if repository is private (may need GitHub Pro for private repo actions)
- Verify workflow file is in correct location

---

## **💡 Pro Tips**

1. **Star your repository** to find it easily
2. **Enable email notifications** for failed runs
3. **Test manually** before relying on automation
4. **Keep credentials updated** if they change
5. **Monitor the Actions tab** weekly

---

**🎉 Congratulations! Your Daily EMD Reporter is now running 24/7 in the cloud!**

