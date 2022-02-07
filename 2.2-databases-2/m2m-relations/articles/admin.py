from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django import forms
from .models import Article, Relationship, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    tag = forms.IntegerField()
    article = forms.IntegerField()
    is_main = forms.BooleanField(required=True)

    def clean(self):
        super(RelationshipInlineFormset,self).clean()
        count = 0
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if type(is_main)== bool:
                count += int(is_main)
        if count == 0:
            raise ValidationError('Выберете основной тег')
        elif count > 1:
            raise ValidationError('Основной тег должен быть 1')

class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ("tag", "article", "is_main")