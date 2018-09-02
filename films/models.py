from django.db import models
from django.utils.translation import ugettext_lazy as _


class Genre(models.Model):
	name 				= models.CharField(verbose_name=_("gener"), max_length=128)


	def __str__(self):
		return self.name



class Picture(models.Model):
	name 				= models.CharField(verbose_name=_("picture") , max_length=128)
	film  				= models.ForeignKey("Film", verbose_name=_("film"), on_delete=models.CASCADE, related_name='gallery')

	def __str__(se):
		return self.name


class Comment(models.Model):
	description			= models.CharField(verbose_name=_("description"), max_length=255, null=True)
	timestamp			= models.DateTimeField(verbose_name=_("timestamp") , auto_now_add=True)
	film  				= models.ForeignKey("Film" ,verbose_name=_("gener") , on_delete=models.CASCADE, related_name='comments')

	def __str__(sel):
		return self.films



class Film(models.Model):

	name 				= models.CharField(verbose_name=_("name"), max_length=128)
	slug 				= models.SlugField(verbose_name=_("slug"), blank=True, unique=True)
	description 		= models.CharField(verbose_name=_("description"), max_length=255)
	length				= models.IntegerField(verbose_name=_("length"))
	director			= models.CharField(verbose_name=_("director"), max_length=30)
	producer			= models.CharField(verbose_name=_("producer"), max_length=30)
	writer 				= models.CharField(verbose_name=_("writer"), max_length=30)
	release_date 		= models.DateField(verbose_name=_("release_date"))
	image				= models.ImageField(verbose_name=_("image"),upload_to='img_films/', null=True, blank=True)
	timestamp 			= models.DateTimeField(verbose_name=_("timestamp"), auto_now_add=True)
	genres 				= models.ManyToManyField(Genre, verbose_name=_("genres"))
	director 			= models.ForeignKey("People", verbose_name=_("director"), on_delete=models.CASCADE, related_name="film_director")
	producer 			= models.ForeignKey("People", verbose_name=_("producer"), on_delete=models.CASCADE, related_name="film_producer")
	writer 				= models.ForeignKey("People", verbose_name=_("writer"), on_delete=models.CASCADE, related_name="film_writer")


	def __str__(self):
		return self.name


class People(models.Model):
	name 			= models.CharField(verbose_name=_("name"), max_length=128)

	def __str__(se):
		return self.name