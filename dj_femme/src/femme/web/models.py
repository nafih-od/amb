from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class RegistrationClass(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    dob = models.DateField()
    message = models.TextField()

    class Meta:
        db_table = 'web_registration'
        verbose_name = _('registration')
        verbose_name_plural = _('registrations')

    def __unicode__(self):
        return self.name


class AboutClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to="web/about/")

    class Meta:
        db_table = 'web_about'
        verbose_name = _('about')
        verbose_name_plural = _('abouts')

    def __unicode__(self):
        return self.title


class IssueClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to='web/issue/')


    class Meta:
        db_table = 'web_issue'
        verbose_name = _('issue')
        verbose_name_plural = _('issues')


    def __unicode__(self):
        return self.title


class WhyClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to='web/why/')


    class Meta:
        db_table = 'web_why'
        verbose_name = _('why')
        verbose_name_plural = _('why')


    def __str__(self):
        return self.title

class FrClass(models.Model):
    title=models.CharField(max_length=128)
    content=models.ForeignKey(WhyClass,on_delete=models.CASCADE,related_name="fr_classes")

    class Meta:
        db_table='fr'
        verbose_name=_('fr')
        verbose_name_plural = _('fr')

    def __str__(self):
        return self.title


class NopClass(models.Model):
    title=models.CharField(max_length=128)
    content=models.ForeignKey(FrClass,on_delete=models.CASCADE,related_name="nop_classes")

    class Meta:
        db_table='nop'
        verbose_name=_('nop')
        verbose_name_plural = _('nop')

    def __unicode__(self):
        return self.title











