import scrapy

class QuerySpider(scrapy.Spider):
    name = 'queryspider'
    search_url = 'http://www.mcso.us/PAID/Home/SearchResults'
    start_urls = [search_url]

    def parse(self, response):
        data = {"SearchType": "0"}
        yield scrapy.FormRequest(
            url=self.search_url, 
            formdata=data, 
            callback=self.parse_queries
        )

    def parse_queries(self, response):
        link_paths = response.xpath("//td/a/@href").getall()
        for link in link_paths:
            booking_no = link.split('/')[4]
            page_url = f'http://www.mcso.us/PAID/Home/Booking/{booking_no}'
            return response.follow(page_url, self.parse_page)

    def parse_page(self, response):
        swis_id = response.xpath('//tbody/tr[1]/td[2]/text()').get()
        print('SWIS ID', swis_id)
