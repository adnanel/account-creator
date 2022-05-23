#!/bin/bash

docker rm account_creator

docker build . -t account_creator

docker run --privileged --network host --name account_creator account_creator
