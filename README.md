# HelloSysadmin
Это набор скриптов для удалённого запуска смешнявок(картинки, проги, звуки) на электронной доске через телеграмм бота.
50% работы взял - https://github.com/SRLQNL

Раздел - Установка бота:

п.1 "Пинкод": 

1)в качестве защиты от дудоса бота и соответственно перехвата управления добавлен пинкод.

faq:
Как поменять пинкод? - Пинкод можно изменить изменив число после "_pin=".
Какие правила установки пинкода? - Пинкод должен быть числовой без точки(int)
Можно ли убрать пинкод? - Убрать пинкод через конфиг нельзя(опытные могут вырезать его на уровне кода) в целях безопасности
Какой пинкод по умолчанию? - С коробки Пинкод равен 1


п.2 "Токен бота и сам Бот: 

Создать бота, а соответственно получить токен можно через тг бота @BotFather.
1) Заходим в тг бота @BotFather и кликаем на /start
2) Вводим/нажимаем на /newbot
3) Придумываем имя
4) Придумываем юзернейм. Юзернэйм должен быть на латинице и заканчиваться на "_bot", например "test_bot" запомним этот юзернэйм т.к переходить в чат к боту через него
5) Получаем ссылку на бота и HTTP API, он же токен. Токен, который мы получили записываем в переменную "token" после "="


п.3 "id таблицы и таблица":

1) Открываем Google Sheets(таблицы) и создаём таблицу. Ничего не меняем!!! Для правильно копирования ссылки нажимаем на "Настройки доступа" и выбираем в пункте прав на изменение таблицы "Все у кого есть ссылка". Ниже нажимаем кнопку "Копировать ссылку"
2) Открывам блокнот и вствляем ссылку. Id таблицы находится в ссылке на таблицу(id находится после d/ и до /edit, в моём случае - 1RKFthr5TGKE5BCUBmNdRJgH-vPfgh_bj
3) Записываем в переменную "spreadsheet_id" id нашей таблицы после "="
!!!Важно:
Ничего, кроме того, что сказано в readme не трогайте, что связано с таблицей и её настройками!!!
