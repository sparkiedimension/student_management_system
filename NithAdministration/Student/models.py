from django.db import models
from Address.models import District, State, Address
from django.utils import timezone
from Institution.models import Degree, Subject


class Board(models.Model):
    boardName = models.CharField(max_length=50, verbose_name='Board')

    def __str__(self):
        return self.boardName


class Category(models.Model):
    categoryName = models.CharField(max_length=30, unique=True, verbose_name='Category Name')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.categoryName


class Activity(models.Model):
    activityName = models.CharField(max_length=30, verbose_name='Activity Name')
    startDate = models.DateField(verbose_name='Start Date')
    endDate = models.DateField(verbose_name='End Date')
    location = models.ForeignKey(District, on_delete=models.PROTECT)
    description = models.TextField(max_length=250)
    created =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.activityName 


class Student(models.Model):
    GENDER = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    DEPARTMENT = [('CSE', 'CSE'), ('ECE', 'ECE'), ('MECHANICAL', 'MECHANICAL'),('CIVIL', 'CIVIL'), ('CHEMICAL', 'CHEMICAL'), ('ELECTRICAL', 'ELECTRICAL'),('PHYSICS', 'PHYSICS'), ('CHEMISTRY', 'CHEMISTRY'), ('MATHEMATICS', 'MATHEMATICS'),('MANAGEMENT', 'MANAGEMENT'), ('HUMANITIES', 'HUMANITIES'), ('ARCHITECTURE', 'ARCHITECTURE'), ('MATERIAL SCIENCE', 'MATERIAL SCIENCE'), ('ENERGY AND ENVIRONMENT', 'ENERGY AND ENVIRONMENT')]
    registrationNumber = models.CharField(max_length=30, unique=True, verbose_name='Registration Number')
    id = models.CharField(max_length=15, unique=True, verbose_name='NITH Roll Number',primary_key=True)
    jeeMainRollNumber = models.CharField(max_length=15, verbose_name='JEE Main Roll Number')
    studentName = models.CharField(max_length=80, verbose_name='Student Name',null=True)
    mothersName = models.CharField(max_length=80, verbose_name="Mother's Name")
    fathersName = models.CharField(max_length=80, verbose_name="Father's Name")
    dob = models.DateField(verbose_name='Date Of Birth')
    gender = models.CharField(max_length=80, choices=GENDER)
    bonafideState = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='Bonafide State')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    familyIncome = models.IntegerField(blank=True, verbose_name='Family Income',null=True)
    jeeAIR = models.IntegerField(verbose_name='JEE Main All India Rank')
    jeeCategoryRank = models.IntegerField(verbose_name='JEE Main Category Rank')
    studentEmail = models.EmailField(verbose_name='Student Email')
    studentEmail_alt = models.EmailField(verbose_name='Alternate Student Email',null=True)
    studentMobileNumber = models.CharField(max_length=13, verbose_name='Student Mobile Number')
    studentMobileNumber_alt = models.CharField(max_length=13, verbose_name='Alternate Student Mobile Number',null=True)
    parentMobileNumber = models.CharField(max_length=13, verbose_name='Parent Mobile Number')
    parentMobileNumber_alt = models.CharField(max_length=13, verbose_name='Alternate Parent Mobile Number',null=True)   
    parenttEmail = models.EmailField(verbose_name='Parent Email',null=True)
    parentEmail_alt = models.EmailField(verbose_name='Alternate Parent Email',null=True)
    boarder = models.BooleanField()


    xMarks = models.FloatField(verbose_name='X Marks (Percentage) or (Grade x 9.5)')
    xBoard = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='xStudents', verbose_name='X Board')
    yearOfPassingX = models.SmallIntegerField(verbose_name='Year Of Passing X')

    xiiMarks = models.FloatField(verbose_name='XII Marks (Percentage) or (Grade x 9.5)')
    xiiBoard = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='xiiStudents', verbose_name='XII Board')
    yearOfPassingXii = models.SmallIntegerField(verbose_name='Year Of Passing XII')

    dateOfJoining = models.DateField(verbose_name='Date Of Joining')
    department = models.CharField(max_length=80, choices=DEPARTMENT)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)
    # BATCH =[('2016','2016'),('2017','2017'),('2018','2018'),('2019','2019'),('2020','2020'),('2021','2021')]
    batch = models.SmallIntegerField(verbose_name='Batch')


    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id 


class PermanentAddress(Address):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Permanent Address')
    street = models.CharField(max_length=80, verbose_name='Street / House No.')

    class Meta:
        verbose_name_plural = 'Permanent Address'


class CorrespondenceAddress(Address):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Correspondence Address')
    street = models.CharField(max_length=80, verbose_name='Street / House No.')

    class Meta:
        verbose_name_plural = 'Correspondence Address'


class Result(models.Model):
    GRADES = [(10, 'A'), (9, 'AB'), (8, 'B'), (7, 'BC'), (6, 'C'), (4, 'D'), (0, 'F')]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    semester = models.SmallIntegerField()
    created =models.DateTimeField(auto_now_add=True)
    grade = models.SmallIntegerField(choices=GRADES)
    noofpresents = models.FloatField(verbose_name='% No. of Presents', blank=True)
    totalclasses = models.FloatField(verbose_name='% Total classes', blank=True)

    @property
    def attendance(self):
        return round((100*self.noofpresents/self.totalclasses),2)

   
    def save(self, *args, **kwargs):
        super(Result, self).save(*args, **kwargs)
        grades = Grade.objects.filter(student=self.student).filter(semester=self.semester)
        print(grades)
        if len(grades) == 0:
            Grade(student=self.student, semester=self.semester).save()

    def __str__(self):
        return str(self.student) + ":  " + str(self.subject) + "  -  " + str(self.grade)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.IntegerField()

    @property
    def sgpi(self):
        results = Result.objects.filter(student=self.student).filter(semester=self.semester)
        (scoredPoints, totalPoints, maxGrade) = (0, 0, 10)
        for result in results:
            totalPoints += result.subject.credit * maxGrade
            scoredPoints += result.subject.credit * result.grade
        if totalPoints == 0: return 0
        return round((10 * scoredPoints / totalPoints), 2)

    @property
    def cgpi(self):
        (scoredPoints, totalPoints, maxGrade) = (0, 0, 10)
        results = Result.objects.filter(student=self.student).filter(semester__lte=self.semester)
        for result in results:
            totalPoints += result.subject.credit * maxGrade
            scoredPoints += result.subject.credit * result.grade
        if totalPoints == 0: return 0
        return round((10 * scoredPoints / totalPoints), 2)

    def __str__(self):
        return str(self.student) + "  -  Semester " + str(self.semester) + ":  " + str(self.sgpi)


class Participation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    achievement = models.CharField(max_length=30, blank=True)
    created =models.DateTimeField(auto_now_add=True)
        

    @property
    def activityName(self):
        return str(self.activity.activityName)

    class Meta:
        verbose_name_plural = 'Participation'

    def __str__(self):
        return str(self.student) + "  :  " + str(self.activity)


class Placements(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Roll No')
    company = models.CharField(max_length=50)
    package = models.IntegerField(blank=True, verbose_name='Package')
    created =models.DateTimeField(auto_now_add=True)
    

    @property
    def department(self):
        return str(self.student.department)

    class Meta:
        verbose_name_plural = 'Placements'
    def __str__(self):
        return str(self.student) 

class Suggestions(models.Model):
    student = models.CharField(max_length=15, verbose_name='student')
    suggestions = models.TextField(max_length=250)
    GENDER = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    gender = models.CharField(max_length=80, choices=GENDER)
    # @property
    # def gender(self):
    #     return str(self.student.gender)

   
    class Meta:
        verbose_name_plural = 'Suggestions'
    def __str__(self):
        return str(self.student)

class OtherExam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Roll No')
    EXAMS = [('GATE', 'GATE'),('CAT', 'CAT'), ('UPSC', 'UPSC'),('GRE', 'GRE'), ('GMAT', 'GMAT'), ('DRDO', 'DRDO'),('ISRO', 'ISRO'), ('MAT', 'MAT'), ('NET', 'NET'),('SSB', 'SSB'), ('SBI', 'SBI'), ('IRS', 'IRS')]

    exam = models.CharField(max_length=80, choices=EXAMS,verbose_name='Exam Name')
    examRollNumber = models.CharField(max_length=15, verbose_name='Exam Roll Number',null=True)
    examAIR = models.IntegerField(verbose_name='All India Rank',null=True)
    examMarks = models.FloatField(verbose_name='Exam Score')
    yearOfAppearingexam = models.SmallIntegerField(verbose_name='Year Of Appearing',null=True)
    nooftimeexam= models.IntegerField(verbose_name='No. of attempts',null=True)


    created =models.DateTimeField(auto_now_add=True)

    @property
    def department(self):
        return str(self.student.department)
    
    class Meta:
        verbose_name_plural = 'OtherExams'
    
    def __str__(self):
        return str(self.student) 