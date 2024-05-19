#!/bin/bash

tablasBases=("Usuario" "Pelicula" "ListaCriticas" "ListaFavoritos")

for tabla in "${tablasBases[@]}"; do
    echo "GRANT EXECUTE ON ${tabla}.* TO 'api'@'%';"
done
