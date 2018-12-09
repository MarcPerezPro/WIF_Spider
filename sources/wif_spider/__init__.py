import scrapy
from scrapy.spiders import Rule
import logging
import re
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from sources.balance_checker import BalanceChecker


class WIFSpider(scrapy.Spider):
    name = 'WIFSpider'
    start_urls = ['http://gobittest.appspot.com/PrivateKey']

    custom_settings = {
        'COOKIES_ENABLED': False,
    }

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
                ),
            follow=True
            )
        ]

    def configure_root_logger():
        root_logger = logging.getLogger()
        logging.basicConfig(filename='logs.txt', level=logging.DEBUG)

        handler = logging.StreamHandler()
        root_logger.addHandler(handler)

        return root_logger

    root_logger = configure_root_logger()

    # Compiled WIF regex
    WIF_REGEX = re.compile("(5[HJK][1-9a-km-zA-HJ-NP-Z]{48,49})")

    balance_checker = BalanceChecker()

    def parse(self, response):
        selector = Selector(response=response)
        results = selector.re(self.WIF_REGEX)
        #self.root_logger.debug("REGEX: " + str(results))
        for wif in results:
            if self.balance_checker.is_valid(wif):
                info = self.balance_checker.get_key_info(wif)
                if info.balance > 0:
                    self.root_logger.critical("CASH: " + str(info))
                    self.root_logger.critical("URL: " + str(response.url))
                    self.root_logger.critical("BODY: " + str(response.body))

        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse)
