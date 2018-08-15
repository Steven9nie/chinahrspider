# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ChinaHR.items import ChinahrItem


class ChinahrSpider(CrawlSpider):
    name = 'chinahr'
    allowed_domains = ['chinahr.com']
    start_urls = ['http://www.chinahr.com/sou/?orderField=relate&city=20,219&industrys=0&page=1']
    page_lx = LinkExtractor(allow=('page=(\d+)'))
    rules = (Rule(page_lx, callback='get_parse', follow=True),)
    'http://st02.chrstatic.com/themes/pcchinahr/js/industry.js'
    def start_requests(self):

        url = 'http://st02.chrstatic.com/themes/pcchinahr/js/citys.js?v=20170829'
        yield scrapy.Request(url, callback=self.get_city)

    def get_city(self, response):
        res_str = response.text
        replace_list = [(key, '%r' % key) for key in ['id', 'mark', 'name', 'en', 'l2', 'l3']]
        for p in replace_list:
            res_str = res_str.replace(p[0], p[1])

        pat = 'exports.base=(\[.*\])'
        city_list = eval(re.findall(pat, res_str)[0])

        for province in city_list:
            pid = province['id']
            for city in province['l2']:
                cid = city['id']
                url = f'http://www.chinahr.com/sou/?orderField=relate&city={pid},{cid}&industrys=0&page=1'
                yield scrapy.Request(url=url)

    def get_parse(self, response):

        job_list = response.xpath('//div[@class="resultList"]//div[@class="jobList"]')
        for job in job_list:
            url = job.xpath('./ul/li[1]/span[@class="e1"]/a/@href').extract()[0]

            yield scrapy.Request(url, callback=self.get_info)

    def get_info(self, response):

        job_name = response.xpath('//div[@class="base_info"]/div/h1//text()').extract()[1]

        job_require = response.xpath('//div[@class="job_require"]')
        job_price = job_require.xpath('./span[1]/text()').extract()[0]
        job_district = job_require.xpath('./span[2]/text()').extract()[0]
        job_property = job_require.xpath('./span[3]/text()').extract()[0]
        educat = job_require.xpath('./span[4]/text()').extract()[0]
        job_exp = job_require.xpath('./span[5]/text()').extract()[0]

        welfare = response.xpath('//div[@class="job_fit_tags"]/ul//text()').extract()
        welfare = [welfare for welfare in welfare if welfare.strip()]

        company_name = response.xpath('//div[@class="job-company jrpadding"]/h4//text()').extract()[0]
        company = response.xpath('//div[@class="job-company jrpadding"]/table/tbody//tr[not(@class)]')
        try:
            industry = ''.join(company[0].xpath('./td[2]//text()').extract()).strip()
        except:
            industry = None
        try:
            company_scale = ''.join(company[1].xpath('./td[2]//text()').extract()).strip()
        except:
            company_scale = None
        try:
            company_property = ''.join(company[2].xpath('./td[2]//text()').extract()).strip()
        except:
            company_property = None
        ability_list = response.xpath('//div[@class="job_intro_info"]//text()').extract()
        ability = ''.join([t.strip() for t in ability_list])

        item = ChinahrItem()
        item['jobName'] = job_name  # 职位名
        item['salary'] = job_price  # 薪资
        item['jobDistrict'] = job_district  # 工作地区
        item['jobProperty'] = job_property  # 工作性质
        item['educat'] = educat  # 学历要求
        item['jobExp'] = job_exp  # 工作经验
        item['welfare'] = welfare  # 就业福利
        item['companyName'] = company_name  # 企业名称
        item['industry'] = industry  # 行业
        item['companyScale'] = company_scale  # 企业规模
        item['companyProperty'] = company_property  # 企业属性
        item['ability'] = ability  # 职位要求
        yield item
