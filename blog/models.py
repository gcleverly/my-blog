import datetime
import markdown

from django.db import models
from django.utils import timezone
from django.conf import settings

def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html

#def markdown_to_html(markdownText, images):
 #   # create instance of Markdown class (note capital "M")
  #  md = markdown.Markdown()
#
 #   for image in images:
  #      image_url = settings.MEDIA_URL + image.image.url
#
 #       # append image reference to Markdown instance
  #      # md.reference[id] = (url, title)
   #     md.references[image.name] = (image_url, '')
#
 #   # parse source text
  #  return md.convert(markdownText)   

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="images" )

    def __unicode__( self ):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(default ='',max_length=255)
    subject = models.CharField(default='',max_length=255)
    body = models.TextField(default='')
    images = models.ManyToManyField( Image, blank=True)

    class Meta:
        ordering = ['-date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def body_html( self ):
        return markdown_to_html( self.body, self.images.all() )