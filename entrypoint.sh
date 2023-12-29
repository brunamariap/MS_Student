#!/bin/bash

# Inicie o serviço do PostgreSQL
service postgresql start

# Aguarde a disponibilidade do PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Execute as migrações do Prisma
prisma migrate dev

# Inicie o servidor da aplicação
exec uvicorn main:app --host 0.0.0.0 --port 8003