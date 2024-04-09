from RFApp.dtos.ExerciseDTO import ExerciseDTO
from RFApp.mappers.exerciseMapper import ExerciseMapper
from ..serializers import ExerciseSerializer
from ..repositories.exerciseRepository import ExerciseRepo

class ExerciseService:

    """
    Class: Service class dedicated to handling Exercise business logic.
    """

    _eRepo = ExerciseRepo()
    _eMapper = ExerciseMapper()

    def get_all_exercises(self) -> list[ExerciseDTO]:
        return list(map(lambda x : self._eMapper.map_to_dto(x), self._eRepo.get_all()))
    
    def get_exercise_by_id(self, id):
        exerciseItem = self._eRepo.get_exercise_by_id(id)
        dto = self._eMapper.map_to_dto(exerciseItem)
        if (dto == None):
            raise Exception("Exercise Does Not Exist with ID")
        return dto
    
    """
        Method: Validates the Exercise sent from the client side. If the record is valid, it is saved to the database (sent to repo class).

            Input: ExerciseDTO object containing the exercise record to be saved.

            Returns: ExerciseDTO object containing the saved exercise record if successful.
    """
    def add_exercise(self, ex):
        try:
            exercise = self._eMapper.map_to_e(ex)
            #ensure the exercise has all the valid fields
            exercise.clean()
            self._eRepo.save_exercise(exercise)
            return self._eMapper.map_to_dto(exercise)
        except Exception as e:
            raise Exception(e.args[0])