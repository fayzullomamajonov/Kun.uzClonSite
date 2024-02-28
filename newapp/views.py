from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Catigory, NewsModel



# import datetime

# Create your views here.


def HomePageView(request):
    cotigorys = Catigory.objects.all()
    # new blog 1
    type_news = NewsModel.objects.filter(types__type='Siyosiy').order_by('-date')
    main_new = type_news[0]
    second_new = type_news[1:5]
    # new blog 2
    muharrir_new = NewsModel.objects.filter(types__type='Muharrir tanlovi').order_by('-date')
    muharrir_news = muharrir_new[:3]
    # new blog 3
    dolzarb_new = NewsModel.objects.filter(types__type='Dolzarb Xabarlar').order_by('-date')
    dolzarb_main_new = dolzarb_new[0]
    dolzarb_second_new = dolzarb_new[1:5]
    # new blog 4
    intervyu_new = NewsModel.objects.filter(types__type='Intervyu').order_by('-date')
    intervtu_news = intervyu_new[:4]
    # new blog 5
    tadbir_new = NewsModel.objects.filter(types__type='Muhun Tadbirlar').order_by('-date')
    tadbir_main_new = tadbir_new[0]
    tadbir_second_new = tadbir_new[1:5]
    # new blog 6
    maqola_new = NewsModel.objects.filter(types__type='Maqolalar').order_by('-date')
    maqola_news = maqola_new[:6]
    # new blog 7
    biznes_new = NewsModel.objects.filter(types__type='Biznes').order_by('-date')
    biznes_news = biznes_new[:15]
    # new blog 8
    video_new = NewsModel.objects.filter(types__type='Video yangiliklar').order_by('-date')
    video_main_new = video_new[0]
    video_second_new = video_new[1:3]
    # new blog 9
    photo_new = NewsModel.objects.filter(types__type='Fotoyangiliklar').order_by('-date')
    photo_main_new = photo_new[0]
    photo_second_new = photo_new[1:3]

    today_news = NewsModel.objects.order_by('-date')[:8]
    # current_week = datetime.date.today().isocalendar()[1]

    context = {
        'cotigorys': cotigorys,

        'main_new': main_new,
        'second_new': second_new,

        'today_news': today_news,

        'muharrir_news': muharrir_news,

        'dolzarb_main_new': dolzarb_main_new,
        'dolzarb_second_new': dolzarb_second_new,

        'intervtu_news': intervtu_news,

        'tadbir_main_new': tadbir_main_new,
        'tadbir_second_new': tadbir_second_new,

        'maqola_news': maqola_news,

        'biznes_news': biznes_news,

        'video_main_new': video_main_new,
        'video_second_new': video_second_new,

        'photo_main_new': photo_main_new,
        'photo_second_new': photo_second_new,

    }
    return render(request, "home.html", context)


#   catigory uzbekistan 
def UzNewView(request):
    catigorys = NewsModel.objects.filter(catigorys__catigory="O`zbekiston").order_by('-date')
    today_news = NewsModel.objects.order_by('-date')[:8]

    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 10)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'uzbekiston.html', context)


# catigory jahon
def JaNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    catigorys = NewsModel.objects.filter(catigorys__catigory="Jahon").order_by()
    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 10)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'jahon.html', context)


# catigory Iqtisodiyot
def IqNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    catigorys = NewsModel.objects.filter(catigorys__catigory="Iqtisodiyot").order_by()
    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 12)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'iqtisodiyot.html', context)


# catigory Jamiyat
def JamNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    catigorys = NewsModel.objects.filter(catigorys__catigory="Jamiyat").order_by()
    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 12)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'jamiyat.html', context)


# catigory Fan-Texnika
def FanNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    catigorys = NewsModel.objects.filter(catigorys__catigory="Fan-Texnika").order_by()
    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 12)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'fan_tex.html', context)


# catigory Sport
def SpNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    catigorys = NewsModel.objects.filter(catigorys__catigory="Sport").order_by()
    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 12)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'sport.html', context)


# catigory Nuqtayi Nazar
def NuNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    catigorys = NewsModel.objects.filter(catigorys__catigory="NuqtayiNazar").order_by()
    cat_main_new = catigorys.filter(dolzarb='+').order_by('-date')[0]
    cat_second_new = catigorys.filter(dolzarb='+').order_by('-date')[1:5]
    cat_all_new = catigorys

    paginator = Paginator(cat_all_new, 12)

    page = request.GET.get('page')
    cat_all_new = paginator.get_page(page)

    context = {
        'cat_main_new': cat_main_new,
        'cat_second_new': cat_second_new,
        'cat_all_new': cat_all_new,
        'today_news': today_news,
    }
    return render(request, 'nuqtayi_nazar.html', context)


# catigory Audio
def AuNewView(request):
    today_news = NewsModel.objects.order_by('-date')[:8]
    audio_news = NewsModel.objects.filter(catigorys__catigory="Audio").order_by('-date')
    paginator = Paginator(audio_news, 10)

    page = request.GET.get('page')
    audio_news = paginator.get_page(page)

    context = {
        'audio_news': audio_news,
        'today_news': today_news,
    }
    return render(request, 'audio.html', context)


def News(request, pk):
    biznes_news = NewsModel.objects.filter(types__type='Biznes').order_by('-date')
    news = NewsModel.objects.get(id=pk)
    related_news = NewsModel.objects.filter(catigorys=news.catigorys).exclude(id=pk).order_by('-date')[:4]
    today_news = NewsModel.objects.order_by('-date')[:8]
    news_titles = NewsModel.objects.filter(news_title = news.news_title).exclude(id=pk).order_by('-date')[0]
    context = {
        'news': news,
        'today_news':today_news,
        'related_news':related_news,
        'news_titles':news_titles,
        'biznes_news':biznes_news,
    }
    return render(request,'news.html', context)

def NewListView(request):
    news_list = NewsModel.objects.all().order_by('-date')
    paginator = Paginator(news_list, 10)

    page = request.GET.get('page')
    news_list = paginator.get_page(page)

    context = {
        'news_list':news_list,
    }
    return render(request,'news_list.html',context)


def NewListMainView(request):
    news_list_main = NewsModel.objects.filter(dolzarb = '+').order_by('-date')
    paginator = Paginator(news_list_main, 10)

    page = request.GET.get('page')
    news_list_main = paginator.get_page(page)
    context = {
        'news_list_main':news_list_main,
    }
    return render(request,'news_list_main.html',context)

def NewEditorChoice(request):
    editor_news = NewsModel.objects.filter(types__type='Muharrir tanlovi').order_by('-date')
    paginator = Paginator(editor_news, 10)

    page = request.GET.get('page')
    editor_news = paginator.get_page(page)
    context = {
       'editor_news': editor_news, 
    }
    return render(request,'muharrir_tanlovi.html',context)

def NewInterviewsView(request):
    interview_news = NewsModel.objects.filter(types__type='Intervyu').order_by('-date')
    paginator = Paginator(interview_news, 10)

    page = request.GET.get('page')
    interview_news = paginator.get_page(page)
    context = {
       'interview_news': interview_news, 
    }
    return render(request,'interview.html',context)

def NewArliclesView(request):
    articles = NewsModel.objects.filter(types__type='Maqolalar').order_by('-date')
    paginator = Paginator(articles, 10)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
       'articles': articles, 
    }
    return render(request,'maqolalar.html',context)

def NewVideosView(request):
    videos = NewsModel.objects.filter(types__type='Video yangiliklar').order_by('-date')
    paginator = Paginator(videos, 10)

    page = request.GET.get('page')
    videos = paginator.get_page(page)
    context = {
       'videos': videos, 
    }
    return render(request,'video_news.html',context)

def NewFotosView(request):
    fotos = NewsModel.objects.filter(types__type='Fotoyangiliklar').order_by('-date')
    paginator = Paginator(fotos, 10)

    page = request.GET.get('page')
    fotos = paginator.get_page(page)
    context = {
       'fotos': fotos, 
    }
    return render(request,'foto_news.html',context)

def BiznesView(request):
    return render(request, 'biznes.html')


def RegionToshkent(request):
    toshkent_top = NewsModel.objects.filter(regions__region='Toshkent', dolzarb = '+').order_by('-date')[:1]
    toshkent = NewsModel.objects.filter(regions__region='Toshkent').order_by('-date')[1:4]
    toshkent_list = NewsModel.objects.filter(regions__region='Toshkent').order_by('-date')[4:]
    now_in_toshkent = NewsModel.objects.filter(regions__region='Toshkent', dolzarb = '-').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(toshkent_list, 10)

    page = request.GET.get('page')
    toshkent_list = paginator.get_page(page)
    context = {
        'toshkent_top':toshkent_top,
        'toshkent':toshkent,
        'toshkent_list':toshkent_list,
        'now_in_toshkent':now_in_toshkent,
        'today_new':today_new,
    }
    return render(request,'regions/toshkent.html',context)


def RegionQoraqalpoq(request):
    qoraqalpoq_top = NewsModel.objects.filter(regions__region='Qoraqalpog`iston', dolzarb = '+').order_by('-date')[:1]
    qoraqalpoq = NewsModel.objects.filter(regions__region='Qoraqalpog`iston').order_by('-date')[1:4]
    qoraqalpoq_list = NewsModel.objects.filter(regions__region='Qoraqalpog`iston').order_by('-date')[4:]
    now_in_qoraqalpoq = NewsModel.objects.filter(regions__region='Qoraqalpog`iston').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(qoraqalpoq_list, 10)

    page = request.GET.get('page')
    qoraqalpoq_list = paginator.get_page(page)
    context = {
        'qoraqalpoq_top':qoraqalpoq_top,
        'qoraqalpoq':qoraqalpoq,
        'qoraqalpoq_list':qoraqalpoq_list,
        'now_in_qoraqalpoq':now_in_qoraqalpoq,
        'today_new':today_new,
    }
    return render(request,'regions/qoraqalpoq.html',context)

def RegionAndijon(request):
    andijon_top = NewsModel.objects.filter(regions__region='Andijon', dolzarb = '+').order_by('-date')[:1]
    andijon = NewsModel.objects.filter(regions__region='Andijon').order_by('-date')[1:4]
    andijon_list = NewsModel.objects.filter(regions__region='Andijon').order_by('-date')[4:]
    now_in_andijon = NewsModel.objects.filter(regions__region='Andijon').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(andijon_list, 10)

    page = request.GET.get('page')
    andijon_list = paginator.get_page(page)
    context = {
        'andijon_top':andijon_top,
        'andijon':andijon,
        'andijon_list':andijon_list,
        'now_in_andijon':now_in_andijon,
        'today_new':today_new,
    }
    return render(request,'regions/andijon.html',context)

def RegionFargona(request):
    fargona_top = NewsModel.objects.filter(regions__region='Fargo`na', dolzarb = '+').order_by('-date')[:1]
    fargona = NewsModel.objects.filter(regions__region='Farg`ona').order_by('-date')[1:4]
    fargona_list = NewsModel.objects.filter(regions__region='Farg`ona').order_by('-date')[4:]
    now_in_fargona = NewsModel.objects.filter(regions__region='Farg`ona').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(fargona_list, 10)

    page = request.GET.get('page')
    fargona_list = paginator.get_page(page)
    context = {
        'fargona_top':fargona_top,
        'fargona':fargona,
        'fargona':fargona_list,
        'now_in_fargona':now_in_fargona,
        'today_new':today_new,
    }
    return render(request,'regions/fargona.html',context)

def RegionNamangan(request):
    namangan_top = NewsModel.objects.filter(regions__region='Namangan', dolzarb = '+').order_by('-date')[:1]
    namangan = NewsModel.objects.filter(regions__region='Namangan').order_by('-date')[1:4]
    namangan_list = NewsModel.objects.filter(regions__region='Namangan').order_by('-date')[4:]
    now_in_namangan = NewsModel.objects.filter(regions__region='Namangan').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(namangan_list, 10)

    page = request.GET.get('page')
    namangan_list = paginator.get_page(page)
    context = {
        'namangan_top':namangan_top,
        'namangan':namangan,
        'namangan_list':namangan_list,
        'now_in_namangan':now_in_namangan,
        'today_new':today_new,
    }
    return render(request,'regions/namangan.html',context)

def RegionSamarqand(request):
    samarqand_top = NewsModel.objects.filter(regions__region='Samarqand', dolzarb = '+').order_by('-date')[:1]
    samarqand = NewsModel.objects.filter(regions__region='Samarqand').order_by('-date')[1:4]
    samarqand_list = NewsModel.objects.filter(regions__region='Samarqand').order_by('-date')[4:]
    now_in_samarqand = NewsModel.objects.filter(regions__region='Samarqand').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(samarqand_list, 10)

    page = request.GET.get('page')
    samarqand_list = paginator.get_page(page)
    context = {
        'samarqand_top':samarqand_top,
        'samarqand':samarqand,
        'samarqand_list':samarqand_list,
        'now_in_samarqand':now_in_samarqand,
        'today_new':today_new,
    }
    return render(request,'regions/samarqand.html',context)

def RegionBuxoro(request):
    buxoro_top = NewsModel.objects.filter(regions__region='Buxoro', dolzarb = '+').order_by('-date')[:1]
    buxoro = NewsModel.objects.filter(regions__region='Buxoro').order_by('-date')[1:4]
    buxoro_list = NewsModel.objects.filter(regions__region='Buxoro').order_by('-date')[4:]
    now_in_buxoro = NewsModel.objects.filter(regions__region='Buxoro').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(buxoro_list, 10)

    page = request.GET.get('page')
    buxoro_list = paginator.get_page(page)
    context = {
        'buxoro_top':buxoro_top,
        'buxoro':buxoro,
        'buxoro_list':buxoro_list,
        'now_in_buxoro':now_in_buxoro,
        'today_new':today_new,
    }
    return render(request,'regions/buxoro.html',context)

def RegionXorazm(request):
    xorazm_top = NewsModel.objects.filter(regions__region='Xorazm', dolzarb = '+').order_by('-date')[:1]
    xorazm = NewsModel.objects.filter(regions__region='Xorazm').order_by('-date')[1:4]
    xorazm_list = NewsModel.objects.filter(regions__region='Xorazm').order_by('-date')[4:]
    now_in_xorazm = NewsModel.objects.filter(regions__region='Xorazm').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(xorazm_list, 10)

    page = request.GET.get('page')
    xorazm_list = paginator.get_page(page)
    context = {
        'xorazm_top':xorazm_top,
        'xorazm':xorazm,
        'xorazm_list':xorazm_list,
        'now_in_xorazm':now_in_xorazm,
        'today_new':today_new,
    }
    return render(request,'regions/xorazm.html',context)

def RegionSurxondaryo(request):
    surxondaryo_top = NewsModel.objects.filter(regions__region='Xorazm', dolzarb = '+').order_by('-date')[:1]
    surxondaryo = NewsModel.objects.filter(regions__region='Xorazm').order_by('-date')[1:4]
    surxondaryo_list = NewsModel.objects.filter(regions__region='Xorazm').order_by('-date')[4:]
    now_in_surxondaryo = NewsModel.objects.filter(regions__region='Xorazm').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(surxondaryo_list, 10)

    page = request.GET.get('page')
    surxondaryo_list = paginator.get_page(page)
    context = {
        'surxondaryo_top':surxondaryo_top,
        'surxondaryo':surxondaryo,
        'surxondaryo_list':surxondaryo_list,
        'now_in_surxondaryo':now_in_surxondaryo,
        'today_new':today_new,
    }
    return render(request,'regions/surxondaryo.html',context)

def RegionQashqadaryo(request):
    qashqadaryo_top = NewsModel.objects.filter(regions__region='Qashqadaryo', dolzarb = '+').order_by('-date')[:1]
    qashqadaryo = NewsModel.objects.filter(regions__region='Qashqadaryo').order_by('-date')[1:4]
    qashqadaryo_list = NewsModel.objects.filter(regions__region='Qashqadaryo').order_by('-date')[4:]
    now_in_qashqadaryo = NewsModel.objects.filter(regions__region='Qashqadaryo').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(qashqadaryo_list, 10)

    page = request.GET.get('page')
    qashqadaryo_list = paginator.get_page(page)
    context = {
        'qashqadaryo_top':qashqadaryo_top,
        'qashqadaryo':qashqadaryo,
        'qashqadaryo_list':qashqadaryo_list,
        'now_in_qashqadaryo':now_in_qashqadaryo,
        'today_new':today_new,
    }
    return render(request,'regions/qashqadaryo.html',context)

def RegionJizzax(request):
    jizzax_top = NewsModel.objects.filter(regions__region='Jizzax', dolzarb = '+').order_by('-date')[:1]
    jizzax = NewsModel.objects.filter(regions__region='Jizzax').order_by('-date')[1:4]
    jizzax_list = NewsModel.objects.filter(regions__region='Jizzax').order_by('-date')[4:]
    now_in_jizzax = NewsModel.objects.filter(regions__region='Jizzax').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(jizzax_list, 10)

    page = request.GET.get('page')
    jizzax_list = paginator.get_page(page)
    context = {
        'jizzax_top':jizzax_top,
        'jizzax':jizzax,
        'jizzax_list':jizzax_list,
        'now_in_jizzax':now_in_jizzax,
        'today_new':today_new,
    }
    return render(request,'regions/jizzax.html',context)

def RegionSirdaryo(request):
    sirdaryo_top = NewsModel.objects.filter(regions__region='Sirdaryo', dolzarb = '+').order_by('-date')[:1]
    sirdaryo = NewsModel.objects.filter(regions__region='Sirdaryo').order_by('-date')[1:4]
    sirdaryo_list = NewsModel.objects.filter(regions__region='Sirdaryo').order_by('-date')[4:]
    now_in_sirdaryo = NewsModel.objects.filter(regions__region='Sirdaryo').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(sirdaryo_list, 10)

    page = request.GET.get('page')
    sirdaryo_list = paginator.get_page(page)
    context = {
        'sirdaryo_top':sirdaryo_top,
        'sirdaryo':sirdaryo,
        'sirdaryo_list':sirdaryo_list,
        'now_in_sirdaryo':now_in_sirdaryo,
        'today_new':today_new,
    }
    return render(request,'regions/sirdaryo.html',context)

def RegionToshkentVil(request):
    toshkentvil_top = NewsModel.objects.filter(regions__region='Toshkent viloyati', dolzarb = '+').order_by('-date')[:1]
    toshkentvil = NewsModel.objects.filter(regions__region='Toshkent viloyati').order_by('-date')[1:4]
    toshkentvil_list = NewsModel.objects.filter(regions__region='Toshkent viloyati').order_by('-date')[4:]
    now_in_toshkentvil = NewsModel.objects.filter(regions__region='Toshkent viloyati', dolzarb = '-').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(toshkentvil_list, 10)

    page = request.GET.get('page')
    toshkentvil_list = paginator.get_page(page)
    context = {
        'toshkentvil_top':toshkentvil_top,
        'toshkentvil':toshkentvil,
        'toshkentvil_list':toshkentvil_list,
        'now_in_toshkentvil':now_in_toshkentvil,
        'today_new':today_new,
    }
    return render(request,'regions/toshkentvil.html',context)

def RegionNavoiy(request):
    navoiy_top = NewsModel.objects.filter(regions__region='Toshkent viloyati', dolzarb = '+').order_by('-date')[:1]
    navoiy = NewsModel.objects.filter(regions__region='Toshkent viloyati').order_by('-date')[1:4]
    navoiy_list = NewsModel.objects.filter(regions__region='Toshkent viloyati').order_by('-date')[4:]
    now_in_navoiy = NewsModel.objects.filter(regions__region='Toshkent viloyati', dolzarb = '-').order_by('-date')[:1]
    today_new = NewsModel.objects.order_by('-date')[:8]
    paginator = Paginator(navoiy_list, 10)

    page = request.GET.get('page')
    navoiy_list = paginator.get_page(page)
    context = {
        'navoiy_top':navoiy_top,
        'navoiy':navoiy,
        'navoiy_list':navoiy_list,
        'now_in_navoiy':now_in_navoiy,
        'today_new':today_new,
    }
    return render(request,'regions/navoiy.html',context)