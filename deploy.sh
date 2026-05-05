#!/bin/bash
set -e
cd /home/romain/run/saas-ui-patterns
git fetch origin
git reset --hard origin/deploy
docker compose up --build -d
