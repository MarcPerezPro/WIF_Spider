#! /bin/python3
from scrapy.crawler import CrawlerProcess
from sources.wif_spider import WIFSpider


def main():
    runner = CrawlerProcess()
    runner.crawl(WIFSpider)
    runner.start()

if __name__ == "__main__":
    main()
