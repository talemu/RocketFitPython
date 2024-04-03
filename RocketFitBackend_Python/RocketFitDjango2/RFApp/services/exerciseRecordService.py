from RFApp.dtos.ExerciseRecordDTO import ExerciseRecordDTO
from RFApp.mappers.exerciseRecordMapper import ExerciseRecordMapper
from ..repositories.exerciseRecordsRepository import ExerciseRecordRepo

class ExerciseRecordService():
    """
    Class: Service class dedicated to handling Exercise Record business logic.
    """

    _erRepo = ExerciseRecordRepo()
    _erMapper = ExerciseRecordMapper()
    
    def get_all_exercise_records(self) -> list[ExerciseRecordDTO]:
        er = list(map(lambda x: self._erMapper.map_to_dto(x), self._erRepo.get_all()))
        return er
    
    def get_ExerciseRecord_based_on_exercise_day_wn_id(self, exercise: str, day: int, workoutNum: int, auth:int) -> list[ExerciseRecordDTO]:
        record = self._erRepo.get_er_based_on_exercise_day_wn_id(exercise, day, workoutNum, auth)
        if (record.exists()):
            return list(map(lambda x: self._erMapper.map_to_dto(x), record))
        else:
            return -10
    
    """
        Method: Gets the average weight of an exercise based on the exercise name and id.
    """
    def get_ExerciseRecord_average_based_on_name_id(self, name:str, id) -> float:
        er = self._erRepo.get_all_er_based_on_exercise_id(name, id)
        if (len(er) == 0):
            return 0
        else:
            sum = 0
            for item in er:
                sum += item.weight
            return sum / len(er)
    
    """
        Method: Validates the Exercise Record sent from the client side. If the record is valid, it is saved to the database (sent to repo class).

            Input: ExerciseRecordDTO object containing the exercise record to be saved.

            Returns: ExerciseRecordDTO object containing the saved exercise if successful.
    """
    def exerciseRecord_track_workout(self, dto:ExerciseRecordDTO):
        try:
            exercise_record = self._erMapper.map_to_er(dto)
            # ensure all the exercise record fields are present
            exercise_record.clean()
            self._erRepo.save_record(exercise_record)
            return self._erMapper.map_to_dto(exercise_record)
        except Exception as e:
            raise Exception(e.args[0])