import scrapy

class Spider(scrapy.Spider):

    name = 'Whisky'
    start_urls = ['https://sipwhiskey.com/collections/alcohol']

    def parse(self, response):

        for product in response.css('div.block-inner'):

            yield {

                'Title': product.css('div.title::text').get(),
                'Link' :  'https://sipwhiskey.com' + product.css('a.product-link').attrib['href'],
                'Price': product.css('span.theme-money::text').get(),
            }


        NextBtn = response.css('a.next').attrib['href']
        
        if NextBtn:
        
            yield response.follow(NextBtn, callback = self.parse)


