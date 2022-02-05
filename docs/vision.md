# 1. Введение
Цель данного документа - обозначить границы разрабатываемого бота “merch-generator”. В нем кратко рассматривается  модель, ее возможности, требования к ней.
# 2. Позиционирование
Разрабатываемый генератор должен уметь по вводным данным сгенерировать коллекцию мерча для заинтересованных компаний. Важно учитывать текстовое описание, которое повлияет на результат генерации.
Заказчиком выступают компании, заинтересованные в мерче для своих целей.
# 3. Описания совладельцев и пользователей
Владелец разрабатываемой системы - компания-заказчик. Ботом будет пользоваться event-менеджер.
# 4. Краткий обзор продукта
Основная цель – предоставить инструмент для генерации мерча к определенным событиям.
# 5. Возможности продукта
* запрос содержит название вещи;
* запрос содержит цвет;
* запрос содержит бренд;
* запрос содержит мероприятие;
* запрос содержит место проведения мероприятия;
* заказчик получает изображение элемента мерча.
# 6. Ограничения
Ограничения при разработке данной системы:
* возможность генерации только одного элемента мерча;
* по каждому запросу один вариант;
* требуется минимальное количество входных данных:

Технические ограничения не предусмотрены ввиду того, что разрабатываемая система не предполагается быть высоконагруженной.
# 7. Показатели качества
Показатели качества:
* понятные фотореалистичные изображения;
* соответствие мероприятию;
* соответствие текстовому описанию.
# 8. Приоритизация требований
Приоритетным требованием является обеспечение качества изображения мерча.
# 9. Другие требования к продукту
Требований по определению стандартов разработки, стандартов по эксплуатации, системных требований не предъявляется.
# 10. Требования к документации
Для описания системы требуется следующая документация:
* техническое задание - детальное описание требований к системе;
* руководство пользователя - описание порядка работы с системой;
* README - верхнеуровневое описание системы, файлов репозитория, инструкция quick start.






