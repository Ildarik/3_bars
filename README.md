# Ближайшие бары

На основе открытых данных о [московских барах](http://data.mos.ru/opendata/7710881420-bary) скрипт рассчитывает:

1. Самый большой бар
2. Самый маленький бар
3. Самый близкий бар - текущие gps-координаты необходимо ввести с клавиатуры.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.

Необходимо скачать и передать в качестве аргумента [JSON-файл с данными](https://op.mos.ru/EHDWSREST/catalog/export/get?id=84505)

Запуск на Linux:

```#!bash
$ python3 bars.py data-2897-2016-11-23.json 

Самый большой бар:  Спорт бар «Красная машина»
Самый маленький бар:  БАР. СОКИ
Введите широту: 37.449144
Введите долготу: 56.007087
Самый близкий бар:  Капитан Конрад
```
Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
