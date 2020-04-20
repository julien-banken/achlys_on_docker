#!/bin/bash

docker build -t my-ubuntu ./ubuntu
docker build --no-cache -t achlys .
