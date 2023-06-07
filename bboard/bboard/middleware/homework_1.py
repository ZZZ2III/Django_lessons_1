import datetime
class HomeworK_middleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        ip = request.META.get('REMOTE_ADDR')
        time = datetime.datetime.now()
        url_for_logger = request.META.get('HTTP_REFERER')
        method = request.META.get('REQUEST_METHOD')
        str_1 =f'ip: {ip}\ntime = {time}\nURL: {url_for_logger} \nmethod: {method}\n'
        with open('logger.txt','a') as log:
           log.writelines(str_1)

        response = self.get_response(request)

        return response
