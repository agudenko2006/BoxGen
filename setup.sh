#!/bin/bash

sudo apt update
sudo apt install --yes python3 python3-pip
pip3 install aiogram

echo "Enter your Telegram Bot Api token"
read token
echo "Enter your printer's name"
read printer

echo "export TOKEN=\"$token\"">>~/.bashrc
echo "export PRINTER=\"$printer\"">>~/.bashrc

source ~/.bashrc
echo "Now you can run \"python3 bot.py\" to start the bot."
