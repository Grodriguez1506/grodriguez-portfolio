from django.contrib import admin
from.models import Project, ContactRequest, Experience, Certificate, ProjectImages

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class CertificateAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    fields = ['image']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactRequest, ContactAdmin)
admin.site.register(Experience)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(ProjectImages)