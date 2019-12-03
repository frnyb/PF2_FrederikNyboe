#!/bin/bash

socat tcp-listen:8080,reuseaddr,fork exec:"./handler.sh $1"
