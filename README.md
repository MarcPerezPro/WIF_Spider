# WIF Spider
A [spider/web crawler](https://en.wikipedia.org/wiki/Web_crawler) that [scrapes](https://en.wikipedia.org/wiki/Web_scraping) websites to find valid (and more importantly with balance) [Bitcoin](https://bitcoin.org/en/) Wallets.

It does that by using [Regular Expression](https://en.wikipedia.org/wiki/Regular_expression) to find [Wallet Import Format (WIF)](https://en.bitcoin.it/wiki/Wallet_import_format) of private ECDSA keys.

---

### To use it, please run:
```console
pip install -r requirements.txt
./main.py URL(s)
```

**For example:**
```console
./main.py http://gobittest.appspot.com/PrivateKey
```

---

### TODO:
 - Add a way to run it with "scrapy runspider WIFSpider.py"
