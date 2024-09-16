import scrapy

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    #start_urls = ['https://www.semanticscholar.org/reader/e63f4b36b4cb675da85656201dd586c29fb6c8cd']
    
    #start_urls = ['https://www.scrapebay.com/ebooks'] #tải được pdf
    
    #start_urls = ['https://paperswithcode.com/paper/a-simple-framework-for-contrastive-learning']
    
    #start_urls = ['https://thuviensach.vn/kho-tang-truyen-co-tich-viet-nam-14229.html'] #tải được pdf
    
    
    def __init__(self, *args, **kwargs):
        super(SimpleSpider, self).__init__(*args, **kwargs)
        self.cnt = 10  # Khai báo biến cnt trong lớp để quản lý việc đếm

    def parse(self, response):
        # Lấy tất cả các phần tử chứa thông tin sách
        for book in response.css('div.reader__action-section.reader__action-section-1'):
            link = book.css('a.pdf ::attr(href)').get()
            if link:
                self.cnt += 1
                full_link = response.urljoin(link)
                yield {
                    'Title': "Title " + str(self.cnt),
                    'file_urls': [full_link],
                }
    
    
    def parse_2(self, response):
        # Lấy tất cả các phần tử chứa thông tin sách
        for book in response.css('div.card-body'):
            link = book.css('a.pdf ::attr(href)').get()
            if link:
                self.cnt += 1
                full_link = response.urljoin(link)
                yield {
                    'Title': "Title " + str(self.cnt),
                    'file_urls': [full_link],
                }
                
                
    def parse_3(self, response):
        # Lấy tất cả các phần tử chứa thông tin sách
        for book in response.css('div.col-md-12'):
            link = book.css('a.pdf ::attr(href)').get()
            if link:
                self.cnt += 1
                full_link = response.urljoin(link)
                yield {
                    'Title': "Title " + str(self.cnt),
                    'file_urls': [full_link],
                }
                
                
    def parse_4(self, response):
        # Lấy tất cả các phần tử chứa thông tin sách
        # Tìm thẻ cha theo id
        parent_div = response.css('div#primary')

        # Tìm thẻ <a> bên trong thẻ cha và lấy thuộc tính href
        for link in parent_div.css('a::attr(href)').getall():
            if link:
                self.cnt += 1
                full_link = response.urljoin(link)
                yield {
                    'Title': "Title " + str(self.cnt),
                    'file_urls': [full_link],
                }          
                
# book scrapy crawl simple -L WARN