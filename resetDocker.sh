#!/bin/bash

contenedores=("baseTodiPelis")
imagenes=("todipelis_base")
volumenes=("folderDatosTodiPelis")

for contenedor in "${contenedores[@]}"; do
    if docker rm -v "${contenedor}" >/dev/null 2>&1; then
        echo "Contenedor ${contenedor} ha sido borrada"
    else
        echo "No se borro el contenedor ${contenedor}"
    fi
done

for imagen in "${imagenes[@]}"; do
    if docker rmi "${imagen}" >/dev/null 2>&1; then
        echo "Imagen ${imagen} ha sido borrado"
    else
        echo "No se borro la imagen ${imagen}"
    fi
done

for volumen in "${volumenes[@]}"; do
    if docker volume rm "${volumen}" >/dev/null 2>&1; then
        echo "Volumen ${volumen} ha sido eliminado"
    else
        echo "No se borro el volumen ${volumen}"
    fi
done

sudo rm -rf ./mariadb_data

docker compose build --no-cache &&
    docker compose up
