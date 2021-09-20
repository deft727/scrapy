import scrapy
from selenium import webdriver
from scrapy import Selector
import re
# from scrapy.crawler import CrawlerProcess
# from scrapy.http import Request
# from multiprocessing import Process
# from scrapy.crawler import CrawlerProcess
# # from ..items import HouseItem
# # from house.house.database.database import create_db, Session
# # from house.house.database.advertisement import Advertisement
# import time


class McitySpider(scrapy.Spider):
    name = 'mcity'
    allowed_domains = ['m.city24.ee']
    myBaseUrl = ''
    start_urls = []

    custom_settings = {'FEED_URI': 'house/outputfile.json',
                       'CLOSESPIDER_TIMEOUT': 15,
                       'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

    def __init__(self, category=None, **kwargs):
        self.driver = webdriver.Firefox()
        if category is not None:
            self.myBaseUrl = category
            self.start_urls = []
            self.start_urls.append(self.myBaseUrl)
            super().__init__(**kwargs)

        # self.page_count = int(self.parse_page())



    # def start_requests(self):
    #     if self.myBaseUrl:
    #         url = self.start_urls[0] + self.myBaseUrl
    #         yield scrapy.Request(url=url, callback=self.parse)
        # print('_------------>>>>', self)
        # if url is not None:
        #     url = self.start_urls + url
        #     yield Request(url=url, callback=self.parse)
        # else:
        # x=['https://m.city24.ee/real-estate/apartments-for-rent/Tallinn-Lasnamae-linnaosa-Narva-mnt/5187674']
        # yield scrapy.Request(url=self.start_urls, callback=self.parse)

    # def parse_page(self):
    #     url = self.start_urls[0]
    #     self.driver.get(url)
    #     while True:
    #         try:
    #             next = self.driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]')
    #             if next:
    #                 next.click()
    #             selq = Selector(text=self.driver.page_source)
    #             last_page = re.findall('\d+', selq.xpath(
    #                 '//button[@class="page__number"]').extract()[-1].split()[-1])[-1]
    #             # print('__________---------->>>>>>', last_page)
    #             if last_page:
    #                 return last_page
    #             else:
    #                 return 1
    #         except:
    #             break
    #     self.driver.close()


    def parse(self,response):

        # page = self.parse_page()
        print("--------------------->>>>>>>>>> response", response.url)
        # for i in range(1, int(page)+1):
        #     # x=self.driver.get(response.url.join(f'pg={i}'))
        #     print(response.url+'/'+f'pg={i}')
        # x = ['https://m.city24.ee/real-estate/apartments-for-rent/Tallinn-Lasnamae-linnaosa-Narva-mnt/5187674']
        self.driver.get(response.url)
        # while True:
        try:
            accept = self.driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]')
            if accept:
                accept.click()

            selq = Selector(text=self.driver.page_source)
            # item = HouseItem()
            price = selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/h1/div/div[1]/text()').get().split()[0],
            image= selq.xpath('//div[@class="image-gallery-image"]/picture').get()

            item = {
            'title' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/h1/span[2]/text()').get(),
            'location' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/h1/span[3]/text()').get(),
            'room' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/li[2]/div/span[2]/text()').get(),
            'price' : re.findall('\d+',selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/h1/div/div[1]/text()').get()),
            'price_for_m' : re.findall('\d+',selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/h1/div/div[2]/text()').get()),
            'img' : image.split()[3].split('"')[1],
            'broker' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[7]/div/div[1]/div[1]/div/a/h3/text()').get(),
            'brokerType' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[7]/div/div[1]/div[1]/div/div/text()').get(),
            'brokerUrl' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[7]/div/div[1]/div[1]/div/a/@href').get(),
            'brokerPhone' : selq.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[7]/div/div[1]/div[2]/ul/li/div/a/@href').get()\
                        .split(':')[1]
            }

            self.driver.close()
            if item:
                yield item
            else:
                item = {'item':'not foud'}
                yield item

            # print("----------------->>>>>>>>>>>>> ", price)
            # # for i in title:
            # item['link'] = str(selq.xpath("//a[@class='object__location']/@href").extract()).strip()
            # item['title'] = str(selq.xpath('//h3[@class="object__address"]/text()').extract()).strip()
            # item['address'] = str(selq.xpath('//div[@class="object__area"]/text()').extract()).strip()
            # item['description'] = str(selq.xpath('//div[@class="object__slogan"]/text()').extract()).strip()
            # item['space'] = str(selq.xpath('//ul[@class="object__main-features"]/li[1]/text()').extract()).strip()
            # item['image'] = str(selq.xpath('//div[@class="object__thumb"]/img/@src').extract()).strip()
            # item['seller'] = str(selq.xpath('//button[@class="object__broker-contact--btn"]/u/text()').extract()).strip()
            # print('--------->>>..title ', title)
            # print('--------->>>..kink ', link)
            # print('--------->>>..adress ', address)
            # print('--------->>>..desc', description)
            # print('--------->>>..apce ', space)
            # print('--------->>>..img ', image)
            # print('--------->>>..sal ', saller)
            # yield item

        except:
            self.driver.close()
            item = {
                'error': 'error with url'
            }
            yield item

#         while True:
#             try:
#                 next = self.driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]')
#                 # next = self.driver.find_element_by_xpath('//div[@class ="_ado-corner-hover"]')
#                 url = 'https://m.city24.ee/en/real-estate-search/apartments-for-rent'
#
#                 next.click()
#                 # yield scrapy.Request(url, callback=self.parse2)
#                 selq = Selector(text=self.driver.page_source)
#                 # municipalitys = selq.xpath('//*[@id="root"]/div/div[5]/div/div[2]/div[2]').extract()
#                 # adds = selq.xpath('//h3[@class="object__address"]/@title').extract()
#                 adds = selq.xpath('//div[@class="results__objects"]').extract()
#                 # print('------------->>>>>>>>>>>', adds)
# #                 # municipalitys = selq.xpath('//div').extract()
# #                 # print(123, municipalitys)
# #                 yield scrapy.Request(url,adds, callback=self.parse2)
#             except:
#                 break
#         self.driver.close()








    # def get_pages(self):
    #     self.driver.get('https://city24.ee/en/list/rent/apartments?ord=default&str=2&c=EE&usp=true&fr=0')
    #     while True:
    #         try:
    #             selq = Selector(text=self.driver.page_source)
    #             get_all_pages = selq.xpath('//a[@class="page"]/@title').extract()
    #             # selq.xpath('//*[@id="id64e"]')
    #             last_page = get_all_pages[-2].split()[-1]
    #             return last_page
    #         except:
    #             break
    #     self.driver.close()
