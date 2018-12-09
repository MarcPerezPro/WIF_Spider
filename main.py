#! /bin/python3
from scrapy.crawler import CrawlerProcess
from sources.wif_spider import WIFSpider
from sys import argv


def main():
    if len(argv) > 1:
        runner = CrawlerProcess()
        wif_spider = WIFSpider()
        runner.crawl(wif_spider, start_urls=argv[1:])
        runner.start()
    else:
        print("Usage: " + argv[0] + " URL(s)")
        return 1


if __name__ == "__main__":
    exit(main())
