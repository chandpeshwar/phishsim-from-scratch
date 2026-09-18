# hMailServer Setup Guide — Phishing Simulator

hMailServer is a free Windows mail server that GoPhish uses to deliver simulation emails.

---

## 1. Download and Install

- Download from: https://www.hmailserver.com/download
- Run the installer, choose **"Install hMailServer"**
- Select **"Use built-in database engine (Microsoft SQL Compact)"**
- Set an administrator password when prompted — save this, you will need it

---

## 2. Add Your Domain

1. Open hMailServer Administrator
2. Click **"Add domain"**
3. Enter your domain name (e.g. `phishsim.local` or your real domain)
4. Click **"Save"**

---

## 3. Create a Mail Account

1. Expand your domain in the left panel
2. Click **"Accounts"** → **"Add"**
3. Fill in:

| Field | Value |
|-------|-------|
| Address | `noreply@yourdomain.com` |
| Password | Choose a strong password |
| Max size | 100 MB |

4. Click **"Save"**

---

## 4. Configure SMTP

1. Go to **Settings** → **Protocols** → **SMTP**
2. Enable SMTP on port **25**
3. Go to **Settings** → **Advanced** → **IP Ranges**
4. Add your server IP and set it to allow relay

---

## 5. Configure DKIM Signing

1. Go to **Domains** → your domain → **DKIM Signing**
2. Check **"Use DKIM signing"**
3. Set selector to: `mail`
4. Paste your private key content from `dkim_private.key`
5. Click **"Save"**

---

## 6. Test the Setup

Open PowerShell and run:

    telnet localhost 25

If you see a response starting with `220`, hMailServer is running correctly.

---

## 7. Configure GoPhish to Use hMailServer

In GoPhish, go to **Sending Profiles** → **New Profile** and fill in:

| Field | Value |
|-------|-------|
| Name | Local SMTP |
| Interface Type | SMTP |
| Host | 127.0.0.1 |
| Port | 25 |
| From Address | noreply@yourdomain.com |

Click **"Save Profile"**.

---

## Notes

- hMailServer runs as a Windows service automatically after install
- Logs are stored at: `C:\Program Files (x86)\hMailServer\Logs\`
- If emails are not delivering, check the SMTP log for error details
