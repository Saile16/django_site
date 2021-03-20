from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # este metodo lo usamos en los drafts
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# create a string representation
# aqui mostramos en string el titulo del post y lo que queramos
    def __str__(self):
        return self.title
        # return self.title + ' por ' + str(self.author)
