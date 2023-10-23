# Чат бот для получения и пересылки данных в некоторый чат

_Сделал [Ananev Nikita](https://t.me/coma8765)_

> Решение первой тестовой задачи от BWG,
> согласно [техническому заданию](docs/TASK.md)

## Использование

### Переменное окружение

> Воспользуйтесь _dotenv_ (для Docker `.env.docker`), либо средства Докер для
> указания переменных

- **LOG_LEVEL** — уровень логирования, по умолчанию info, (возможные варианты:
  debug, info, warning, error , critical);
- **TELEGRAM_API_TOKEN** — токен для работы с Telegram;
- **TELEGRAM_CHAT_ID** — идентификатор "общего" чата.

### Docker Compose

_Скопируйте [`.env.example`](.env.example) в `.env.docker` и заполните его._

```shell
docker compose up -d  # Equal "make up" 
```

## Техническое описание

### Архитектура

> Архитектура придерживается методологии чистой архитектуры.
> Внешние взаимодействия описаны в [адаптерах](./src/adapters).
> Бизнес логика описана в [доменной части](./src/domain),
> а именно в главном и единственном [use-case](./src/domain/main.py).

### Библиотеки

* **aiogram** — асинхронное взаимодействие с Telegram API
* **environs** — адаптер переменного окружения

##### Библиотеки для разработки

* **unittest** — Unit-тестирование
* **mypy** — проверка типов
* **black** — форматер кода
* **pylint** — линтинг кода
* **isort** — сортировщик импортов

#### Граф зависимостей для производственного запуска

```text
aiogram==3.1.1
├── aiofiles [required: ~=23.1.0, installed: 23.1.0]
├── aiohttp [required: ~=3.8.5, installed: 3.8.6]
│   ├── aiosignal [required: >=1.1.2, installed: 1.3.1]
│   │   └── frozenlist [required: >=1.1.0, installed: 1.4.0]
│   ├── async-timeout [required: >=4.0.0a3,<5.0, installed: 4.0.3]
│   ├── attrs [required: >=17.3.0, installed: 23.1.0]
│   ├── charset-normalizer [required: >=2.0,<4.0, installed: 3.3.0]
│   ├── frozenlist [required: >=1.1.1, installed: 1.4.0]
│   ├── multidict [required: >=4.5,<7.0, installed: 6.0.4]
│   └── yarl [required: >=1.0,<2.0, installed: 1.9.2]
│       ├── idna [required: >=2.0, installed: 3.4]
│       └── multidict [required: >=4.0, installed: 6.0.4]
├── certifi [required: >=2023.7.22, installed: 2023.7.22]
├── magic-filter [required: ~=1.0.11, installed: 1.0.12]
├── pydantic [required: >=2.1.1,<2.4, installed: 2.3.0]
│   ├── annotated-types [required: >=0.4.0, installed: 0.6.0]
│   ├── pydantic-core [required: ==2.6.3, installed: 2.6.3]
│   │   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.7.1]
│   └── typing-extensions [required: >=4.6.1, installed: 4.7.1]
└── typing-extensions [required: ~=4.7.1, installed: 4.7.1]
environs==9.5.0
├── marshmallow [required: >=3.0.0, installed: 3.20.1]
│   └── packaging [required: >=17.0, installed: 23.2]
└── python-dotenv [required: Any, installed: 1.0.0]
```

## Тестирование

### Unit-tests

Частично [реализованно тестирование адаптера библиотеки телеграмм API](src/test/test_adapters/test_aiogram_adapter.py)

### Code quality

_Команда: `make pretty`_

#### Pylint

```text
>> pylint src
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

#### Black

```text
>> black src
All done! ✨ 🍰 ✨
20 files left unchanged.
```

#### Mypy

```text
>> mypy src
Success: no issues found in 20 source files
```

### Фотоотчёт

![screen-1.png](docs/images/screen-1.png)
![screen-2.png](docs/images/screen-2.png)
![screen-3.png](docs/images/screen-3.png)