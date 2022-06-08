from django.shortcuts import render
from alba.models import Album, Zanr
from django.views.generic import ListView, DetailView

class AlbumListView(ListView):
 model = Album
 context_object_name = 'albums_list'
 # Umístění a název šablony
 template_name = 'list.html'

 def get_queryset(self):
  if 'album_zanr' in self.kwargs:
   return Album.objects.filter(zanr__zanr=self.kwargs['album_zanr']).all()
  else:
   return Album.objects.all()

 def get_context_data(self, **kwargs):
  context = super().get_context_data(**kwargs)
  context['num_albums'] = len(self.get_queryset())

  if 'album_zanr' in self.kwargs:
   context['view_title'] = f"Žánr: {self.kwargs['album_zanr']}"
   context['view_head'] = f"Žánr alba: {self.kwargs['album_zanr']}"
  else:
   context['view_title'] = 'Alba'
   context['view_head'] = 'Přehled Alb'
  return context



class AlbumDetailView(DetailView):
  # Nastavení požadovaného modelu
 model = Album

 context_object_name = 'album_detail'
 # Umístění a název šablony
 template_name = 'detail.html'


def index(request):

 context = {
  'albumss': Album.objects.order_by('-datumV')[:3],
  'deset': Album.objects.order_by('-hodnoceni').all()[:10],
  'zanrs': Zanr.objects.order_by('zanr').all(),
  'num_albums': Album.objects.all().count(),
  'albums': Album.objects.order_by('-hodnoceni')[:6],
 }

 """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
 return render(request, 'index.html', context=context)
