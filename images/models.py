from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)


    def __str__(self):
    	return self.title    

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  


class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos',verbose_name='Image')
    def __str__(self):
    	return 'for ' + str(self.post)