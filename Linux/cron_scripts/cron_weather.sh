#!/bin/bash

curl -s "api.openweathermap.org/data/2.5/weather?lat=49.988358&lon=36.232845&appid=${API_key}" \
        | jq '.' > ~/cron_result_weather.txt
