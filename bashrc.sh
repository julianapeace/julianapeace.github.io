echo 'alias goproxy="export http_proxy=http://192.168.1.11:8080"' >> ~/.bashrc
echo  "alias disproxy='unset http_proxy'" >> ~/.bashrc
echo "alias ..='cd ..'" >> ~/.bashrc
echo "alias ...='cd ../..'" >> ~/.bashrc
source ~/.bashrc
