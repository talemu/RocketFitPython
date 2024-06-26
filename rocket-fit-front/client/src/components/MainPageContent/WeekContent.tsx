import { Link } from "react-router-dom";
import styled from "styled-components";
import { WorkoutItem } from "../../services/workoutExerciseService";
import { Slide } from "react-awesome-reveal";
import { useEffect } from "react";

const WeekHeader = styled.h1`
  padding: 0em 0em 0em 1em;
`;

const Content = styled.div`
  padding: 0em 0em 0em 1em;
`;

const DayButton = styled.button`
  margin: 1em 2em;
  padding: 1em;
  text-align: start;
  width: 50%;
  border-radius: 0.5em;
  background-color: red;
  color: white;

  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(0.5em) translateZ(0);
  transform: perspective(0.5em) translateZ(0);
  box-shadow: 0 0 0.5em rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: transform;
  transition-property: transform;

  &:hover,
  &:focus,
  &:active {
    -webkit-transform: translateX(0.5em);
    transform: translateX(0.5em);
  }
`;

const SlideDiv = styled(Slide)``;

interface Props {
  authId: number;
  week: number;
  workout: any;
  workoutArray: WorkoutItem[];
}

const WeekContent = ({ authId, week, workout, workoutArray }: Props) => {
  const currentWeek = Number(week);
  const dayItems = [...new Set(workoutArray.map((item) => item.day))];
  useEffect(() => {}, []);
  return (
    <>
      <WeekHeader>Week {currentWeek}</WeekHeader>{" "}
      <Content>
        {dayItems.map((item, count) => (
          <SlideDiv key={count} delay={count * 50}>
            <Link
              to="/workout"
              state={[
                workout,
                workoutArray.filter((item2) => item2.day === item),
                authId,
                workout.workoutNumber,
                week,
              ]}
            >
              <DayButton>Day {item - (week - 1) * 7}</DayButton>
            </Link>
          </SlideDiv>
        ))}
      </Content>
    </>
  );
};

export default WeekContent;
