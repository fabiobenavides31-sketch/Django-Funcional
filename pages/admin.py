from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# Configuración personalizada para el panel de gestión
admin.site.site_header = "Proyecto con Django"
admin.site.site_title = "Panel de Gestión"
admin.site.index_title = "Bienvenido al Panel de Gestión"