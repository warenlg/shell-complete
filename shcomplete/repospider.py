import just

from scrapy.spiders import Spider


class MySpider(Spider):
    name = "github_spider"
    allowed_domains = ["github.com"]
    with open("../repos.txt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        base = "https://raw.githubusercontent.com"
        content = response.text.encode("utf-8")
        just.write(content,  "data" + response.url[len(base):])
