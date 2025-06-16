#!/usr/bin/env bash
# Build the Docker image for Baseline Awareness Service

docker build -f docker/Dockerfile -t baseline-awareness:latest .
