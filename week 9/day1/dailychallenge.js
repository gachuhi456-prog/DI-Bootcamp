dailychallenge
npx create-react-app daily-planner
cd daily-planner

npm install redux react-redux

export const SELECT_DAY = "SELECT_DAY";
export const ADD_TASK = "ADD_TASK";
export const EDIT_TASK = "EDIT_TASK";
export const DELETE_TASK = "DELETE_TASK";

export const selectDay = (day) => ({
  type: SELECT_DAY,
  payload: day,
});

export const addTask = (day, task) => ({
  type: ADD_TASK,
  payload: { day, task },
});

export const editTask = (day, taskId, updatedTask) => ({
  type: EDIT_TASK,
  payload: { day, taskId, updatedTask },
});

export const deleteTask = (day, taskId) => ({
  type: DELETE_TASK,
  payload: { day, taskId },
});

import {
  SELECT_DAY,
  ADD_TASK,
  EDIT_TASK,
  DELETE_TASK,
} from "./actions";

const initialState = {
  selectedDay: new Date().toISOString().split("T")[0],
  tasks: {},
};

const plannerReducer = (state = initialState, action) => {
  switch (action.type) {
    case SELECT_DAY:
      return {
        ...state,
        selectedDay: action.payload,
      };

    case ADD_TASK: {
      const { day, task } = action.payload;

      return {
        ...state,
        tasks: {
          ...state.tasks,
          [day]: [...(state.tasks[day] || []), task],
        },
      };
    }

    case EDIT_TASK: {
      const { day, taskId, updatedTask } = action.payload;

      return {
        ...state,
        tasks: {
          ...state.tasks,
          [day]: state.tasks[day].map((task) =>
            task.id === taskId ? updatedTask : task
          ),
        },
      };
    }

    case DELETE_TASK: {
      const { day, taskId } = action.payload;

      return {
        ...state,
        tasks: {
          ...state.tasks,
          [day]: state.tasks[day].filter(
            (task) => task.id !== taskId
          ),
        },
      };
    }

    default:
      return state;
  }
};

export default plannerReducer;

import { createStore } from "redux";
import plannerReducer from "./reducers";

const store = createStore(plannerReducer);

store.subscribe(() => {
  localStorage.setItem(
    "plannerState",
    JSON.stringify(store.getState())
  );
});

export default store;

import React from "react";
import { connect } from "react-redux";
import { selectDay } from "../redux/actions";

const DatePicker = ({ selectedDay, selectDay }) => {
  return (
    <div>
      <h3>Select Day</h3>

      <input
        type="date"
        value={selectedDay}
        onChange={(e) => selectDay(e.target.value)}
      />
    </div>
  );
};

const mapStateToProps = (state) => ({
  selectedDay: state.selectedDay,
});

export default connect(
  mapStateToProps,
  { selectDay }
)(DatePicker);

import React, { useState } from "react";
import { connect } from "react-redux";
import { addTask } from "../redux/actions";

const TaskForm = ({ selectedDay, addTask }) => {
  const [taskText, setTaskText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!taskText.trim()) {
      alert("Task cannot be empty");
      return;
    }

    const task = {
      id: Date.now(),
      text: taskText,
    };

    addTask(selectedDay, task);
    setTaskText("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter Task"
        value={taskText}
        onChange={(e) => setTaskText(e.target.value)}
      />

      <button type="submit">
        Add Task
      </button>
    </form>
  );
};

const mapStateToProps = (state) => ({
  selectedDay: state.selectedDay,
});

export default connect(
  mapStateToProps,
  { addTask }
)(TaskForm);

import React from "react";
import { connect } from "react-redux";
import {
  editTask,
  deleteTask,
} from "../redux/actions";

const TaskList = ({
  selectedDay,
  tasks,
  editTask,
  deleteTask,
}) => {
  const dayTasks = tasks[selectedDay] || [];

  const handleEdit = (task) => {
    const updatedText = prompt(
      "Edit Task",
      task.text
    );

    if (!updatedText) return;

    editTask(selectedDay, task.id, {
      ...task,
      text: updatedText,
    });
  };

  return (
    <div>
      <h3>Tasks</h3>

      {dayTasks.length === 0 ? (
        <p>No tasks available</p>
      ) : (
        <ul>
          {dayTasks.map((task) => (
            <li key={task.id}>
              {task.text}

              <button
                onClick={() =>
                  handleEdit(task)
                }
              >
                Edit
              </button>

              <button
                onClick={() =>
                  deleteTask(
                    selectedDay,
                    task.id
                  )
                }
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

const mapStateToProps = (state) => ({
  selectedDay: state.selectedDay,
  tasks: state.tasks,
});

export default connect(
  mapStateToProps,
  { editTask, deleteTask }
)(TaskList);

import React from "react";
import DatePicker from "./components/DatePicker";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";
import "./App.css";

function App() {
  return (
    <div className="container">
      <h1>Daily Planner</h1>

      <DatePicker />

      <TaskForm />

      <TaskList />
    </div>
  );
}

export default App;

import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import App from "./App";
import store from "./redux/store";

const root =
  ReactDOM.createRoot(
    document.getElementById("root")
  );

root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

body {
  font-family: Arial, sans-serif;
}

.container {
  width: 600px;
  margin: 40px auto;
}