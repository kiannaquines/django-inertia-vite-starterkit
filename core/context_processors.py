from django.conf import settings

def title(request):
    return {
        "APP_NAME": settings.APP_NAME
    }
