from django.contrib	import admin
from blogs.models import Blogspost


#class BlogspostAdmin(admin.ModelAdmin):
	#fieldsets = [
    #    ('Title',					{'fields':	['title']}),
	#	 ('Date information',	{'fields':	['pub_date']}),
    #    ('Article',					{'fields':	['body']}),
    #    ('URL',					{'fields':	['url']}),
    #    ('Author',					{'fields':	['publisher']}),
#    ]
#list_display = ('title','pub_date','was_published_recently')

class BlogspostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('URL',              {'fields': ['url']}),
        ('Title',            {'fields': ['title']}),
        ('Author',           {'fields': ['publisher']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Article',          {'fields': ['body']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy	=	'pub_date'

admin.site.register(Blogspost, BlogspostAdmin)
