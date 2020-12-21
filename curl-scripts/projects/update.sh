curl "http://localhost:8000/projects/${ID}" \
  --include \
  --request PATCH \
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
