from django.contrib import admin
from blog.models import blog,contact

# Register your models here.

class blogadmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/style.css",)
        }

        js = ("js/app.js",)

admin.site.register(blog,blogadmin)
admin.site.register(contact)
