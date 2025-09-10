from django.contrib import admin
from .models import Empresa, User_model, User_empresa

# Register your models here.


class empresasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'status')
    search_fields = ('nome',)

class custom_user_admin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    search_fields = ('nome',)

class user_empresa_admin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    search_fields = ('nome',)


admin.site.register(Empresa,empresasAdmin)
admin.site.register(User_model, custom_user_admin)
admin.site.register(User_empresa, user_empresa_admin)


