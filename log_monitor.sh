#!/bin/bash

# Intialize variables  to contain path to lop file, database name and user
LOGFILE="/var/log/app.log"
DBNAME="log_entries"
DBUSER="agb"

# Using a tail which prints the last N number of data of the given input Logfile 
# Using Grep with tail to buffer through the log file for the the words fatal or
tail -f "$LOGFILE" | grep --line-buffered -E -i 'fatal|error' | while read -r logLine; do
    log_timestamp=$(echo "$logLine" | awk  '{print $1, $2}')
    error_levels=$(echo "$logLine" | awk '{print $3}')
    log_messages=$(echo "$logLine" | awk '{$1=$2=$3=""; print $0}' | sed 's/^ *//g')

    # Inserting the values of log_timestamp, error_levels, log_messages into the Log_entries database.
    psql -w -U "$DBUSER" -d "$DBNAME" \
    -c "INSERT INTO log_entries (log_timestamp, error_levels, log_messages) VALUES ('$log_timestamp', '$error_levels', '$log_messages');"
done