from RFApp.dtos.ExerciseRecordDTO import ExerciseRecordDTO
from RFApp.mappers.exerciseRecordMapper import ExerciseRecordMapper
from ..repositories.exerciseRecordsRepository import ExerciseRecordRepo

class ExerciseRecordService():

    _erRepo = ExerciseRecordRepo()
    _erMapper = ExerciseRecordMapper()
    
    def get_all_exercise_records(self) -> list[ExerciseRecordDTO]:
        er = list(map(lambda x: self._erMapper.map_to_dto(x), self._erRepo.get_all()))
        return er
    
    def get_ExerciseRecord_based_on_exercise_day_wn_id(self, exercise: str, day: int, workoutNum: int, auth:int) -> list[ExerciseRecordDTO]:
        record = self._erRepo.get_er_based_on_exercise_day_wn_id(exercise, day, workoutNum, auth)
        if (record.exists()):
            return self._erMapper.map_to_dto(record[0])
        else:
            return -10
    
    def get_ExerciseRecord_average_based_on_name_id(self, name:str, id) -> float:
        er = self._erRepo.get_all_er_based_on_exercise_id(name, id)
        if (len(er) == 0):
            return 0
        else:
            sum = 0
            for item in er:
                sum += item.weight
            return sum / len(er)
    
    def exerciseRecord_track_workout(self, dto:ExerciseRecordDTO):
        try:
            entity = self._erMapper.map_to_er(dto)
            self._erRepo.save_record(entity)
            return self._erMapper.map_to_dto(entity)
        except Exception as e:
            raise Exception(e.args[0])