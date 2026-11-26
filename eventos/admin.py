from django.contrib import admin
from django.utils.formats import number_format
from .models import eventos, inscripciones
# Register your models here.

class InscipcionesInLine(admin.TabularInline):
    model = inscripciones
    extra = 0
    readonly_fields = ('nombre','correo','cantidad','creada',)



@admin.register(eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('nombre','lugar','descripcion','valor_en_pesos','cupos','activo','cupos_disponibles')
    list_filter = ('activo', 'lugar')
    search_fields = ('nombre','lugar')
    list_editable = ('activo',)
    inlines = [InscipcionesInLine]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['valor'].label = 'Valor (CLP)'
        return form

    @admin.display(description='Valor (CLP)', ordering='valor')
    def valor_en_pesos(self, obj):
        return f"$ {number_format(obj.valor, use_l10n=True, force_grouping=True)}"


@admin.display(description='Disponibles')
def disponibles(self, obj):
    return obj.cupos_disponibles()


@admin.register(inscripciones)
class InscripcionesAdmin(admin.ModelAdmin):
    list_display = ('evento','nombre','correo','cantidad','creada')
    list_filter = ('evento',)
    search_fields = ('nombre','correo')
    readonly_fields = ('evento','nombre','correo','cantidad','creada',)