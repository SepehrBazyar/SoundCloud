from django.contrib import admin
from .models import (
    Fan,
    Artist,
    Relation,
)


# Register your models here.
admin.site.register(Fan)
admin.site.register(Artist)
admin.site.register(Relation)
