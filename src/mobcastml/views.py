from django.http import HttpResponse

def index_view(request):
    return HttpResponse('MobcastML is coming soon.')
