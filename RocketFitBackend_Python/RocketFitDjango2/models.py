# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Exercise(models.Model):
    exerciseid = models.AutoField(db_column='ExerciseID', primary_key=True)  # Field name made lowercase.
    exercisename = models.CharField(db_column='ExerciseName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exercise'


class Exerciserecord(models.Model):
    exercise_name = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()
    auth_id = models.IntegerField()
    day = models.IntegerField()
    workout_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ExerciseRecord'


class Rfauthuser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    password = models.CharField(max_length=28)
    username = models.CharField(max_length=50)
    email_address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'RFAuthUser'


class Workoutexercise(models.Model):
    workoutexerciseid = models.AutoField(db_column='WorkoutExerciseID', primary_key=True)  # Field name made lowercase.
    days = models.CharField(max_length=200)
    exercises = models.CharField(max_length=200)
    sets = models.CharField(max_length=200)
    reps = models.CharField(max_length=200)
    rest = models.CharField(max_length=200)
    weeks = models.IntegerField()
    authid = models.IntegerField(db_column='AuthID')  # Field name made lowercase.
    workoutnumber = models.IntegerField(db_column='WorkoutNumber')  # Field name made lowercase.
    workoutname = models.CharField(db_column='WorkoutName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkoutExercise'


class Workouttemplate(models.Model):
    workouttemplateid = models.AutoField(db_column='WorkoutTemplateID', primary_key=True)  # Field name made lowercase.
    workoutname = models.CharField(max_length=200, db_collation='utf8mb3_general_ci')
    exercises = models.CharField(db_column='Exercises', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    sets = models.CharField(db_column='Sets', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    reps = models.CharField(db_column='Reps', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    rest = models.CharField(db_column='Rest', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    days = models.CharField(db_column='Days', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    weeks = models.CharField(db_column='Weeks', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkoutTemplate'
