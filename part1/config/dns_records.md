# DNS Records Reference — Phishing Simulator Setup

Configure these three DNS records on your domain before running any campaigns.
Without them, your emails will land in spam or get rejected entirely.

---

## SPF Record

| Field | Value |
|-------|-------|
| Type | TXT |
| Host | @ |
| Value | `v=spf1 ip4:YOUR.SERVER.IP.HERE ~all` |
| TTL | 3600 |

**What it does:** Tells receiving mail servers that your IP is allowed to send email for your domain.

---

## DKIM Record

| Field | Value |
|-------|-------|
| Type | TXT |
| Host | `mail._domainkey` |
| Value | `v=DKIM1; k=rsa; p=YOUR_PUBLIC_KEY_HERE` |
| TTL | 3600 |

**What it does:** Adds a digital signature to your emails so receivers can verify they were not tampered with in transit.

**Generate your DKIM keys on Windows (PowerShell):**
```powershell
openssl genrsa -out dkim_private.key 2048
openssl rsa -in dkim_private.key -pubout -out dkim_public.key
Get-Content dkim_public.key
```

Copy the public key output (remove the header/footer lines) and paste it into the `p=` field above.

---

## DMARC Record

| Field | Value |
|-------|-------|
| Type | TXT |
| Host | `_dmarc` |
| Value | `v=DMARC1; p=none; rua=mailto:admin@yourdomain.com` |
| TTL | 3600 |

**What it does:** Tells receiving servers what to do if SPF or DKIM checks fail. Start with `p=none` (monitor only) during testing.

---

## Verification

After adding all three records, verify them using:
- [MXToolbox SPF Checker](https://mxtoolbox.com/spf.aspx)
- [MXToolbox DKIM Checker](https://mxtoolbox.com/dkim.aspx)
- [MXToolbox DMARC Checker](https://mxtoolbox.com/dmarc.aspx)

Allow up to 24 hours for DNS propagation.
