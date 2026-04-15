#!/bin/bash
sudo ufw default deny incoming
sudo ufw allow 45678/tcp
sudo ufw logging low
sudo ufw enable
