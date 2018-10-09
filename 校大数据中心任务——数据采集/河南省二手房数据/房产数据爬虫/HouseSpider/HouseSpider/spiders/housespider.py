# -*- coding: utf-8 -*-
import scrapy
from HouseSpider.items import HousespiderItem
from HouseSpider.items import HouseItem
from HouseSpider.items import DetailInfoItem
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class HousespiderSpider(scrapy.Spider):
    name = 'housespider'
    start_url = 'http://esf.fang.com/newsecond/esfcities.aspx'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    #解析网页获取所有城市的URL
    def parse(self, response):
        node_li_s = response.css('div.letterSelt #c02 ul li.blubk')
        for li in node_li_s:
            if li.css('strong::text').extract_first() != u"河南":
                continue
            nodes = li.css('a.red')
            for node in nodes:
                item = HousespiderItem()
                item['city'] = node.css('a::text').extract_first()
                item['url'] = node.css('a::attr(href)').extract_first()
                yield scrapy.Request(url=item['url'], meta={'item':item}, callback=self.parse_house)

    #解析网页获取所有城市楼房详情网页的url
    def parse_house(self, response):
        item = response.meta['item']
        base_url = item['url']
        node_dl_s = response.css('div.houseList dl')

        if len(node_dl_s) == 0:
            print '该网页没有楼房信息！'
            return

        for dl in node_dl_s:
            house_item = HouseItem()
            house_item['city'] = item['city']
            house_url = dl.css('dt a::attr(href)').extract_first()
            if house_url is None:
                continue
            detailinfo_url = str(base_url) + str(house_url)
            house_item['detailinfo_url'] = detailinfo_url
            #print "楼房url：", detailinfo_url
            yield scrapy.Request(url=house_item['detailinfo_url'], meta={'house_item': house_item }, callback=self.parse_detailinfo)

        #next_tag_1 = response.xpath('//a[@id="PageControl1_hlk_next"]/@href')
        # if len(next_tag_1) == 1:
        #     new_url = response.xpath('//a[@id="PageControl1_hlk_next"]/@href').extract_first()
        #     next_url = str(base_url) + str(new_url)
        #     yield scrapy.Request(url=next_url, meta={'item': item}, callback=self.parse_house)

        next_tag_3 = response.xpath('//div[@class="listBox floatl"]/div[@id="list_D10_15"]/a[@id="PageControl1_hlk_next"]/@href')
        if len(next_tag_3) != 0:
            new_url = response.xpath('//div[@class="listBox floatl"]/div[@id="list_D10_15"]/a[@id="PageControl1_hlk_next"]/@href').extract_first()
            #print '--------------3', new_url
            next_url = str(base_url) + str(new_url)
            yield scrapy.Request(url=next_url, meta={'item': item}, callback=self.parse_house)


    #解析楼房详情网页，获取房屋详细信息
    def parse_detailinfo(self, response):
        #print response.xpath('//div[@class="trl-item_top"]/div[@class="trl-item price_esf  sty1"]/i/text()').extract()
        house_item = response.meta['house_item']
        detailinfo_item = DetailInfoItem()
        detailinfo_item['city'] = house_item['city']

        html = response.css('html').extract_first()
        soupDetail = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

        direction = "null"
        housetype = "null"
        huXingAndCaoXiang = soupDetail.find_all("div", attrs={"class": "trl-item1 w146"})
        if (huXingAndCaoXiang.__len__() != 0):
            for num in range(0, huXingAndCaoXiang.__len__()):
                xx = huXingAndCaoXiang[num].find_all("div", attrs={"class": "font14"})
                yy = huXingAndCaoXiang[num].find_all("div", attrs={"class": "tt"})
                if (xx.__len__() != 0):
                    if (xx[0].get_text().__contains__("朝向")):
                        direction = yy[0].get_text()
                    elif (xx[0].get_text().__contains__("户型")):
                        housetype = yy[0].get_text().strip()
        detailinfo_item['direction'] = direction
        detailinfo_item['housetype'] = housetype

        floor = "null"
        conarea = "null"
        louCengAndArea = soupDetail.find_all("div", attrs={"class": "trl-item1 w182"})
        if (louCengAndArea.__len__() != 0):
            for num in range(0, louCengAndArea.__len__()):
                xx = louCengAndArea[num].find_all("div", attrs={"class": "font14"})
                yy = louCengAndArea[num].find_all("div", attrs={"class": "tt"})
                if (xx.__len__() != 0):
                    if (xx[0].get_text().__contains__("楼层")):
                        floor = yy[0].get_text()
                    elif (xx[0].get_text().__contains__("建筑面积")):
                        area1 = yy[0].get_text()
                        area1 = re.findall(r"\d+", area1)
                        if (area1.__len__() != 0):
                            conarea = area1[0]
        detailinfo_item['floor'] = floor
        detailinfo_item['conarea'] = conarea

        unitprice = "null"
        decoration = "null"
        unitPriceAndDecorate = soupDetail.find_all("div", attrs={"class": "trl-item1 w132"})
        if (unitPriceAndDecorate.__len__() != 0):
            for num in range(0, unitPriceAndDecorate.__len__()):
                xx = unitPriceAndDecorate[num].find_all("div", attrs={"class": "font14"})
                yy = unitPriceAndDecorate[num].find_all("div", attrs={"class": "tt"})
                if (xx.__len__() != 0):
                    if (xx[0].get_text().__contains__("装修")):
                        decorate1 = yy[0].get_text()
                        if (decorate1.__contains__("暂无") == False):
                            decoration = decorate1
                    elif (xx[0].get_text().__contains__("单价")):
                        unitPrice1 = yy[0].get_text()
                        unitPrice1 = re.findall(r"\d+", unitPrice1)
                        if (area1.__len__() != 0):
                            unitprice = unitPrice1[0]
        detailinfo_item['unitprice'] = unitprice
        detailinfo_item['decoration'] = decoration

        totalprice = "null"
        total = soupDetail.find_all("div", attrs={"class": "trl-item_top"})
        if (total.__len__() != 0):
            text = total[0].get_text()
            totalPrice1 = re.findall(r"\d+", text)
            if (totalPrice1.__len__() != 0):
                totalprice = totalPrice1[0]
        detailinfo_item['totalprice'] = totalprice

        xiaoQu = "null"
        region = "null"
        xiaoQuAndRegion = soupDetail.find_all("div", attrs={"class": "trl-item2 clearfix"})
        for num in range(0, xiaoQuAndRegion.__len__()):
            leibie = xiaoQuAndRegion[num].find_all("div", attrs={"class": "lab"})
            if (leibie.__len__() != 0):
                if (leibie[0].get_text().__contains__("小")):
                    xiaoQu1 = xiaoQuAndRegion[num].find_all("a", attrs={"class": "blue"})
                    if (xiaoQu1.__len__() == 1):
                        xiaoQu = xiaoQu1[0].get_text()
                elif (leibie[0].get_text().__contains__("域")):
                    region1 = xiaoQuAndRegion[num].find_all("a")
                    if (region1.__len__() != 0):
                        region = ""
                        for num in range(0, region1.__len__()):
                            region = region + region1[num].get_text().strip() + " "
        detailinfo_item['xiaoqu'] = xiaoQu
        detailinfo_item['region'] = region

        fangYuanInfo = soupDetail.find_all("div", attrs={"class": "text-item clearfix"})
        buildAge1 = "null"
        lift1 = "null"
        chanQuan1 = "null"
        zhuzaiLeiBie1 = "null"
        buildStruct1 = "null"
        buildLeiBie1 = "null"
        guaPaiTime1 = "null"
        if (fangYuanInfo.__len__() != 0):
            for num in range(0, fangYuanInfo.__len__()):
                if (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("建筑年代")):
                    buildAge = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (buildAge.__len__() != 0):
                        buildAge = re.findall(r"\d+", buildAge[0].get_text())
                        if (buildAge.__len__() != 0):
                            buildAge1 = buildAge[0]
                elif (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("有无电梯")):
                    lift = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (lift.__len__() != 0):
                        lift1 = lift[0].get_text().strip()
                elif (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("产权性质")):
                    chanQuan = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (chanQuan.__len__() != 0):
                        chanQuan1 = chanQuan[0].get_text()
                elif (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("住宅类别")):
                    zhuzaiLeiBie = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (zhuzaiLeiBie.__len__() != 0):
                        zhuzaiLeiBie1 = zhuzaiLeiBie[0].get_text()
                elif (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("建筑结构")):
                    buildStruct = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (buildStruct.__len__() != 0):
                        buildStruct1 = buildStruct[0].get_text()
                elif (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("建筑类别")):
                    buildLeiBie = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (buildLeiBie.__len__() != 0):
                        buildLeiBie1 = buildLeiBie[0].get_text()
                elif (fangYuanInfo[num].find_all("span", attrs={"class": "lab"})[0].get_text().__contains__("挂牌时间")):
                    guaPaiTime = fangYuanInfo[num].find_all("span", attrs={"class": "rcont"})
                    if (guaPaiTime.__len__() != 0):
                        guaPaiTime1 = guaPaiTime[0].get_text()
                        guaPaiTime1 = guaPaiTime1.strip()
        detailinfo_item['architecturalage'] = buildAge1
        detailinfo_item['islift'] = lift1
        detailinfo_item['propertynature'] = chanQuan1
        detailinfo_item['residentialtype'] = zhuzaiLeiBie1
        detailinfo_item['buildingstructure'] = buildStruct1
        detailinfo_item['buildingtype'] = buildLeiBie1
        detailinfo_item['listingtime'] = guaPaiTime1

        yield detailinfo_item





