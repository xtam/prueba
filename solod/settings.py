# Scrapy settings for solod project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'solod'

SPIDER_MODULES = ['solod.spiders']
NEWSPIDER_MODULE = 'solod.spiders'
#USER_AGENT = "	Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"

DOWNLOAD_DELAY = 5 
FEED_URI = 'raw.json'
FEED_FORMAT= 'jsonlines'
DUPEFILTER_CLASS = 'scrapy.dupefilter.BaseDupeFilter'


### More comprehensive list can be found at 
### http://techpatterns.com/forums/about304.html
USER_AGENT_LIST = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7(KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10']
HTTP_PROXY = 'http://127.0.0.1:8123'

#DOWNLOADER_MIDDLEWARES = {'solod.middlewares.RandomUserAgentMiddleware': 400, 'solod.middlewares.ProxyMiddleware': 410,'solod.middlewares.redir': 450,}#'solod.middlewares.count': 460,}
#DOWNLOADER_MIDDLEWARES = {'solod.middlewares.redir': 450,'solod.middlewares.count': 460,}
# Disable compression middleware, so the actual HTML pages are cached
