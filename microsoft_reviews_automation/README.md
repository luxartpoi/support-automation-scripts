# 🇬🇧 Microsoft Partner Center Review Automation

This script uses **Selenium** to automatically reply to reviews in Microsoft Partner Center.

## 🚀 How it works?
1. Opens the review page.
2. Extracts review texts.
3. Generates a response (ChatGPT API can be integrated).
4. Automatically inserts and submits the reply.

## 🔧 Requirements
- **Python 3.8+**
- **Google Chrome** (or Chromium)
- **Selenium** and **webdriver-manager** (installed automatically)

## 📌 Installation and Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python reviews_automation.py
```

## ⚠ Important
- Check the **HTML structure** on Microsoft’s website (`review-class`, `reply-button`, etc.).
- If the website changes, code updates might be needed.
