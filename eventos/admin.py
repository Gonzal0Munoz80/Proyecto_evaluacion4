from django.contrib import admin
from .models import eventos, inscripciones
# Register your models here.

class InscipcionesInLine(admin.TabularInline):
    model = inscripciones
    extra = 0
    readonly_fields = ('nombre','correo','cantidad','creada',)



@admin.register(eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('nombre','lugar','descripcion','valor','cupos','activo','cupos_disponibles')
    list_filter = ('activo', 'lugar')
    search_fields = ('nombre','lugar')
    list_editable = ('activo',)
    inlines = [InscipcionesInLine]


@admin.display(description='Disponibles')
def disponibles(self, obj):
    return obj.cupos_disponibles()


@admin.register(inscripciones)
class InscripcionesAdmin(admin.ModelAdmin):
    list_display = ('evento','nombre','correo','cantidad','creada')
    list_filter = ('evento',)
    search_fields = ('nombre','correo')
    readonly_fields = ('evento','nombre','correo','cantidad','creada',)