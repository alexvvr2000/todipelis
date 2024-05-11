FROM mariadb:11.3

ENV MYSQL_ROOT_PASSWORD_FILE=/run/secrets/root-password

COPY ./00-esquema.sql /docker-entrypoint-initdb.d/
COPY ./funciones/*.sql /docker-entrypoint-initdb.d/
COPY ./procedureActualizar/*.sql /docker-entrypoint-initdb.d/
COPY ./procedureBorrar/*.sql /docker-entrypoint-initdb.d/
COPY ./procedureObtener/*.sql /docker-entrypoint-initdb.d/