from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        date = self.pub_date
        return reverse('blog:detail',
                       args=[date.year, date.month, date.day, self.title])
	                                    
