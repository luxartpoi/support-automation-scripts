from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запуск браузера (используем webdriver-manager для автоматической настройки)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Без графического интерфейса (можно убрать для отладки)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открываем страницу отзывов
driver.get("https://partner.microsoft.com/...")  # URL страницы отзывов
time.sleep(5)

# Логинимся (если требуется)
# username = driver.find_element(By.ID, "username")
# password = driver.find_element(By.ID, "password")
# username.send_keys("your_email")
# password.send_keys("your_password")
# password.send_keys(Keys.RETURN)
# time.sleep(5)

# Получаем все отзывы
reviews = driver.find_elements(By.CLASS_NAME, "review-class")  # Указать актуальный класс отзывов

for review in reviews:
    review_text = review.text  # Получаем текст отзыва

    # Генерируем ответ (можно добавить API ChatGPT)
    answer = f"Спасибо за ваш отзыв! Если у вас есть вопросы, напишите нам на support@safe-in-cloud.com."

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

print("Все отзывы обработаны!")
driver.quit()
