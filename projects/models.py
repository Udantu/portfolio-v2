from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200)
    file = models.TextField(default="")
    tag = models.TextField(default="")
    srcType = models.TextField(default="URL")

    def __str__(self):
        return f'{self.title}'

    def tags_as_list(self):
        return self.tag.split(',')
