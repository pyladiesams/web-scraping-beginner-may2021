import scrapy
from bs4 import BeautifulSoup
from scrapy_workshop_pyladies.items import ScrapyWorkshopPyladiesItem


class CuisinesSpider(scrapy.Spider):
    name = 'cuisines'
    def start_requests(self):
        cuisines = ['african', 'american', 'british', 'caribbean', 'chinese', 'east_european',
                    'french', 'greek', 'indian', 'irish', 'italian', 'japanese', 'korean',
                    'mexican', 'nordic', 'north_african', 'pakistani', 'portuguese',
                    'south_american', 'spanish', 'thai_and_south-east_asian', 'turkish_and_middle_eastern']

        # # FOR TEST
        # cuisines = ['african']
        cuisines = ['african', 'korean']

        for cuisine in cuisines:
            url = 'https://www.bbc.co.uk/food/search?cuisines=' + cuisine
            request = scrapy.Request(url=url, meta={'cuisine': cuisine}, callback=self.parse)
            yield request


    def parse(self, response):
        item = ScrapyWorkshopPyladiesItem()

        # Cuisine
        item['cuisine'] = response.meta['cuisine']

        bs_obj = BeautifulSoup(response.text, 'lxml')

        # Field: name of the recipe
        item['name_recipe'] = bs_obj.find_all('h3', {'class': 'promo__title gel-pica'})


        print('item to add: ', item)
        #yield item
