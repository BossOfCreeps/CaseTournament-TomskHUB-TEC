# CaseTournament-TomskHUB-TEC
Видение решения от команды NullPointerException задания компании ООО НПП "ТЭК" в рамках кейс-турнира от TomskHUB

Параметры:
* Дата изготовления
* Вес заготовки
* Геометрические параметры заготовки
* Состав
* Отметка о прохождении контроля качества

Алгоритм работы:
1) регистрация
* получаем заготовку на склад
* вручную записываем в форму параметры (в будущем можно заменить на сочетание из весов и датчиков расстояния)
* данные заносятся в форму
* возвращаем с сервера ID
* отправлякется SQL запрос на сервер на запись данных 
* осущетсвляем возможность печати кода на принтере
2) использование
* пользоватль с портативным устройством подходит к qr коду
* считывает всю информацию
* чекаем интернет соединение
* если есть, то смотрим есть ли на сервере такое
* если нет, то 