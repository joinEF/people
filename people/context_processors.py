from django.conf import settings

def segment_io(request):
    return {
        'SEGMENT_IO_API_WRITE_KEY': settings.SEGMENT_IO_API_WRITE_KEY
    }