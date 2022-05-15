from django.contrib import admin
from .models import *


# Register your models here.
class GroupView(admin.ModelAdmin):
    list_display = ('data_formation', 'description')


class EntryView(admin.ModelAdmin):
    list_display = ('group', 'statement')


class StatementView(admin.ModelAdmin):
    list_display = (
        'client', 'type_statement', 'data_statement', 'contract_number', 'data_start_contract', 'data_start_contract',
        'package_documents', 'payment_status', 'passport_series', 'passport_number')


class ClientView(admin.ModelAdmin):
    list_display = (
        'surname', 'firstname', 'patronymic', 'date_birth', 'phone_number', 'date_enrollment',
        'growth', 'weight')


class AchievementsView(admin.ModelAdmin):
    list_display = (
        'client', 'rank', 'date_assignment', 'belt', 'competition', 'passport_number')


class CompetitionView(admin.ModelAdmin):
    list_display = (
        'certification_competition', 'date', 'time', 'place', 'coach_id', 'rating_id', 'cost')


class SpeakerView(admin.ModelAdmin):
    list_display = ('competition_id', 'entry')


class CoachingView(admin.ModelAdmin):
    list_display = ('practice_id', 'entry_id')


class CoachView(admin.ModelAdmin):
    list_display = ('surname', 'firstname', 'patronymic', 'phone_number', 'date_birth', 'date_enrollment')


class PracticeView(admin.ModelAdmin):
    list_display = ('coach', 'date', 'time', 'hall', 'cost')


admin.site.register(Group, GroupView)
admin.site.register(Entry, EntryView)
admin.site.register(Statement, StatementView)
admin.site.register(TypeStatement)
admin.site.register(PackageDocuments)
admin.site.register(Document)
admin.site.register(Client, ClientView)
admin.site.register(Achievements, AchievementsView)
admin.site.register(Belt)
admin.site.register(Rank)
admin.site.register(Competition, CompetitionView)
admin.site.register(Speaker, SpeakerView)
admin.site.register(Coaching, CoachingView)
admin.site.register(Rating)
admin.site.register(Coach, CoachView)
admin.site.register(Practice, PracticeView)
admin.site.register(Hall)
