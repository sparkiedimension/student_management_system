from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
import csv
from django.http import HttpResponse
from .models import (
   Suggestions, Board, Category, Activity, Student,OtherExam,PermanentAddress, CorrespondenceAddress,Placements, Result, Grade, Participation
)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from django.contrib.admin import AdminSite


admin.site.site_url = "http://127.0.0.1:8000/nith/"

# class MyAdminSite(AdminSite):
#     site_url = 'http://127.0.0.1:8000/nith/'

# admin_site = MyAdminSite(name='myadmin')


class BoardAdmin(ImportExportModelAdmin):
    pass

def export_result(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    writer = csv.writer(response)
    writer.writerow(['StudentRollNO','Semester','Grade','Attendance'])
    results = queryset.values_list('student','semester','grade','attendance' )
    for Result in results:
        writer.writerow(Result)
    return response
export_result.short_description = 'Export slected results to csv'

def export_student(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_details.csv"'
    writer = csv.writer(response)
    writer.writerow(['StudentRollNO','StudentName'])
    results = queryset.values_list('id','studentName' )
    for Result in results:
        writer.writerow(Result)
    return response
export_student.short_description = 'Export  csv'

def export_participation(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="participation.csv"'
    writer = csv.writer(response)
    writer.writerow(['StudentRollNO','Achievement'])
    results = queryset.values_list('student','achievement' )
    for Result in results:
        writer.writerow(Result)
    return response
export_participation.short_description = 'Export slected participation to csv'





class ActivityAdmin(ImportExportModelAdmin):
    list_display=('activityName','created')
    list_filter=('activityName','created')
    search_fields=('activityName',)
    pass

class ResultAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('student','subject','grade','semester','created')
    list_filter=('subject','student__batch','grade','semester','created')
    search_fields=('student__id',)
    actions = [export_result]
    save_as = True
    save_on_bottom = True
    change_list_template = 'changes1.html'
    pass
    
class ParticipationAdmin(ImportExportModelAdmin):
    list_display=('student','activity','achievement','created')
    list_filter=('activity__activityName','achievement','created')
    search_fields=('student__id','achievement')
    actions = [export_participation]
    # save_as = True
    # save_on_bottom = True
    # change_list_template = 'changes4.html'
    # pass

class PermanentAddressInline(admin.TabularInline):
    model = PermanentAddress
    classes = ['collapse']

class CorrespondenceAddressInline(admin.TabularInline):
    model = CorrespondenceAddress
    classes = ['collapse']

class GradeInline(admin.TabularInline):
    model = Grade
    classes = ['collapse']
    fields = ('semester', 'sgpi', 'cgpi')
    readonly_fields = ('semester', 'sgpi', 'cgpi')

    def has_add_permission(self, *args):
        return False

class PlacementInline(admin.TabularInline):
    model = Placements
    classes = ['collapse']
    fields = ('company','package')

    def get_extra(self, *args, **kwargs):
        return 0
    

class OtherInline(admin.TabularInline):
    model = OtherExam
    classes = ['collapse']
    fields = ('exam','examRollNumber','examAIR','examMarks','yearOfAppearingexam','nooftimeexam')

    def get_extra(self, *args, **kwargs):
        return 0


class ParticipationInline(admin.TabularInline):
    model = Participation
    classes = ['collapse']

    def get_extra(self, *args, **kwargs):
        return 0

# class SuggestionInline(admin.TabularInline):
#     model = Suggestions
#     classes = ['collapse']


class StudentAdmin(ImportExportModelAdmin):
    
    actions = [export_student]
    save_as = True
    save_on_top = False
    change_list_template = 'changes.html'
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':20})},
        models.EmailField:{'widget': TextInput(attrs={'size':'20'})},
    }
    inlines = [ CorrespondenceAddressInline,PermanentAddressInline, GradeInline, ParticipationInline,OtherInline,PlacementInline]
    list_display=('registrationNumber','id','studentName','department','created')
    list_filter=('gender','department','batch','created')
    search_fields=('id','studentName')
    fieldsets = (
        ('Basic_Profile', {
            'classes':('collapse','wide','extrapretty'),
            'fields': ('registrationNumber','id','studentName',('gender','dob'),('fathersName','mothersName'),('jeeMainRollNumber','jeeAIR','jeeCategoryRank'),'bonafideState',('xiiBoard','xiiMarks','yearOfPassingXii'),('xBoard','xMarks','yearOfPassingX'),'category','familyIncome','boarder','dateOfJoining','degree','department','batch',)
        }),
        ('Contact_Details', {
            'classes': ('collapse','wide','extrapretty'),
            'fields': (('studentEmail','studentEmail_alt'),('studentMobileNumber','studentMobileNumber_alt'),('parenttEmail','parentEmail_alt'),('parentMobileNumber','parentMobileNumber_alt')),
            
        }),
        
    )
class PlacementnAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('student','company','package','created')
    list_filter=('student__batch','student__gender','student__department','created','company','package')
    search_fields=('student__id',)
    save_as = True
    save_on_bottom = True
    change_list_template = 'changes2.html'
    pass

class SuggestionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('student','suggestions')
    list_filter=('gender','suggestions')
    search_fields=('suggestions','student')
    save_as = True
    save_on_bottom = True
    change_list_template = 'changes5.html'
    pass

class OtherExamAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('student','exam','examRollNumber','examAIR','examMarks','created')
    list_filter=('student__batch','student__department','exam','created')
    search_fields=('student__id',)
    fieldsets = (
        ('Student_Profile', {
            'classes':('wide','extrapretty'),
            'fields': ('student',)
        }),

        ('Exam_details', {
            'classes':('wide','extrapretty'),
            'fields': (('exam','examRollNumber'),('examAIR','examMarks'),('yearOfAppearingexam','nooftimeexam'))
        }),
    )    
    save_as = True
    save_on_bottom = True
    change_list_template = 'changes3.html'
    pass

   
   

admin.site.register(Board,BoardAdmin)
admin.site.register(Category,BoardAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(Participation,ParticipationAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Placements,PlacementnAdmin)
admin.site.register(OtherExam,OtherExamAdmin)
admin.site.register(Suggestions,SuggestionAdmin)


 