from alba.models import Zanr
def zanrs(request):
 return {'zanrs': Zanr.objects.all()}