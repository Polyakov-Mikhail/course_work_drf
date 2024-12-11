# Курсовая 7. DRF

# Напоминание о привычках

### Разработал - Поляков Михаил

## Контекст 
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к нам с запросом реализовать трекер полезных привычек.
## Настройка и установка

### 1. Клонирование репозитория

```bash
git@github.com:Polyakov-Mikhail/course_work_7.git
```
### 2. Скопируйте файл env.example в .env:
Откройте .env и замените значения переменных на свои собственные
```bash
cp .env.example .env
```
### 3. Установление зависимостей
```bash
poetry shell
poetry install
```
### 4. Запуск миграций
Чтобы запустить миграции, используйте следующую команду:
```bash
python3 manage.py migrate
```
### 5. Установка Fixture
Загрузка тестовых фикстур для базы данных:
```bash
python3 manage.py loaddata data.json
```

### 6. Run Server
```bash
python3 manage.py runserver
```
Сервер будет доступен по адресу http://127.0.0.1:8000


### 7. Запуск Coverage Tests
Для запуска тестов и проверки покрытия тестами исполььзуйте команды:
   ```bash
coverage run manage.py test
coverage report
   ```

### 8. Запуск Celery Worker
Чтобы запустить Celery worker, используйте следующую команду:
```bash
celery -A habit_reminder worker --loglevel=info
```

### 9. Запуск Celery Beat
Чтобы запустить Celery Beat scheduler, используйте следующую команду:
```bash
celery -A habit_reminder beat --loglevel=info
```