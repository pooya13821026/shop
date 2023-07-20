from django.http import HttpRequest


def get_user_ip(request: HttpRequest):
    forwarded_for = request.META.get('HTTP_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
