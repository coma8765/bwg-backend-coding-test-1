# Technical specification

## Use cases

### Main

Получение от пользователя сообщение с ФИО + Изображение и отправка их в некоторый чат

## Requirements

- Docker Compose
- Usage dotenv file

### Other requirements

#### Code quality

- pylint - linter
- black - formatter
- isort - import sorting

#### Architecture

- the possibility of implementing another realization of the telegram API library

### Optimizations (optional)

- usage WebHook for communications with Telegram

## Original

```markdown
**Реализовать телеграм бота, который получает от пользователя данные: ФИО + скрин**
После этого бот пересылает эти данные в отдельный общий чат
То есть каждый пишет боту в лс, скидывает ему данные, после этого бот скидывает данные каждого человека в один чат

**Необходимо:**

- Опубликовать проект в github
- Проект должен быть собран в docker контейнеры и в docker-compose файл. Для запуска проекта должно быть достаточно
  набрать команду `docker compose up --build`
- README заполнить информацией по запуску, заполнению секретов и прикрепить отчет о тестировании
```