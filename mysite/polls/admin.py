from django.contrib import admin

from .models import Choice, Question

#class ChoiceInline(admin.StackedInline):
#Stacked choices-take up a lot of space on screen
class ChoiceInline(admin.TabularInline):
#Tabular choices make a table-less space on screen
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

#    fieldsets = [
#    (None,      {'fields':['question_text']}),
#    ('Date information', {'fields':['pub_date']}),
#    ]

    fieldsets = [
    (None,      {'fields':['question_text']}),
    ('Date information', {'fields':['pub_date'],
     'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    
    list_display = ('question_text','pub_date',
    'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
