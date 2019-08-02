from django.contrib import admin

from dbdav.models import CollectionModel, ObjectModel

# Register your models here.
@admin.register(CollectionModel)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(ObjectModel)
class ObjectAdmin(admin.ModelAdmin):
    pass
