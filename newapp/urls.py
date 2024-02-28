from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView, name='home'),
    path('category/uzbekiston/', UzNewView, name='uzbekiston'),
    path('category/jahon/', JaNewView, name='jahon'),
    path('category/iqtisodiyot/', IqNewView, name='iqtisodiyot'),
    path('category/jamiyat/', JamNewView, name='jamiyat'),
    path('category/fan_tex/', FanNewView, name='fan_tex'),
    path('category/sport/', SpNewView, name='sport'),
    path('category/nuqtayi_nazar/', NuNewView, name='nuqtayi_nazar'),
    path('category/audio/', AuNewView, name='audio'),
    path('news/<int:pk>/', News, name='news'),
    path('news/list/', NewListView, name='news_list'),
    path('news/main/', NewListMainView, name='news_list_main'),
    path('editor/news', NewEditorChoice, name='muharrir_tanlovi'),
    path('interviews/', NewInterviewsView, name='interview'),
    path('articles/', NewArliclesView, name='maqolalar'),
    path('video/news', NewVideosView, name='video_news'),
    path('foto/news', NewFotosView, name='foto_news'),
    path('biznes/', BiznesView, name='biznes'),
    path('region/toshkent/',RegionToshkent,name='toshkent'),
    path('region/qoraqalpoq/',RegionQoraqalpoq,name='qoraqalpoq'),
    path('region/andijon/',RegionAndijon,name='andijon'),
    path('region/fargona/',RegionFargona,name='fargona'),
    path('region/namangan/',RegionNamangan,name='namangan'),
    path('region/samarqand/',RegionSamarqand,name='samarqand'),
    path('region/buxoro/',RegionBuxoro,name='buxoro'),
    path('region/xorazm/',RegionXorazm,name='xorazm'),
    path('region/surxondaryo/',RegionSurxondaryo,name='surxondaryo'),
    path('region/qashqadaryo/',RegionQashqadaryo,name='qashqadaryo'),
    path('region/jizzax/',RegionJizzax,name='jizzax'),
    path('region/sirdaryo/',RegionSirdaryo,name='sirdaryo'),
    path('region/toshkent-vil/',RegionToshkentVil,name='toshkentvil'),
    path('region/navoiy/',RegionNavoiy,name='navoiy'),


]
