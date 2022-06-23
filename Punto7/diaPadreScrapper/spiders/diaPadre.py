from email.policy import default
import scrapy

class DiapadreSpider(scrapy.Spider):
    #Se define el nombre del spider
    name = 'diaPadre'
    #Se define el link que se usara para hacer el scraping
    start_urls = ['https://listado.mercadolibre.com.co/_Deal_dia-del-padre-2022']

    #Funcion que realizara todo el web scraping
    def parse(self, response):
        #Se especifica la clase CSS por las cuales ira pasando y sacando la iformacion, en el caso de la pagina de marcado libre es cada uno
        #de las "cajas" donde se encuentra la informacion del producto, pasara por cada una y sacara el precio, el descuento si lo tiene y el nombre
        for offer in response.css('li.ui-search-layout__item'):
            #En esta parte veficia el tamaño del resultado extraido del css, si es menor a 1 significa que no hay descuento y cuando retorne los resultados asignara que
            # no tiene descuento
            discounts=offer.css(".ui-search-price__discount::text").extract()
            if len(discounts)<1:
                discounts="No tiene descuento"
            #Si no se cumple la condicion significa que si tiene descuento y lo extrae
            else:
                discounts=offer.css(".ui-search-price__discount::text").extract()
            #Aqui se extrae el nombre del producto y los precios que cumplan con la condicion de CSS dada y se extrae la informacion
            #los descuentos se asignan aqui ya que se extrayeron previamente, luego de esto con yield se retorna informacion extraida a scrapy
            #para que la almacene y procese
            yield {
                'product':offer.css(".ui-search-item__title.ui-search-item__group__element::text").extract(),
                'price':offer.css(".ui-search-price.ui-search-price--size-medium .ui-search-price__second-line .price-tag-text-sr-only::text" ).extract(),
                'discounts':discounts
            }



