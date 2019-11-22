#!/usr/bin/zsh
train_number=50
index=0
while [ "$index" -lt "$train_number" ]
do
  index=$((index+1))
  /home/gabyf/.virtualenvs/openai/bin/python /home/gabyf/projects/openai/sarsa_taxi_driver.py
done
