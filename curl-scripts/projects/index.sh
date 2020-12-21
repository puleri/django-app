#!/bin/bash

curl "http://localhost:8000/projects/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
