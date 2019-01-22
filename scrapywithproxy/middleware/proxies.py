class ProxiesMiddleware(object):
    def __init__(self, settings):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):

                request.meta['proxy'] = "http://124.12.50.43:8088"