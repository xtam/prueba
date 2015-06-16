import os
import random
import time
from scrapy.conf import settings
import re
from urllib import unquote

counter = 1
random_1 = random.randint(9,15)
random_2 = random.randint(45,60)
random_3 = random.randint(500,550)

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')
        
class redir(object):
    def process_response(self, request, response, spider):
		#print response.url
		#print request.url
		#raw_input()
		if "uas" or "join" in response.url:
			print ":( Linked Session redirect"
			print response.url
			#new_url = unquote(re.sub("^https.*?=","",response.url))
			new_url = unquote(re.sub("https.*?=.*?=","",response.url))
			new_req = request.replace(url = new_url)
			print "es la new"
			print new_req.url
			raw_input()
			return new_req
		else:
			return response
		if "sorry" in response.url:
			print ":( Google Sorry"
			print response.url
			new_url = re.sub("ipv4.google.com.sorry.IndexRedirect.continue.","",response.url)
			new_req = request.replace(url = new_url)
			print "es la new"
			print new_req
			raw_input()
			return new_req
		else:
			return response
		

class count(object):
    def process_response(self, request,response, spider):
		global counter, random_1, random_2, random_3
		print counter
		if counter % random_1 == 0:
			print "Esta esperando"
			print random_1
			time.sleep(random.randint(60,90))
			random_1 = random.randint(9,15)
		if counter % random_2 == 0:
			print "Paaraaaa un poco..ya van:"
			print random_2
			time.sleep(random.randint(300,500))
			random_2 = random.randint(45,60)
		if counter % random_3 == 0:
			print "Paaraaaa un poco..ya van 50:"
			time.sleep(random.randint(300,500))
			random_3 = random.randint(200,250)
		counter = counter + 1
		return response
