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

        for cuisine in cuisines:
            url = 'https://www.bbc.co.uk/food/search?cuisines=' + cuisine
            request = scrapy.Request(url=url, meta={'cuisine': cuisine}, callback=self.parse)
            yield request


    def parse(self, response):
        # Cuisine
        cuisine = response.meta['cuisine']
        print(f"Cuisine to scrape: {cuisine}")

        bs_obj = BeautifulSoup(response.text, 'lxml')

        # File name to be saved
        filename = f'data_scraped/quotes-{cuisine}.txt'
        textfile = open(filename, "w")
        
        print("Recipes to save: ")
        # Recipes with images
        for n in bs_obj.find_all('h3', {'class': 'promo__title gel-pica'}):
            rec_name =  n.get_text()
            print(rec_name)
            textfile.write(rec_name + "\n")

        # Recipes with no images
        for n in bs_obj.find_all('h3', {'class': 'promo__title promo__title-no-image gel-double-pica'}):
            rec_name =  n.get_text()
            print(rec_name)
            textfile.write(rec_name + "\n")

        textfile.close()
        print('File succesfully saved')

