from django.contrib import admin
from .models import Dog

# Register your models here.
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'description')
admin.site.register(Dog, DogAdmin)

admin.site.site_header = "Puppies friends direct admin"
admin.site.site_title = "Direct admin"
