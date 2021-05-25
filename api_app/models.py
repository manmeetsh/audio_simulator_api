from django.db import models

class song(models.Model):
	name = models.CharField(max_length=20)
	duration = models.DurationField()
	upld_time = models.DateTimeField()

class podcast(models.Model):
	name = models.CharField(max_length=20)
	duration = models.DurationField()
	upld_time = models.DateTimeField()
	host = models.CharField(max_length=100)
			

class audiobook(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	nrtr_name = models.CharField(max_length=100)
	upld_time = models.DateTimeField()
	duration = models.DurationField()



	# def __str__(self):
	# 	return self.f_name 