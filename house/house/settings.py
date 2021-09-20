
BOT_NAME = 'house'

SPIDER_MODULES = ['house.spiders']
NEWSPIDER_MODULE = 'house.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':401,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    }

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'

DEFAULT_REQUEST_HEADERS={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'X-JAVASCRIPT-ENABLED': 'True',
    'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

SPIDER_SETTINGS = [
    {
        'endpoint': 'cg-spider',
        'location': 'spiders.mcity',
        'spider': 'McitySpider',
    },
    {
        'endpoint': 'dmoz',
        'location': 'spiders.McitySpider',
        'spider': 'McitySpider',
        'scrapy_settings':  {
            'ITEM_PIPELINES': {
                'pipelines.AddTablePipeline': 500
            }
        }       
    }
]



SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

LOGS = True

EXPORT_JSON = True
EXPORT_CSV = True
