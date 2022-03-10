#!/bin/bash

sudo apt update
sudo apt install --yes python3 python3-pip cron cups
pip3 install aiogram

sudo usermod -aG $USER lp
sudo usermod -aG $USER lpprint
sudo systemctl restart cups

sudo cp .cupsd.conf /etc/cups/cupsd.conf
clear
echo "Open $HOSTNAME:631 on another computer, set your printer up and press RETURN"
read >> /dev/null
echo "Enter your printer's name"
read printer

echo "Enter your Telegram Bot Api token"
read token

echo "export TOKEN=\"$token\"">>~/.bashrc
echo "export PRINTER=\"$printer\"">>~/.bashrc

export TOKEN=\"$token\"
export PRINTER=\"$printer\"

sudo apt install --yes inkscape
clear
echo "Now you can run \"python3 bot.py\" to start the bot."
