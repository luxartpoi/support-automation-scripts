## README (English)

### 🛠 Unspamming Tickets in Zoho Desk

This script automatically removes the "Spam" label from tickets in **Zoho Desk**.

### 🚀 How it works?
1. Fetches a list of tickets from a specific **viewId**.
2. Sends requests to the Zoho API to remove the "Spam" flag (**isSpam=false**).
3. Processes tickets in batches of 50 to comply with API limits.

### 📌 Requirements
- **Python 3.8+**
- Zoho Desk API access

### 🔧 Installation and Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python unspam_zoho_tickets_bulk.py
```

### ⚠ Important
Before running, **set the correct parameters in the script** (`ORG_ID`, `ACCESS_TOKEN`, `VIEW_ID`). **Do not expose your API keys publicly!**

---

## README (Русский)

### 🛠 Разспамливание тикетов в Zoho Desk

Этот скрипт автоматически снимает метку "Спам" у тикетов в **Zoho Desk**. 

### 🚀 Как работает?
1. Получает список тикетов из заданного представления (**viewId**).
2. Отправляет запросы в API Zoho, чтобы снять отметку "Спам" (**isSpam=false**).
3. Работает пакетами по 50 тикетов, чтобы избежать ограничения API.

### 📌 Требования
- **Python 3.8+**
- Доступ к API Zoho Desk

### 🔧 Установка и запуск
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск скрипта
python unspam_zoho_tickets_bulk.py
```

### ⚠ Важно
Перед запуском **укажите правильные параметры в коде** (`ORG_ID`, `ACCESS_TOKEN`, `VIEW_ID`). **Не выкладывайте свои ключи в открытый доступ!**

---
