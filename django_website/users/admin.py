from django.contrib import admin
from .models import Profile, ProfilePictures

#admin.site.register(Profile)
#admin.site.register(ProfilePictures)

class PhotosInLine(admin.StackedInline):
    model = ProfilePictures
    extra = 3

class ProfileAdmin(admin.ModelAdmin):
    ''' Customizing the fields layout. Choosing an intuitive order is an important usability detail'''
    #fields = ['pub_date', 'question_text']

    ''' Works similat to above but splits them up even more
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]'''
    inlines = [PhotosInLine]

admin.site.register(Profile, ProfileAdmin)
