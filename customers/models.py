import jdatetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels
from django.db import models
from screening.models import Chair, Cinema






class Order(models.Model):
	order_number            = models.IntegerField(verbose_name=_("order_number"))
	transactio_number     	= models.IntegerField(verbose_name=_("transactio_number"))
	payment_datetime 		= jmodels.jDateTimeField(default=jdatetime.datetime.now,verbose_name=_("payment_datetime"))
	price                   = models.IntegerField(verbose_name=_("price"))
	status                  = models.CharField(max_length=128, verbose_name=_("status"))
	film 					= models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
	cinema 					= models.ForeignKey(Cinema, on_delete=models.CASCADE)
