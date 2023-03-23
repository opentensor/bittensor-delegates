#!/bin/bash

JSON_INDENT=4

cat public/delegates.json | jq --indent $JSON_INDENT > checks/tmp.json
diff public/delegates.json checks/tmp.json