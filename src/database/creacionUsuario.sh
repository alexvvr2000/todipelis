#!/bin/bash

tablasBases=("Usuario" "Pelicula" "ListaCriticas" "ListaFavoritos")

echo "CREATE USER 'api'@'%' IDENTIFIED BY '${API_PASSWORD_FILE}';"

for tabla in "${tablasBases[@]}"; do
    echo "GRANT INSERT, UPDATE, DELETE, SELECT ON todipelis.${tabla} TO 'api'@'%';"
    echo "GRANT EXECUTE ON ${tabla}.* TO 'api'@'%' IDENTIFIED BY '${API_PASSWORD_FILE}';"
done
