from django.contrib import admin
from .models import gold_hand,gold_goshvareh,gold_ring,silver_goshvareh,silver_hand,silver_ring,stones,Tag
# Register your models here.
admin.site.register(gold_ring)
admin.site.register(gold_goshvareh)
admin.site.register(gold_hand)
admin.site.register(silver_ring)
admin.site.register(silver_hand)
admin.site.register(silver_goshvareh)
admin.site.register(stones)
admin.site.register(Tag)