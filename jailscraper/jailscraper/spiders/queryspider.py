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
        page_links = []
        for link in link_paths:
            booking_no = link.split('/')[4]
            page_links.append(f'http://www.mcso.us/PAID/Home/Booking/{booking_no}')
        
        return response.follow_all(page_links, self.parse_page)

    def parse_page(self, response):
        def extract_by_label(query):
            return response.xpath(f'//label[contains(./text(),"{query}")]/parent::td/following-sibling::td/text()').get(default='').strip()
        
        booking =  {
            'url': response.url,
            'swis_id': extract_by_label('SWIS ID'),
            'full_name': extract_by_label('Name'),
            'age': extract_by_label('Age'),
            'gender': extract_by_label('Gender'),
            'race': extract_by_label('Race'),
            'height': extract_by_label('Height'),
            'weight': extract_by_label('Weight'),
            'hair_color': extract_by_label('Hair'),
            'eye_color': extract_by_label('Eyes'),
            'arresting_agency': extract_by_label('Arresting Agency'),
            'booking_date': extract_by_label('Booking Date'),
            'assigned_facility': extract_by_label('Assigned Facility'),
            'projected_release_date': extract_by_label('Projected Release Date')
        }

        yield booking
