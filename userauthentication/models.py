# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

COUNTRY = (('India','India'),('China','China'))
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	uname = models.CharField(max_length=200, default='username')
	uaddress = models.CharField(max_length=200)
	ucountry = models.CharField(max_length=200,choices=COUNTRY,default='India')
	uzipcode = models.IntegerField()
	usex = models.CharField(max_length=200)
	ulanguage = models.CharField(max_length=200)
	uabout = models.CharField(max_length=200)
	uimage = models.ImageField(upload_to="imageFolder/", blank=True)
	uphone = models.CharField(max_length=100,default='9999999999')
	uvechicle = models.CharField(max_length=200, default='KL')

	def __str__(self):
		return self.user.username

	#def __iter__(self):
	#	return [ self.user, 
     #            self.uaddress, 
      #           self.ucountry, 
       #          self.uzipcode, 
        #         self.usex, 
         #        self.ulanguage, 
          #       self.uabout, 
           #      self.uimage ]	

   # def get_absolute_url(self):	
	#	return reverse("name:details", kwargs={"pk": self.id})	