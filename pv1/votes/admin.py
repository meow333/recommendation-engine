from django.contrib import admin

# Register your models here.
from votes.models import Project, People, Votes

class VotesInline(admin.TabularInline):
    model = Votes
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    fields = ['name','category','score']
    inlines = [VotesInline]
    list_display = ('id','name','category','up_voted','down_voted','score','highest_10',)
    search_fields = ['name']

class PeopleAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [VotesInline]
    list_display = ('id','name','up_voted_to','down_voted_to','up_down_ratio',)
    search_fields = ['name']

class VotesAdmin(admin.ModelAdmin):
    fields = ['pid', 'ppid','vote']
    inlines = [VotesInline]
    list_display = ('pid', 'ppid','vote')

admin.site.register(Project, ProjectAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Votes, VotesAdmin)
