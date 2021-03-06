import datetime
import markdown

from django.db import models
from django.utils import timezone
from django.conf import settings

def markdown_to_html( markdownText): #, images ):
    image_ref = ""

    #for image in images:
    #    image_url = settings.MEDIA_URL + image.image.url
    #    image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="images" )

    def __unicode__( self ):
        return self.name

class Project(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(default ='',max_length=255)
    subject = models.CharField(default='',max_length=255)
    thumbnail = models.ImageField(upload_to="images", default='images/question.jpg') #, null=True, blank=True, )
    body = models.TextField(default='')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        return "/projects/{}".format(self.id)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def body_html( self ):
        return markdown_to_html( self.body) # self.images.all() )