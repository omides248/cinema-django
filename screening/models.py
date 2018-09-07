from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels


class Chair(models.Model):
	chair_number 				= models.CharField(max_length=3, verbose_name=_("name"))
	status 						= models.BooleanField()
	order  						= models.ForeignKey("customers.Order", on_delete=models.CASCADE)
	screening   				= models.ForeignKey("Screening", on_delete=models.CASCADE)

	def __str__(self):
		return self.chair_number

	class Meta:
		verbose_name=_("chair")
		verbose_name_plural=_("chairs")


class Screening(models.Model):
	name 				= models.CharField(max_length=128, verbose_name=_("name"))
	price 				= models.IntegerField(verbose_name=_("price"))
	time_screening 		= jmodels.jDateTimeField(verbose_name=_("time_screening"))
	hall 				= models.ForeignKey("Hall", on_delete=models.CASCADE)
	cinema    			= models.ForeignKey("Cinema", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_("screening")
		verbose_name_plural=_("screenings")


class Hall(models.Model):
	name 				= models.CharField(max_length=128, verbose_name=_("name"))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_("hall")
		verbose_name_plural=_("halls")


class Cinema(models.Model):
	name 				= models.CharField(max_length=128, verbose_name=_("name"))
	city 				= models.CharField(max_length=128, verbose_name=_("city"))
	address				= RichTextField(max_length=128, verbose_name=_("description_city"))
	phone_number		= PhoneNumberField(verbose_name=_("phone_number"))
	movie  				= models.ForeignKey("movies.Movie", on_delete=models.CASCADE)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name=_("cinema")
		verbose_name_plural=_("cinemas")
