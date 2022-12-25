# Service mailing 

Работает с Python 3.11, Ubuntu 20.04
Для того, чтобы установить данный сервис, необходимо выполнить следующие действия:
- Установить PostgreSQL 14
  - Создать базу данных
  - Установить Docker и Docker Compose
  - Клонировать данный репозиторий
    - Перейти в папку с проектом
    - Создать файл .env
    - Заполнить файл .env
  - Выполнить команду docker-compose build
  - Выполнить команду docker-compose up -d

## Установка PostgreSQL 14

Для установки PostgreSQL 14 необходимо выполнить следующие действия:

- Добавить репозиторий PostgreSQL 14
  - sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
  - wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key
  - sudo apt-get update
  - sudo apt-get install postgresql-14 postgresql-contrib
- Создать базу данных
  - sudo -u postgres psql
  - CREATE DATABASE db_name;
  - CREATE USER user WITH PASSWORD 'password';
  - GRANT ALL PRIVILEGES ON DATABASE db_name TO user;
  - \q

## Установка Docker и Docker Compose

Для установки Docker и Docker Compose необходимо выполнить следующие действия:

- Установить Docker
  - sudo apt-get update
  - sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
  - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  - echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  - sudo apt-get update
  - sudo apt-get install docker-ce docker-ce-cli containerd.io

- Установить Docker Compose
  - sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  - sudo chmod +x /usr/local/bin/docker-compose
  - docker-compose --version

## Клонирование репозитория

Для клонирования репозитория необходимо выполнить следующие действия:

- Клонировать репозиторий
  - git clone
  - cd directory
  - cp .env.example .env
  - nano .env
  - docker-compose build
  - docker-compose up -d


## Работа с API

Для работы с API необходимо выполнить следующие действия:

Зайти в Swagger