from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels

CHAIR_STATUS = (
	(0 , _('Not reserved chair')),
	(1 , _('Reserved'))
)

class Chair(models.Model):
	chair_number 				= models.CharField(max_length=3, verbose_name=_("name"))
	status 						= models.BooleanField(choices=CHAIR_STATUS, default=0, verbose_name=_("status"))
	order  						= models.ForeignKey("customers.Order", on_delete=models.CASCADE, verbose_name=_("order"))
	screening   				= models.ForeignKey("Screening", on_delete=models.CASCADE, verbose_name=_("screening"))

	def __str__(self):
		return self.chair_number

	class Meta:
		verbose_name=_("chair")
		verbose_name_plural=_("chairs")


class Screening(models.Model):
	name 				= models.CharField(max_length=128, verbose_name=_("name"))
	price 				= models.IntegerField(verbose_name=_("price"))
	time_screening 		= jmodels.jDateTimeField(verbose_name=_("time_screening"))
	hall 				= models.ForeignKey("Hall", on_delete=models.CASCADE, verbose_name=_("hall"))
	cinema    			= models.ForeignKey("Cinema", on_delete=models.CASCADE, verbose_name=_("cinema"))

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
	movie  				= models.ForeignKey("movies.Movie", on_delete=models.CASCADE, verbose_name=_("movie"))

	def __str__(self):
		return self.name


	class Meta:
		verbose_name=_("cinema")
		verbose_name_plural=_("cinemas")
