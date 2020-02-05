#!/bin/sh

IFS=';' read -ra NAMES <<< "$BACKUPDB_NAMES"

wget https://raw.githubusercontent.com/deekshahegde86/postgresql-operator-phases-1-2-3/master/scripts/restore/pull-db-backup.py

for i in "${NAMES[@]}"; do
   export BACKUP_FILE=$i;
   python pull-db-backup.py
   export FILE=${i%%-*}
   cat databackup.sql | PGPASSWORD=$POSTGRES_PASSWORD psql -h $SERVICE_IP -U $POSTGRES_USER -d $FILE
   rm -rf databackup.sql
done
rm -rf pull-db-backup.py
