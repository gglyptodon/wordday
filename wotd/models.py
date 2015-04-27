from django.db import models

# Create your models here.

from django.db import models
# Create your models here.

class Word(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    example = models.TextField(default="")
    description = models.TextField(default="")
    dateShown = models.DateField()

    def whenShown(self):
        return self.dateShown

    def __repr__(self):
        return "{}({}): {}".format(self.title, self.language, self.description)