# 🛠 zaxy-Framework (v0.2.1)

zaxy is a powerful Python utility library that simplifies standard boilerplate code into clean, one-line commands.
zaxy — это производительная библиотека для Python, превращающая громоздкий стандартный код в чистые однострочные команды.

[EN] Developed by maks39P. Created on February 8, 2026, by a 14-year-old developer with minimal use of AI.
[RU] Разработчик: maks39P. Создано 8 февраля 2026 г. 14-летним разработчиком с минимальным использованием ИИ.

-----------------------------------------------------------
EN | Installation
-----------------------------------------------------------
pip install zaxy

EN | Core Documentation

0.Framework initialization inside the code (required)
- connect()

1. Console Output & Control
- tx(*args): Shortcut for print().
- clr() / clear(): Clears terminal screen (supports Windows/Linux).
- pau(text) / pause(text): Execution pause (replaces input() for waiting).

2. Smart Input & Global Variables
*Important: These functions inject variables directly into the global scope (globals).*
- ir("var_name", "prompt"): Replaces [ var_name = input("prompt") ]
- irn("var_name", "prompt"): Replaces [ var_name = int(input("prompt")) ] (includes protection against non-integer input).
- irf("var_name", "prompt"): Replaces [ var_name = float(input("prompt")) ] (supports both dots and commas).

3. File System (OS wrappers)
- ls(path): Returns list of files in directory.
- gwd(): Returns current working directory path.
- md(name): Creates a new directory.
- rm(path): Removes a FILE (does not remove directories). Includes Xa-System-Error protection.
- ren(old, new): Renames a file or directory.

4. Randomization
- rn(a, b): Returns random integer (randint).
- rc(list): Returns random element from list (choice).
- sh(list): Shuffles list and returns it.

-----------------------------------------------------------
RU | Инструкция по использованию
-----------------------------------------------------------
pip install zaxy

RU | Техническая документация

0.подключение фраемворка внутри кода(обязательно)
- connect()

1. Вывод и управление консолью
- tx(*args): Сокращение для print().
- clr() / clear(): Полная очистка консоли (Windows/Linux).
- pau(text) / pause(text): Пауза выполнения кода (ожидание нажатия Enter).

2. Умный ввод и глобальные переменные
*Важно: Эти функции создают переменные сразу в глобальной области видимости (globals).*
- ir("имя", "текст"): Заменяет [ имя = input("текст") ]
- irn("имя", "текст"): Заменяет [ имя = int(input("текст")) ] (с защитой от ввода букв вместо чисел).
- irf("имя", "текст"): Заменяет [ имя = float(input("текст")) ] (автоматически меняет запятую на точку).

3. Работа с системой (OS модули)
- ls(путь): Список содержимого папки.
- gwd(): Получение пути текущей рабочей директории.
- md(имя): Создание новой папки.
- rm(путь): Удаление ФАЙЛА (не папки). Включает обработку Xa-System-Error.
- ren(старое, новое): Переименование файла или папки.

4. Рандомизация и списки
- rn(a, b): Случайное целое число от a до b.
- rc(список): Случайный выбор элемента из списка.
- sh(список): Перемешивание элементов списка (shuffle).

-----------------------------------------------------------
Contacts / Контакты:
Email: dekabri2316@gmail.com
Telegram: @maks39P
-----------------------------------------------------------