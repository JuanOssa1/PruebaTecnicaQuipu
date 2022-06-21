import scrapy

class DiapadreSpider(scrapy.Spider):
    name = 'diaPadre'
    start_urls = ['https://listado.mercadolibre.com.co/_Deal_dia-del-padre-2022']

    def parse(self, response):
        #products= response.xpath("//h2[@class='ui-search-item__title']").extract()
        products= response.css(".ui-search-item__title.ui-search-item__group__element::text").extract()
        prices= response.css(".price-tag-fraction::text").extract()
        

        for searched in zip(products,prices):
            searchedInfo={
                'product': searched[0],
                'price': searched[1]
            }

            yield searchedInfo