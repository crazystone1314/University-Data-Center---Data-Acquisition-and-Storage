# -*- coding: utf-8 -*-

import scrapy

# 字段如下：
# 城市 city
# 总价 totalprice
# 户型 housetype
# 建筑面积 conarea
# 单价 unitprice
# 朝向 direction
# 楼层 floor
# 装修 decoration
# 小区 xiaoqu
# 区域 region
# 建筑年代 architecturalage
# 有无电梯 islift
# 产权性质 propertynature
# 住宅类型 residentialtype
# 建筑建构 buildingstructure
# 建筑类别 buildingtype
# 挂牌时间 listingtime


class HousespiderItem(scrapy.Item):

    url = scrapy.Field()
    city = scrapy.Field()


class HouseItem(scrapy.Item):
    detailinfo_url = scrapy.Field()
    city = scrapy.Field()


class DetailInfoItem(scrapy.Item):
    city = scrapy.Field()
    totalprice = scrapy.Field()
    housetype = scrapy.Field()
    conarea = scrapy.Field()
    unitprice = scrapy.Field()
    direction = scrapy.Field()
    floor = scrapy.Field()
    decoration = scrapy.Field()
    xiaoqu = scrapy.Field()
    region = scrapy.Field()
    architecturalage = scrapy.Field()
    islift = scrapy.Field()
    propertynature = scrapy.Field()
    residentialtype = scrapy.Field()
    buildingstructure = scrapy.Field()
    buildingtype = scrapy.Field()
    listingtime = scrapy.Field()

