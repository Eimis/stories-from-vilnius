from django.db import models
from sfv import settings
from django.template.defaultfilters import slugify
from location_field.models.plain import PlainLocationField


def file(self, filename):  # nice difrectory structure for images
    url = "images/post_images/%s/%s/%s" % (self.user, self.slug, filename)
    return url


class Story(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    picture = models.ImageField(upload_to=file)
    date = models.DateTimeField(auto_now_add=True)
    # location:
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=[city], zoom=12)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):  # create url slug automatically
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = ('Stories')
