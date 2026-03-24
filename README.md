# Effective Mobile

Python-бэкенд за Nginx reverse proxy, всё в Docker.

---

## Как это работает


Запрос идёт так: `curl localhost` → `nginx:80` → `backend:8080` → `"Hello from Effective Mobile!"`

Бэкенд снаружи недоступен - только из Docker-сети через nginx.

---

## Быстрый старт

### Что нужно

- Docker ≥ 24
- Docker Compose plugin ≥ 2

### Запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/<your-org>/effective-mobile-docker.git
cd effective-mobile-docker

# 2. Если порт 80 занят меняем в .env
cp .env.example .env
# NGINX_HOST_PORT=8080

# 3. Собираем и запускаем
docker compose up --build -d
```

Ждём пока оба контейнера станут healthy:

```bash
docker compose ps
```

```
NAME          STATUS
em_backend    Up (healthy)
em_nginx      Up (healthy)
```

### Проверка

```bash
curl http://localhost
```

Ответ:
```
Hello from Effective Mobile!
```

---

## Полезные команды

```bash
# Логи в реальном времени
docker compose logs -f

# Логи конкретного сервиса
docker compose logs -f backend

# Остановить
docker compose down

# Остановить и удалить образы
docker compose down --rmi all
```

---

## Структура проекта

```
├── backend/
│   ├── .dockerignore
│   ├── Dockerfile        
│   └── app.py           
├── nginx/
│   ├── .dockerignore
│   ├── Dockerfile       
│   └── nginx.conf       
├── .env.example         
├── .gitignore
├── docker-compose.yml   
└── README.md
```

---

## Технологии

| Что         | Версия / образ    |
| ----------- | ----------------- |
| Бэкенд      | Python 3.12-slim  |
| Прокси      | nginx 1.27-alpine |
| Оркестрация | Docker Compose v2 |
