from django.contrib import admin
from .models import Local, Tipo, Fabricante, Componente

admin.site.register(Local)
admin.site.register(Tipo)
admin.site.register(Fabricante)
admin.site.register(Componente)
