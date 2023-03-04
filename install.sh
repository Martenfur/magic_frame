echo "Make sure you cloned the repository into /home/pi/magic_frame directory! Your username must be 'pi'!"
sudo timedatectl set-ntp true

sudo cp magic_frame.service /etc/systemd/system/magic_frame.service
sudo systemctl daemon-reload
sudo systemctl enable magic_frame.service
sudo systemctl start magic_frame.service

echo "DONE!"