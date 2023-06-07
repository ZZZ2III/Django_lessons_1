from django.core.exceptions import PermissionDenied

class BlockedFilterIpMiddleware:

    def __init__(self, get_response):
       self.get_response = get_response

    def __call__(self, request):
        not_allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        if ip  in not_allowed_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response

