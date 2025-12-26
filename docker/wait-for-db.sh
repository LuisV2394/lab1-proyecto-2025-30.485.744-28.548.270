#!/bin/sh
# Espera a que MySQL esté listo antes de iniciar la API
echo "Waiting for MySQL to be ready..."
while ! nc -z db 3306; do
  sleep 1
done
echo "MySQL is up! Starting API..."
exec "$@"
