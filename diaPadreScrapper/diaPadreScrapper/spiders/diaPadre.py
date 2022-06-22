from email.policy import default
import scrapy

class DiapadreSpider(scrapy.Spider):
    name = 'diaPadre'
    start_urls = ['https://listado.mercadolibre.com.co/_Deal_dia-del-padre-2022']

    def parse(self, response):
        for offer in response.css('li.ui-search-layout__item'):
            discounts=offer.css(".ui-search-price__discount::text").extract()
            if len(discounts)<1:
                discounts="No tiene descuento"
            else:
                discounts=offer.css(".ui-search-price__discount::text").extract()
            yield {
                'product':offer.css(".ui-search-item__title.ui-search-item__group__element::text").extract(),
                'price':offer.css(".price-tag-fraction::text").extract(),
                'discounts':discounts
            }



