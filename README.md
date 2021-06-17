# Proxy scraper and checker 
Program that utilizes ProxyScrapper/Checker python program to push
10 random proxies to the proxychains Kali program.
Recycles proxies every hour using CRON
Must be using Kali Linux or similiar distro
## Installation
  
   Use this command to install dependencies.
  ```bash
  sudo pip3 install -r requirements.txt
  sudo apt install proxychains-ng
  chmod 755 proxy_scraper_to_proxychains.py
  sudo python3 proxy_scraper_to_proxychains.py
  ```
 ## Credit: code I used to make this
  * [Proxy Scraper](https://github.com/Abigdog4/ProxyScrapper)
  * [Proxy Checker](https://github.com/byRo0t96/proxy_checker)
  * [Proxy__Scaper](https://github.com/iw4p/proxy-scraper)
 ## License
[MIT](https://choosealicense.com/licenses/mit/
