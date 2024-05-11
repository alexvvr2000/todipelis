FROM mariadb:11.3

ENV MYSQL_ROOT_PASSWORD_FILE=/run/secrets/root-password

COPY ./00-esquema.sql /docker-entrypoint-initdb.d/
COPY ./1-funciones/*.sql /docker-entrypoint-initdb.d/
COPY ./2-procedureObtener/*.sql /docker-entrypoint-initdb.d/
COPY ./3-procedureInsert /docker-entrypoint-initdb.d/
COPY ./5-procedureActualizar/*.sql /docker-entrypoint-initdb.d/
COPY ./4-procedureBorrar/*.sql /docker-entrypoint-initdb.d/