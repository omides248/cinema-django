from django.contrib import admin
from .models import Screening, Chair, Hall, Cinema

admin.site.register(Screening)
admin.site.register(Chair)
admin.site.register(Hall)
admin.site.register(Cinema)