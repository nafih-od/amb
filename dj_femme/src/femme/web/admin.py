from django.contrib import admin
from web.models import RegistrationClass, AboutClass, IssueClass,WhyClass,FrClass,NopClass


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dob', 'education', 'message')


admin.site.register(RegistrationClass, RegistrationAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(AboutClass, AboutAdmin)

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(IssueClass, IssueAdmin)


class WhyAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(WhyClass, WhyAdmin)


class FrAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(FrClass, FrAdmin)


class NopAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(NopClass, NopAdmin)




