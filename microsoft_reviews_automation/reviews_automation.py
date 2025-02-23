import time
import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Настройки OpenAI API
OPENAI_API_KEY = "your_openai_api_key"  # ЗАМЕНИТЬ на свой ключ

def generate_response(review_text):
    """Генерирует ответ на отзыв с помощью GPT-4o."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Теперь используем GPT-4o
            messages=[
                {"role": "system", "content": "Ты — профессиональный саппорт __________. Отвечай тепло, четко и информативно."},
                {"role": "user", "content": f"Напиши ответ на этот отзыв: {review_text}"}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Ошибка OpenAI: {e}")
        return "Спасибо за ваш отзыв! Если у вас есть вопросы, напишите нам на support@_________.com."

# Запуск браузера в headless-режиме
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открываем страницу отзывов
driver.get("https://partner.microsoft.com/...")  # Заменить на реальный URL
time.sleep(5)

# Получаем все отзывы
reviews = driver.find_elements(By.CLASS_NAME, "review-class")  # Указать актуальный класс отзывов

for review in reviews:
    review_text = review.text.strip()
    print(f"Обрабатываем отзыв: {review_text[:100]}...")

    # Генерируем ответ через GPT-4o
    answer = generate_response(review_text)
    print(f"Ответ: {answer}")

    # Нажимаем "Reply"
    reply_button = review.find_element(By.CLASS_NAME, "reply-button")
    reply_button.click()
    time.sleep(2)

    # Вставляем ответ
    text_area = driver.find_element(By.CLASS_NAME, "text-area")
    text_area.send_keys(answer)

    # Вставляем email
    email_field = driver.find_element(By.CLASS_NAME, "email-field")
    email_field.send_keys("support@safe-in-cloud.com")

    # Отправляем
    send_button = driver.find_element(By.CLASS_NAME, "send-button")
    send_button.click()
    time.sleep(3)

print("✅ Все отзывы обработаны!")
driver.quit()
