echo 'alias goproxy="export http_proxy=http://192.168.1.11:8080"' >> ~/.bashrc
echo  "alias disproxy='unset http_proxy'" >> ~/.bashrc
echo "alias ..='cd ..'" >> ~/.bashrc
echo "alias ...='cd ../..'" >> ~/.bashrc
echo "alias pm2-start='pm2 start --name=notification npm -- run dev'" >> ~/.bashrc
echo "alias yeet='docker stop \$(docker ps -aq) && docker rm \$(docker ps -aq)'" >> ~/.bashrc
source ~/.bashrc
