#!/bin/bash

curl "http://localhost:8000/projects/${ID}/tasks/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
