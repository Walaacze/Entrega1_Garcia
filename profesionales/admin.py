from django.contrib import admin

from profesionales.models import Administrativo, Freelance, Permanente

admin.site.register(Permanente)
admin.site.register(Freelance)
admin.site.register(Administrativo)
