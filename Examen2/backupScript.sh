#!/bin/bash

SOURCE_DIR="Directorio"
BACKUP_DIR="Directorio2"
DATETIME=$(date +%F)
BACKUP_PATH=$BACKUP_DIR/$DATETIME
LATEST_LINK=$BACKUP_DIR/$(date -d yesterday +%F)
ssh nombre@ip mkdir -p $BACKUP_PATH
rsync -av --link-dest=$LATEST_LINK $SOURCE_DIR nombre@ip:$BACKUP_PATH
