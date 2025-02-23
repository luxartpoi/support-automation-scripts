import requests
import time

# -----------------------
# ВАШИ НАСТРОЙКИ (ЗАГЛУШКИ)
# -----------------------
ORG_ID = "YOUR_ORG_ID"                # Пример: "123456789"
ACCESS_TOKEN = "YOUR_OAUTH_TOKEN"     # Пример: "1000.xxxx..."
VIEW_ID = "YOUR_VIEW_ID"             # Пример: "1073894000000001234"
BASE_URL = "https://desk.zoho.com/api/v1"  # Оставляем адрес API для .com
HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# -----------------------
# ФУНКЦИЯ 1: Получение списка тикетов (ID) из представления
# -----------------------
def get_tickets_from_view(view_id):
    """
    Постранично выгружает тикеты (ID) из указанного viewId.
    Возвращает список ID в виде строк.
    """
    all_ticket_ids = []
    from_param = 1
    limit_param = 50  # согласно документации, max 50

    while True:
        url = f"{BASE_URL}/tickets?viewId={view_id}&from={from_param}&limit={limit_param}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"Ошибка при получении тикетов (viewId={view_id}): {resp.status_code}, {resp.text}")
            break

        data = resp.json()
        tickets = data.get("data", [])
        if not tickets:
            # Пустой список — значит, все страницы прошли
            break

        # Собираем ID тикетов
        for t in tickets:
            tid = t.get("id")
            if tid:
                all_ticket_ids.append(tid)

        from_param += limit_param
        # Пауза, чтобы не перегружать API
        time.sleep(0.3)

    return all_ticket_ids

# -----------------------
# ФУНКЦИЯ 2: Снятие метки «Спам» (isSpam=false) у списка тикетов
# -----------------------
def unspam_tickets(ticket_ids):
    """
    Делим тикеты на партии (batch) по 50 штук и шлём запрос POST /tickets/markSpam,
    выставляя isSpam=false.
    """
    BATCH_SIZE = 50
    url = f"{BASE_URL}/tickets/markSpam"

    total = len(ticket_ids)
    print(f"Всего тикетов для разспамливания: {total}")

    for i in range(0, total, BATCH_SIZE):
        batch = ticket_ids[i:i + BATCH_SIZE]
        payload = {
            "isSpam": False,            # ключевой флаг: снимаем спам
            "ids": batch,              # список ID
            "contactSpam": False,      # не трогаем контакт
            "handleExistingTickets": False  # не трогаем остальные тикеты этого контакта
        }

        resp = requests.post(url, headers=HEADERS, json=payload)
        batch_number = i // BATCH_SIZE + 1

        if resp.status_code in [200, 202]:
            print(f"Партия {batch_number}: {len(batch)} тикетов → УСПЕХ")
        else:
            print(f"Партия {batch_number}: ОШИБКА {resp.status_code}: {resp.text}")

        # Небольшая пауза между батчами
        time.sleep(0.3)

# -----------------------
# ОСНОВНОЙ БЛОК (main)
# -----------------------
if __name__ == "__main__":
    print(f"Получаем тикеты из представления (viewId={VIEW_ID})...")
    spam_ticket_ids = get_tickets_from_view(VIEW_ID)
    print(f"Найдено {len(spam_ticket_ids)} тикетов в данном View.")

    if spam_ticket_ids:
        print("Начинаем «разспамливать»...")
        unspam_tickets(spam_ticket_ids)
        print("Готово! Проверьте в Zoho Desk.")
    else:
        print("Тикетов не найдено. Возможно, уже нет спам-тикетов или viewId неверен.")
