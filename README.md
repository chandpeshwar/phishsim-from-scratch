# Phishing Simulator From Scratch

Build a fully functional phishing simulation environment using free, open source tools — no vendor, no subscription, no data leaving your machine.

This is the companion repository for the  blog series:
**"Building a Phishing Simulator from Scratch"**

> ⚠️ **Legal Disclaimer:** This repository is intended for educational and defensive security purposes only. All tools and techniques are for authorized security testing within your own organization. Never use these against systems or individuals without explicit written permission.

---

## What's Inside

| Folder | Contents |
|--------|----------|
| `part1/config/` | GoPhish config, hMailServer setup guide, DNS records reference |
| `part1/templates/` | 3 phishing email templates + training landing page |
| `part1/targets/` | Sample target list CSV format |
| `part1/authorization/` | Written authorization letter template |

---

## Tools Used

- [GoPhish](https://getgophish.com/) — Phishing simulation platform
- [hMailServer](https://www.hmailserver.com/) — Windows mail server
- [NSSM](https://nssm.cc/) — Run GoPhish as a Windows service
- [OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) — DKIM key generation

---

## Blog Series

- Part 1 — Architecture, Setup, and Your First Campaign *(you are here)*
- Part 2 — AI-Generated Lures, Automated OSINT, and Docker Setup *(coming soon)*

---

## Who This Is For

- SOC analysts and blue teamers
- Security awareness program managers
- Anyone who wants to understand how phishing simulations work under the hood

---

*Built and maintained by the Eswar*
