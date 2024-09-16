from scrapy.pipelines.files import FilesPipeline


class CustomFilePipelines(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        #print(item.get('file_urls'))
        return item.get('Title')+'.pdf'
        #return item.get('file_urls')
