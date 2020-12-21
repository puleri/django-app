#!/bin/bash

curl "http://localhost:8000/projects/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
