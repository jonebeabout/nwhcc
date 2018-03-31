#!/bin/sh
dir1=/var/www/nwhcc.org/public_html/commons/
cd /var/www/nwhcc.org/scripts
while inotifywait -qqre modify "$dir1"; do
    python update-commons.py
done
