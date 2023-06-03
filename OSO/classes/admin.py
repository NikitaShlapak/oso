from django.contrib import admin

from .models import StudyGroup


class StudyGroupAdmin(admin.ModelAdmin):
    def get_str(self, object):
        return f"{object.__str__()}"

    get_str.short_description = "Полное название"

    def get_study_year(self, object):
        return f"{object.get_study_year()}"

    get_study_year.short_description = "Курс"

    list_display = ('get_str', 'get_study_year','type', 'year')
    list_display_links = ('get_str',)
    sortable_by = ('get_str','type', 'year')
    readonly_fields = ('get_str', 'get_study_year')

    fieldsets = (
        ('Основное', {"fields": ("get_str", 'get_study_year')}),
        ("Данные о группе", {"fields": ("type", "numgroup", "year", 'subgroup', 'is_foreigns')}),
    )

admin.site.register(StudyGroup, StudyGroupAdmin)
