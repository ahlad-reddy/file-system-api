#!/bin/bash

export ROOT_DIR=./example_dir
docker-compose up -d
docker-compose exec web coverage run -m pytest
docker-compose exec web coverage report
docker-compose down