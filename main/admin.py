from django.contrib import admin
from .models import Exhibition, Collection, Work, WorkPicture

admin.site.register(Exhibition)
admin.site.register(Collection)
admin.site.register(Work)
admin.site.register(WorkPicture)
