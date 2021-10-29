from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from items.models import Category, Item, ItemAlbum


admin.site.register(Item)
admin.site.register(ItemAlbum)
admin.site.register(Category,DraggableMPTTAdmin,
                    list_display=('tree_actions','indented_title',),
                    list_display_links=('indented_title',),
                    )