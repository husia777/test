Команды для запуска сервиса 
1) git clone https://github.com/husia777/test.git
2) cd test
3) docker compose -f docker-compose.yml up --build -d
4) docker exec -it api  /bin/sh 
5) cd src/infrastructure/database
6) alembic upgrade head 
7) переходим  http://0.0.0.0:8080/docs
8) сначала выполняем этот запрос http://0.0.0.0:8080/docs#/default/save_all_currencies_currencies_save_get
9) а дальше как душе угодно )
