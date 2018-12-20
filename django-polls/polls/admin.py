from django.contrib import admin

from .models import Question, Choice

'''Django will construct a defaul form representation. Will need to use below alt to customize '''
#admin.site.register(Question)

''' The code to replace generic choice '''
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    ''' Customizing the fields layout. Choosing an intuitive order is an important usability detail'''
    #fields = ['pub_date', 'question_text']

    ''' Add more to the list of questions '''
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    ''' Works similat to above but splits them up even more '''
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]

    ''' That adds a “Filter” sidebar that lets people filter the change list by the pub_date field '''
    ''' Django knows what type of list filter to use becasue pub_date is a DateTimeField '''
    list_filter = ['pub_date']

    ''' Adds a search bar '''
    search_fields = ['question_text']

''' This particular change above makes the “Publication date” come before the “Question” field '''
admin.site.register(Question, QuestionAdmin)

''' Creates that annoying choice alone with a dropdown menu to select the question '''
#admin.site.register(Choice)
