

# apt-get upgrade -- upgrade fresh installed ubuntu

==================install Mysql:
# apt-get install mysql-server -- install MySql server
# mysql_secure_installation -- Setup MySql Server
# systemctl restart mysql.service -- Restart Mysql Server
# systemctl status mysql.service -- Check Status of Mysql Server

==================mysql
# mysql -- access mysql 
# CREATE USER 'horizen'@'%' IDENTIFIED  BY 'Horizen@123'; -- create MySQL User Name and Password
# create database horizen; -- create database
# GRANT ALL PRIVILEGES ON horizen.* TO 'horizen'@'%'; -- grant permission for the user
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'; -- grant full permisson to route from remote
# FLUSH PRIVILEGES; to apply new PRIVILEGES on the server

==================nginx & SSL & Code Server
wget https://github.com/coder/code-server/releases/download/v4.98.2/code-server_4.98.2_amd64.deb
sudo dpkg -i code-server_4.98.2_amd64.deb
sudo systemctl enable --now code-server@root
nano ~/.config/code-server/config.yaml -- to set the password 

sudo nano /etc/nginx/sites-available/code-server

server {
    listen 80;
    server_name vscode.giize.com;  # Replace with your domain or server IP

    location / {
        proxy_pass http://localhost:8080; # Change this to your backend server
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

sudo ln -s /etc/nginx/sites-available/code-server /etc/nginx/sites-enabled/
nginx -t
sudo systemctl restart nginx
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your_domain_or_ip
sudo systemctl status code-server
==================== Venv 
 sudo apt install python3-venv
 python3 -m venv .venv


====================
sudo apt update
sudo apt install nodejs npm

