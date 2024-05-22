import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import WeekButtons from "../components/MainPageContent/WeekButtons";
import WeekContent from "../components/MainPageContent/WeekContent";
import Spinner from "../components/Spinner";
import {
  StandardizeWorkouts,
  WorkoutItem,
} from "../services/workoutExerciseService";
import exerciseRecordService from "../services/exerciseRecordService";
import exerciseService, { Exercise } from "../services/exerciseService";

interface Props {
  authId: number;
}

const MainPage = ({ authId }: Props) => {
  const Navigate = useNavigate();
  useEffect(() => {
    if (authId == -10) {
      Navigate("/unauthorized");
    }
  }, [authId]);

  const location = useLocation();
  //redirect to workouts page, no workout inputted
  useEffect(() => {
    if (location.state === null) Navigate("/myworkouts");
  }, []);

  //data incoming from WorkoutPage returning back to main page
  if (location.state !== null) {
    const workout = location.state[1];
    const [week, setWeek] = useState(
      localStorage.getItem("savedWeekNumber") === "null"
        ? 1
        : JSON.parse(localStorage.getItem("savedWeekNumber") || "{}")
    );
    const [isPreviousButtonDisabled, setPreviousButtonDisabled] =
      useState<boolean>(week <= 1);
    const [isNextButtonDisabled, setNextButtonDisabled] =
      useState<boolean>(false);
    const [workoutArray, setWorkoutArray] = useState<WorkoutItem[]>([]);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
      setWorkoutArray(StandardizeWorkouts(workout, week));
      setPreviousButtonDisabled(week <= 1);
      setNextButtonDisabled(week >= workout.weeks);
      setLoading(false);
    }, [week]);

    // useEffect(() => {
    //   const { request } = exerciseService.getAll("/");
    //   request.then((response) => {
    //     const response_exercises = response.data as unknown[] as Exercise[];
    //     setExercises(response_exercises);
    //   });
    // });

    // useEffect(() => {
    //   console.log(workoutArray);
    //   workoutArray.map((workoutItem: WorkoutItem) => {
    //     const fetchData = async () => {
    //       const response2 = await exerciseRecordService.getAll(
    //         "/item?exercise=" +
    //           exercises.find(
    //             (element: Exercise) =>
    //               element.exerciseId === workoutItem.exercise
    //           )?.exerciseName +
    //           "&day=" +
    //           workoutItem.day +
    //           "&workoutNum=" +
    //           workout.workoutNumber +
    //           "&auth=" +
    //           authId
    //       ).request;

    //       const exercise_record_value = response2.data;
    //       console.log(exercise_record_value);
    //     };
    //     fetchData();
    //   });
    // }, [workoutArray]);

    const handleWeekData = (data: number) => {
      window.location.reload();
      setWeek(data);
    };

    return (
      <>
        {loading ? (
          <Spinner />
        ) : (
          <>
            {" "}
            <WeekContent
              authId={authId}
              week={week}
              workout={workout}
              workoutArray={workoutArray}
            />
            <WeekButtons
              isPreviousButtonDisabled={isPreviousButtonDisabled}
              isNextButtonDisabled={isNextButtonDisabled}
              week={week}
              sendWeekToParent={handleWeekData}
            />{" "}
          </>
        )}
      </>
    );
  }
  return <div></div>;
};
export default MainPage;
