# Автогенератор мерча по бренду

## Команда:
- Калиниченко Михаил – капитан, Backend, CV разработчик
- Соколов Дмитрий – NLP, CV, Backend разработчик
- Переладова Алина – технический писатель 

## Кураторы:
- Созинов Иван – руководитель команды, FrontEnd разработчик

# Usage service: 

## via api:

send request: POST http://server:port/api query="example_text_string"

expected response: json with array of urls of images: {"images": [ url1, url2 ]}

download ones: GET url1, GET url2

## via web:

Go to http://server:port and enter the text to the box and press button

## via Telegram bot:

Got to chat with @TestTG11_bot

Write message /start Your text string
