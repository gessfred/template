#!/bin/sh
serve -s /app/dist -l "tcp://0.0.0.0:$HTTP_PORT"