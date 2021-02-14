import scrapy

class QuerySpider(scrapy.Spider):
    name = 'queryspider'
    search_url = 'http://www.mcso.us/PAID/Home/SearchResults'
    start_urls = [search_url]

    def parse(self, response):
        data = {"SearchType": "0"}
        yield scrapy.FormRequest(url=self.search_url, formdata=data, callback=self.parse_queries)

    def parse_queries(self, response):
        rows = response.xpath('//table/tbody/tr')
        bookingnos = rows.xpath("td/a/@href").extract()
        print('Booking Numbers', bookingnos)
        
