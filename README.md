# WIF Spider
A spider/web crawler that scrapes websites to find valid (and more importantly with balance) Bitcoin Wallets.

It does that by using Regular Expression to find [Wallet Import Format (WIF)](https://en.bitcoin.it/wiki/Wallet_import_format) of private ECDSA keys.

---

### To use it, please run:
```
pip install -r requirements.txt
./main.py
```
---

### TODO:
 - Add a way to run it with "scrapy runspider WIFSpider.py"
