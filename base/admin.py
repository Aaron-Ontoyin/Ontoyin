from django.contrib import admin

from .models import Contact, Gallery, Saying, Update, Upload

admin.site.register(Update)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Upload)
admin.site.register(Saying)