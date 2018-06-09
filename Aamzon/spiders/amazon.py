# -*- coding: utf-8 -*-
import scrapy

from Aamzon.items import AamzonBabyItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/gp/global-store/ranking']

    def parse(self, response):
        with open("index.html", "w") as f:
            f.write(response.body)
        baby_node_list = response.xpath("//*[@id='anonCarousel1']")
        print baby_node_list
        # print response.body
        for node in baby_node_list:
            item=AamzonBabyItem()
            item['goods_name']=node.xpath('./div[2]/div[2]/a/text()').extract_first()
            item['goods_price']=node.xpath('./div[4]/span[2]/text()').extract_first()
            item['goods_link']=node.xpath('./div[2]/div[2]/a/@href').extract_first()
            yield item

