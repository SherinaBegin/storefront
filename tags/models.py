from django.db import models
from django.contrib.contenttypes.models import ContentType #allows generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey #allows generic relationships
# Create your models here.

class Tag(models.Model):
   label = models.CharField(max_length=255)


class TaggedItem(models.Model):
   #what tag is applied to what object
   tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
   #makes it so that you don't need to create dependecies
   #type( product, video article)
   #id
   content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   object_id = models.PositiveIntegerField()
   content_object = GenericForeignKey()