#!/bin/bash

docker build \
  --build-arg MANGA_URL \
  --build-arg CHAPTER_NUMBER \
  --build-arg NOTIFICATION_FROM_EMAIL \
  --build-arg NOTIFICATION_TO_EMAIL \
  --build-arg SMTP_SERVER \
  --build-arg SMTP_PORT \
  --build-arg SMTP_USERNAME \
  --build-arg SMTP_PASSWORD \
  -t myapp .