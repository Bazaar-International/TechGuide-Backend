from django.contrib import admin
from .models import Section, Subsection
from markdownx.admin import MarkdownxModelAdmin

class SubsectionAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'section', 'order']
    ordering = ['section', 'order']
    
class SubsectionAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'section', 'order']
    ordering = ['section', 'order']

admin.site.register(Section)
admin.site.register(Subsection, SubsectionAdmin)

# from django.contrib import admin
# from markdownx.admin import MarkdownxModelAdmin
# from .models import Section, Subsection

# @admin.register(Section)
# class SectionAdmin(MarkdownxModelAdmin):
#     list_display = ['title', 'order']
#     readonly_fields = ['html_content']

# @admin.register(Subsection)
# class SubsectionAdmin(MarkdownxModelAdmin):
#     list_display = ['title', 'section', 'order']
#     readonly_fields = ['html_content']
