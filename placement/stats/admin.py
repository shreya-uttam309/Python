from django.contrib import admin
from .models import PlacementStatistic
# Register your models here.
@admin.register(PlacementStatistic)
class PlacementStatisticAdmin(admin.ModelAdmin):
    list_display = ('year', 'company_name', 'students_placed', 'average_package', 'highest_package', 'role_offered')
    list_filter = ('year', 'recruitment_type')
    search_fields = ('company_name',)