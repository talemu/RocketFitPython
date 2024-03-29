import { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { Exercise } from "../services/exerciseService";
import styled from "styled-components";
import NumberAdjuster from "../components/NumberAdjuster";

const HeaderOne = styled.h1``;

const StyledTable = styled.table``;

const TableBody = styled.tbody``;

const TableHeader = styled.th`
  padding: 1em 2em;
`;

const TableColumn = styled.td`
  text-align: center;
`;

const TableRecord = styled.tr``;

const TableHead = styled.thead``;

const WorkoutsButton = styled.button``;

const StartButton = styled.button``;

interface Props {
  authId: number;
}

const CustomizeWorkout = ({ authId }: Props) => {
  const Navigate = useNavigate();

  const location = useLocation();
  const workoutData = location.state;
  const validAuthIdShow = authId != -10;
  const [change, setChange] = useState<boolean>(false);

  useEffect(() => {
    if (authId == -10) {
      Navigate("/main");
    }
  }, [change]);

  const UpdateCurrent = (data: number, count: number, array: number[]) => {
    if (count != -1) {
      array[count] = data;
    } else {
      workoutData[0].weeks = data;
    }
    setChange(!change);
  };

  const AddWorkoutToUser = () => {};

  return (
    <>
      {validAuthIdShow ? (
        <>
          <WorkoutsButton>
            <Link to="/workouts">Back</Link>
          </WorkoutsButton>
          <HeaderOne>{workoutData[0].workoutName}</HeaderOne>
          <NumberAdjuster
            weeksFlag={true}
            sendDataToParent={(current) =>
              UpdateCurrent(current, -1, workoutData[0].weeks)
            }
            current={workoutData[0].weeks}
          />
          <StyledTable>
            <TableHead>
              <TableRecord>
                <TableHeader>Day</TableHeader>
                <TableHeader>Exercise</TableHeader>
                <TableHeader>Sets</TableHeader>
                <TableHeader>Reps</TableHeader>
                <TableHeader>Rest</TableHeader>
              </TableRecord>
            </TableHead>
            {workoutData[0].days.map((day: number, count: number) => (
              <>
                <TableBody>
                  <TableRecord>
                    {workoutData[0].days[count] !==
                    workoutData[0].days[count - 1] ? (
                      <TableColumn>{day}</TableColumn>
                    ) : (
                      <TableColumn></TableColumn>
                    )}

                    {
                      <TableColumn>
                        {
                          workoutData[1].find(
                            (element: Exercise) =>
                              element.exerciseId === count + 1
                          )?.exerciseName
                        }
                      </TableColumn>
                    }
                    {
                      <TableColumn>
                        <NumberAdjuster
                          weeksFlag={false}
                          sendDataToParent={(current) =>
                            UpdateCurrent(current, count, workoutData[0].sets)
                          }
                          current={workoutData[0].sets[count]}
                        />{" "}
                      </TableColumn>
                    }
                    {
                      <TableColumn>
                        <NumberAdjuster
                          weeksFlag={false}
                          sendDataToParent={(current) =>
                            UpdateCurrent(current, count, workoutData[0].reps)
                          }
                          current={workoutData[0].reps[count]}
                        />
                      </TableColumn>
                    }
                    {
                      <NumberAdjuster
                        weeksFlag={false}
                        sendDataToParent={(current) =>
                          UpdateCurrent(current, count, workoutData[0].rest)
                        }
                        current={workoutData[0].rest[count]}
                      />
                    }
                  </TableRecord>
                </TableBody>
              </>
            ))}
          </StyledTable>
          <StartButton onClick={AddWorkoutToUser}>Start Workout</StartButton>{" "}
        </>
      ) : (
        <div></div>
      )}
    </>
  );
};

export default CustomizeWorkout;
