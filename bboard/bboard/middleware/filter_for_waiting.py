from django.core.exceptions import PermissionDenied
import time
class FilterIpMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0
        self.barrier = 4
    def __call__(self, request):
        if request:
            self.counter += 1
            print(f'Counter = {self.counter}')

        if self.counter >= self.barrier:
            time.sleep(5)
            self.counter = 0
        response = self.get_response(request)

        return response

