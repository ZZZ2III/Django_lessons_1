from django.core.exceptions import PermissionDenied
import datetime
class BlockedListIpMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.seconds = 10
        self.banned_ips = []
        self.counter = 0
        self.start_time = 0
        self.k_asks = 5
        self.unban_time = 20
        self.ban_time_start = 0

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip and self.counter == 0:
            self.start_time = datetime.datetime.now()

        time_now = datetime.datetime.now()

        if ip:
            print(self.counter)
            self.counter += 1

        if time_now.second - self.start_time.second <= self.seconds and self.counter > self.k_asks:
            self.banned_ips.append(ip)
            self.ban_time_start = datetime.datetime.now()

        if self.banned_ips:
            if time_now.second - self.ban_time_start.second >= self.unban_time:
                self.counter = 0
                self.banned_ips.remove(ip)

        if ip in self.banned_ips:
            raise PermissionDenied


        response = self.get_response(request)

        return response

