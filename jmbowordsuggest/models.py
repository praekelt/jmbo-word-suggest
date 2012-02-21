from django.db import models

class AcceptedWord(models.Model):
    word = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return self.word

class AcceptedWordCategory(models.Model):
    name = models.TextField(blank=False, null=False)
    words = models.ManyToManyField(AcceptedWord, blank=False, null=False)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.words.count())
    