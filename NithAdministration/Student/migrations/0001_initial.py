# Generated by Django 2.2.1 on 2019-07-02 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Address', '0001_initial'),
        ('Institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityName', models.CharField(max_length=30, verbose_name='Activity Name')),
                ('startDate', models.DateField(verbose_name='Start Date')),
                ('endDate', models.DateField(verbose_name='End Date')),
                ('description', models.TextField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Address.District')),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardName', models.CharField(max_length=50, verbose_name='Board')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30, unique=True, verbose_name='Category Name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=15, verbose_name='Roll Number')),
                ('suggestions', models.TextField(max_length=250)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('registrationNumber', models.CharField(max_length=30, unique=True, verbose_name='Registration Number')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='NITH Roll Number')),
                ('jeeMainRollNumber', models.CharField(max_length=15, verbose_name='JEE Main Roll Number')),
                ('studentName', models.CharField(max_length=80, null=True, verbose_name='Student Name')),
                ('mothersName', models.CharField(max_length=80, verbose_name="Mother's Name")),
                ('fathersName', models.CharField(max_length=80, verbose_name="Father's Name")),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=80)),
                ('familyIncome', models.IntegerField(blank=True, null=True, verbose_name='Family Income')),
                ('jeeAIR', models.IntegerField(verbose_name='JEE Main All India Rank')),
                ('jeeCategoryRank', models.IntegerField(verbose_name='JEE Main Category Rank')),
                ('studentEmail', models.EmailField(max_length=254, verbose_name='Student Email')),
                ('studentEmail_alt', models.EmailField(max_length=254, null=True, verbose_name='Alternate Student Email')),
                ('studentMobileNumber', models.CharField(max_length=13, verbose_name='Student Mobile Number')),
                ('studentMobileNumber_alt', models.CharField(max_length=13, null=True, verbose_name='Alternate Student Mobile Number')),
                ('parentMobileNumber', models.CharField(max_length=13, verbose_name='Parent Mobile Number')),
                ('parentMobileNumber_alt', models.CharField(max_length=13, null=True, verbose_name='Alternate Parent Mobile Number')),
                ('parenttEmail', models.EmailField(max_length=254, null=True, verbose_name='Parent Email')),
                ('parentEmail_alt', models.EmailField(max_length=254, null=True, verbose_name='Alternate Parent Email')),
                ('boarder', models.BooleanField()),
                ('xMarks', models.FloatField(verbose_name='X Marks (Percentage) or (Grade x 9.5)')),
                ('yearOfPassingX', models.SmallIntegerField(verbose_name='Year Of Passing X')),
                ('xiiMarks', models.FloatField(verbose_name='XII Marks (Percentage) or (Grade x 9.5)')),
                ('yearOfPassingXii', models.SmallIntegerField(verbose_name='Year Of Passing XII')),
                ('dateOfJoining', models.DateField(verbose_name='Date Of Joining')),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('MECHANICAL', 'MECHANICAL'), ('CIVIL', 'CIVIL'), ('CHEMICAL', 'CHEMICAL'), ('ELECTRICAL', 'ELECTRICAL'), ('PHYSICS', 'PHYSICS'), ('CHEMISTRY', 'CHEMISTRY'), ('MATHEMATICS', 'MATHEMATICS'), ('MANAGEMENT', 'MANAGEMENT'), ('HUMANITIES', 'HUMANITIES'), ('ARCHITECTURE', 'ARCHITECTURE'), ('MATERIAL SCIENCE', 'MATERIAL SCIENCE'), ('ENERGY AND ENVIRONMENT', 'ENERGY AND ENVIRONMENT')], max_length=80)),
                ('batch', models.SmallIntegerField(verbose_name='Batch')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bonafideState', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Address.State', verbose_name='Bonafide State')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Student.Category')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Institution.Degree')),
                ('xBoard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='xStudents', to='Student.Board', verbose_name='X Board')),
                ('xiiBoard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='xiiStudents', to='Student.Board', verbose_name='XII Board')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('grade', models.SmallIntegerField(choices=[(10, 'A'), (9, 'AB'), (8, 'B'), (7, 'BC'), (6, 'C'), (4, 'D'), (0, 'F')])),
                ('noofpresents', models.FloatField(blank=True, verbose_name='% No. of Presents')),
                ('totalclasses', models.FloatField(blank=True, verbose_name='% Total classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Institution.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('package', models.IntegerField(blank=True, verbose_name='Package')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student', verbose_name='Roll No')),
            ],
            options={
                'verbose_name_plural': 'Placements',
            },
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(verbose_name='Pin Code')),
                ('street', models.CharField(max_length=80, verbose_name='Street / House No.')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Address.City')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Student.Student', verbose_name='Permanent Address')),
            ],
            options={
                'verbose_name_plural': 'Permanent Address',
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(blank=True, max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Student.Activity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
            options={
                'verbose_name_plural': 'Participation',
            },
        ),
        migrations.CreateModel(
            name='OtherExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(choices=[('GATE', 'GATE'), ('CAT', 'CAT'), ('UPSC', 'UPSC'), ('GRE', 'GRE'), ('GMAT', 'GMAT'), ('DRDO', 'DRDO'), ('ISRO', 'ISRO'), ('MAT', 'MAT'), ('NET', 'NET'), ('SSB', 'SSB'), ('SBI', 'SBI'), ('IRS', 'IRS')], max_length=80, verbose_name='Exam Name')),
                ('examRollNumber', models.CharField(max_length=15, null=True, verbose_name='Exam Roll Number')),
                ('examAIR', models.IntegerField(null=True, verbose_name='All India Rank')),
                ('examMarks', models.FloatField(verbose_name='Exam Score')),
                ('yearOfAppearingexam', models.SmallIntegerField(null=True, verbose_name='Year Of Appearing')),
                ('nooftimeexam', models.IntegerField(null=True, verbose_name='No. of attempts')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student', verbose_name='Roll No')),
            ],
            options={
                'verbose_name_plural': 'OtherExams',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='CorrespondenceAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(verbose_name='Pin Code')),
                ('street', models.CharField(max_length=80, verbose_name='Street / House No.')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Address.City')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Student.Student', verbose_name='Correspondence Address')),
            ],
            options={
                'verbose_name_plural': 'Correspondence Address',
            },
        ),
    ]
