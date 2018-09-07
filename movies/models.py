import jdatetime
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from django.db import models
from customers.models import Order
from screening.models import Cinema



class Genre(models.Model):
	name = models.CharField(verbose_name=_("gener"), max_length=128)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_("genre")
		verbose_name_plural=_("genres")


class Picture(models.Model):
	name 					= models.CharField(verbose_name=_("name"), max_length=128)
	image 					= models.ImageField(verbose_name=_("image"), upload_to='img_movies/', null=True, blank=True)
	timestamp				= jmodels.jDateTimeField(verbose_name=_("timestamp"))
	movie  					= models.ForeignKey("movies.Movie", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_("picture")
		verbose_name_plural=_("pictures")


class Comment(models.Model):
	name 					= models.CharField(verbose_name=_("name"), max_length=128)
	description 			= RichTextField(verbose_name=_("description"), max_length=255, null=True)
	timestamp 				= jmodels.jDateTimeField(verbose_name=_("timestamp"), default=jdatetime.datetime.now)
	movie  					= models.ForeignKey("movies.Movie", on_delete=models.CASCADE, verbose_name=_("movie"))
	# user --> AbstractUser --> phoneNumber
	def __str__(self):
		return self.description

	class Meta:
		verbose_name=_("commet")
		verbose_name_plural=_("commets")


class Movie(models.Model):
	objects 				= jmodels.jManager()
	name 					= models.CharField(verbose_name=_("name"), max_length=128)
	slug 					= models.SlugField(verbose_name=_("slug"), blank=True, unique=True)
	description 			= RichTextField(verbose_name=_("description"), max_length=255, null=True)
	length 					= models.IntegerField(verbose_name=_("length"))
	director 				= models.CharField(verbose_name=_("director"), max_length=30)
	producer 				= models.CharField(verbose_name=_("producer"), max_length=30)
	actor 					= RichTextField(verbose_name=_("actor"), max_length=255)
	writer 					= models.CharField(verbose_name=_("writer"), max_length=30)
	release_date		 	= jmodels.jDateField(default=jdatetime.date.today, verbose_name=_("release_date"))
	timestamp 				= jmodels.jDateTimeField(verbose_name=_("timestamp"))
	genres 					= models.ManyToManyField(Genre, verbose_name=_("genres"))
	director 				= models.ForeignKey("People", on_delete=models.CASCADE, related_name="movie_director", verbose_name=_("director"))
	producer 				= models.ForeignKey("People", on_delete=models.CASCADE, related_name="movie_producer", verbose_name=_("producer"))
	writer 					= models.ForeignKey("People", on_delete=models.CASCADE, related_name="movie_writer", verbose_name=_("writer"))


	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_("movie")
		verbose_name_plural=_("movies")


class People(models.Model):
	name 					= models.CharField(verbose_name=_("name"), max_length=128)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name=_("people")
		verbose_name_plural=_("peoples")
