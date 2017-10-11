# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Event(models.Model):

  ENTER = 'E'
  LEAVE = 'L'
  OTHER = 'O'

  EVENTS_CHOICES = ((ENTER, 'Zutritt'),( LEAVE, 'Ausgang'),( OTHER, 'sonstige'))
  
  datum =  models.DateTimeField()
  eingangswert = models.IntegerField(default=0)
  ausgangswert = models.IntegerField(default=0)
  mensch = models.CharField(max_length=1, choices=EVENTS_CHOICES, blank=True)
  computer = models.CharField(max_length=1, choices=EVENTS_CHOICES)
  event = models.ImageField(upload_to='events/')
  
  def bild(self):
    if self.event:
      return '<a href = "%s"> <img src = "%s" width="50" height="50" /> </a>' % (self.event.url, self.event.url)
    return ''

  bild.allow_tags = True

  def cmp_check(self):
    if self.mensch in ['E','L','O']:
        return bool(self.mensch==self.computer)
    return None

  cmp_check.boolean = True
