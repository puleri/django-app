curl "http://localhost:8000/projects/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "project": {
      "name": "'"${NAME}"'",
      "completed": "'"${COMPLETED}"'",
      "priority": "'"${PRIORITY}"'",
      "deadline": "'"${DEADLINE}"'",
      "time_estimate": "'"${TIME_ESTIMATE}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
