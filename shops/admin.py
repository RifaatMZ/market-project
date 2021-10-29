from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from shops.models import Location, Shop, ShopAlbum, Contacts, ItemDetail


admin.site.register(Shop)
admin.site.register(ShopAlbum)
admin.site.register(Contacts)
admin.site.register(ItemDetail)
admin.site.register(Location,DraggableMPTTAdmin,
                    list_display=('tree_actions','indented_title',),
                    list_display_links=('indented_title',),
                    )