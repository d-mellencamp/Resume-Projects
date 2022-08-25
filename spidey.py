import scrapy
from ..items import PeterItem


class Book_Spider(scrapy.Spider):
    name = "spidey"

    start_urls = ["https://www.barnesandnoble.com/",
                  "https://www.amazon.com/s?k=laptops",
                  "https://www.macrotrends.net/stocks/charts/WMT/walmart/stock-price-history"]

    def parse(self, response):
        product = PeterItem()
        for year in response.css(".ic-rt , thead~ thead+ tbody td:nth-child(1)::text").extract():
            yield {'year': year}
        for avg_price in response.css("thead~ thead+ tbody td:nth-child(2)::text").extract():
            yield {"avg_price": avg_price}

