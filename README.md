# RU
# Автогенератор мерча по бренду

## Описание:

Телеграм-бот `@merch_generator_bot`, генерирующий мерч (а именно футболку) с рисунком по текстовому описанию

## Команда:
- Калиниченко Михаил – капитан, Backend, CV разработчик
- Соколов Дмитрий – NLP, CV, Backend разработчик
- Переладова Алина – технический писатель 

## Кураторы:
- Созинов Иван – руководитель команды, FrontEnd разработчик

# Инструкция по использованию бота: 

## Генерация футболки с рисунком:

1) Введите текстовое описание футболки, указав

   - Название бренда, логотип которого вы хотите видеть на футболке
   - Основной цвет футболки
   - Для какого мероприятия предназначена футболка

2) Дождитесь, пока бот сгенерирует изображение:)

## Запуск бота на своём сервере:

Для запуска рекомендуется использовать `python 3.8` и ОС `Ubuntu 21.04`

1) склонируйте репозиторий 

`git clone https://github.com/mikhail-7975/merch-autogenerator.git`
2) установите все библиотеки 

`pip install -r requirements.txt`

Для установки YandexImageParser следуйте инструкции, указанной в репозитории https://github.com/Ulbwaa/YandexImagesParser/

3) Создайте в корневой папке проекта файл `config.py`, в котором укажите URL своего телеграм-бота

```python
telegram_bot_url = "str_with_your_url"
```
4) Запустите файл `run.py`

`python run.py`

5) Отправьте текстовый запрос на генерацию изображения и дождитесь результата:)

# EN
# Brand merchandise generator

## Description:

Telegram bot `@merch_generator_bot` that generates merchandise (namely, a T-shirt) with a picture based on a text description

## Team:
- Mikhail Kalinichenko - captain, Backend, CV developer
- Dmitry Sokolov - NLP, CV, Backend developer
- Pereladova Alina - technical writer

## Curators:
- Sozinov Ivan - team leader, FrontEnd developer

# Instructions for using the bot:

## Generation of a t-shirt with a picture:

1) Enter a textual description of the T-shirt, specifying

   - The name of the brand whose logo you want to see on the T-shirt
   - The main color of the T-shirt
   What event is the T-shirt for?

2) Wait for the bot to generate the image :)

## Run the bot on your server:

To run it is recommended to use `python 3.8` and `Ubuntu 21.04 OS`

1) clone the repository

`git clone https://github.com/mikhail-7975/merch-autogenerator.git`
2) install all libraries

`pip install -r requirements.txt`

To install YandexImageParser, follow the instructions in the repository https://github.com/Ulbwaa/YandexImagesParser/

3) Create a file `config.py` in the root folder of the project, in which specify the URL of your telegram bot

```python
telegram_bot_url = "str_with_your_url"
```
4) Run the file `run.py`

`python run.py`

5) Send a text request to generate an image and wait for the result :)