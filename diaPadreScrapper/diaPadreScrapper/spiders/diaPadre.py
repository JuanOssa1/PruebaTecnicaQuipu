import scrapy

class DiapadreSpider(scrapy.Spider):
    name = 'diaPadre'
    allowed_domains = ['listado.mercadolibre.com.co/_Deal_dia-del-padre-2022']
    start_urls = ['https://listado.mercadolibre.com.co/_Deal_dia-del-padre-2022/']

    def parse(self, response):
        nombre= response.css(".ui-search-item__title ui-search-item__group__element::text").extract()
        dataSearched = {"a"}
        #precio=
        #descuento=
        for oferta in zip(nombre):
            dataSearched = {
                'title' : oferta[0]
            }
        print("Hola")
        print(dataSearched)
        yield dataSearched
