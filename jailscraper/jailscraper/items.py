# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from dataclasses import dataclass

@dataclass
class BookingPage:
    url : str
    swis_id : str
    full_name : str
    age : str
    gender : str
    race : str
    height : str
    weight : str
    hair_color : str
    eye_color : str
    arresting_agency : str
    booking_date : str
    assigned_facility : str
    projected_release_date : str

    pass

# class JailscraperItem(scrapy.Item):
#     url = scrapy.Field(),
#     swis_id = scrapy.Field(),
#     full_name = scrapy.Field(),
#     age = scrapy.Field(),
#     gender = scrapy.Field(),
#     race = scrapy.Field(),
#     height = scrapy.Field(),
#     weight = scrapy.Field(),
#     hair_color = scrapy.Field(),
#     eye_color = scrapy.Field(),
#     arresting_agency = scrapy.Field(),
#     booking_date = scrapy.Field(),
#     assigned_facility = scrapy.Field(),
#     projected_release_date = scrapy.Field()
    
#     pass
