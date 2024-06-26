import datetime
from ..models import Exerciserecord

class ExerciseRecordRepo:
    """
    Class: Repository class dedicated to reading and writing Exercise Records to the database.
    """
    def get_all(self):
        return Exerciserecord.objects.all()

    def get_er_based_on_exercise_day_wn_id(self, name:str, day:int, workoutNum:int, id:int):
        return Exerciserecord.objects.filter(exercise_name = name, day = day, workout_number = workoutNum, auth_id = id)
    
    def get_all_er_based_on_exercise_id(self, name:str, id:int):
        return Exerciserecord.objects.filter(exercise_name = name, auth_id = id)
    
    def get_exercise_record_by_name_startdate_enddate_id(self, name:str, start_date:str, end_date:str, id:int):
        #including the entire day of the end date
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        return Exerciserecord.objects.filter(exercise_name = name, created_date__gte = start_date, created_date__lte = end_date, auth_id = id)
    
    def get_exercise_record_unique_exercise_record(self, substring:str, id:int):
        return Exerciserecord.objects.values_list('exercise_name', flat=True).distinct().filter(auth_id = id, exercise_name__contains = substring)
    
    """
        Method: Save Exercise Record to the database.
    """
    def save_record(self, exerciserecord):
        try:
            return exerciserecord.save()
        except Exception as e:
            raise Exception(e.args[0])