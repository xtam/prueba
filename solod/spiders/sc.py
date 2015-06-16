from scrapy.spider import Spider
from scrapy.selector import Selector
from solod.items import SolodItem
from scrapy.http.request import Request
from scrapy.http import FormRequest
from scrapy.shell import inspect_response
import re
import time
import urllib
import os


class ScSpider(Spider):
	name = "find"
	#allowed_domains = ["http://www.soloduenosdirectos.com.ar"]
	#start_urls = ["http://google.com"]
	start_urls = ["http://checkip.dyndns.org/"]
	#start_urls = ["https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fprofile%2Fview%3FauthType%3Dname%26id%3D133841145%26authToken%3Dhpkd%26trk%3Dprof-sb-browse_map-name"]
	
	def parse(self, response):
		item = SolodItem()
		item['ip']= response.body
		print response.body
		yield item
