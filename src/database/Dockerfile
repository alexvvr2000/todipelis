FROM mariadb:11.3

# esquema de la base
COPY ./00-esquema.sql /docker-entrypoint-initdb.d/
COPY ./1-funciones/*.sql /docker-entrypoint-initdb.d/
COPY ./2-procedureObtener/*.sql /docker-entrypoint-initdb.d/
COPY ./3-procedureInsert/*.sql /docker-entrypoint-initdb.d/
COPY ./5-procedureActualizar/*.sql /docker-entrypoint-initdb.d/
COPY ./4-procedureBorrar/*.sql /docker-entrypoint-initdb.d/

# script de permisos para usuario
COPY ./creacionUsuario.sh /scripts/
RUN chmod +x /scripts/creacionUsuario.sh

# creando usuario para flask
RUN bash /scripts/creacionUsuario.sh > /docker-entrypoint-initdb.d/15-usuarioFlask.sql