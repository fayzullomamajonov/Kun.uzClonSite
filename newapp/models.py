from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Catigory(models.Model):
    catigory = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.catigory
    

class RegionModel(models.Model):
    region = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.region


class NewsType(models.Model):
    type = models.CharField(max_length=25)
    

    def __str__(self) -> str:
        return self.type


class NewsModel(models.Model):
    catigorys = models.ForeignKey(Catigory, blank=True, null=True, on_delete=models.CASCADE)
    VOTE_TYPE = (
    ('+', 'main'),
    ('-', 'second')
    )
    dolzarb = models.CharField( blank=True, null=True, max_length=25, choices=VOTE_TYPE)
    regions = models.ForeignKey(RegionModel, blank=True, null=True, on_delete=models.CASCADE)
    types = models.ForeignKey(NewsType, blank=True,null=True, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=252, blank=True, null=True)
    title = models.CharField(max_length=255)
    descriptions = RichTextField()
    short_text = RichTextField( blank=True, null=True)
    image = models.ImageField()
    audio_file = models.FileField( blank=True, null=True, upload_to='audio/')
    date = models.DateTimeField(auto_now_add=True)
    operator = models.CharField(max_length=25, blank=True, null=True)
    montajor = models.CharField(max_length=25, blank=True, null=True)
    tg_id = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    




