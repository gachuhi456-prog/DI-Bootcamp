exercise
mkdir task-manager-api
cd task-manager-api

npm init -y
npm install express

[]

const express = require("express");

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());

// Import routes
const taskRoutes = require("./routes/tasks");

// Use router
app.use("/tasks", taskRoutes);

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

const express = require("express");
const fs = require("fs");

const router = express.Router();

const FILE_PATH = "./tasks.json";


// Read tasks from file
function readTasks() {
    try {
        const data = fs.readFileSync(FILE_PATH);

        return JSON.parse(data);
    } catch (error) {
        throw new Error("Error reading file");
    }
}


// Write tasks to file
function writeTasks(tasks) {
    try {
        fs.writeFileSync(
            FILE_PATH,
            JSON.stringify(tasks, null, 2)
        );
    } catch (error) {
        throw new Error("Error writing file");
    }
}


// =========================
// GET all tasks
// =========================
router.get("/", (req, res) => {
    try {
        const tasks = readTasks();

        res.status(200).json(tasks);

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =========================
// GET task by ID
// =========================
router.get("/:id", (req, res) => {

    try {

        const tasks = readTasks();

        const task = tasks.find(
            task => task.id === Number(req.params.id)
        );

        if (!task) {
            return res.status(404).json({
                message: "Task not found"
            });
        }

        res.status(200).json(task);

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =========================
// CREATE task
// =========================
router.post("/", (req, res) => {

    try {

        const { title } = req.body;

        if (!title) {
            return res.status(400).json({
                message: "Title is required"
            });
        }

        const tasks = readTasks();

        const newTask = {
            id: tasks.length + 1,
            title,
            completed: false
        };

        tasks.push(newTask);

        writeTasks(tasks);

        res.status(201).json({
            message: "Task created successfully",
            task: newTask
        });

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =========================
// UPDATE task
// =========================
router.put("/:id", (req, res) => {

    try {

        const { title, completed } = req.body;

        if (title === undefined && completed === undefined) {
            return res.status(400).json({
                message: "Provide title or completed status"
            });
        }

        const tasks = readTasks();

        const task = tasks.find(
            task => task.id === Number(req.params.id)
        );

        if (!task) {
            return res.status(404).json({
                message: "Task not found"
            });
        }

        if (title !== undefined) {
            task.title = title;
        }

        if (completed !== undefined) {
            task.completed = completed;
        }

        writeTasks(tasks);

        res.status(200).json({
            message: "Task updated successfully",
            task
        });

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =========================
// DELETE task
// =========================
router.delete("/:id", (req, res) => {

    try {

        let tasks = readTasks();

        const task = tasks.find(
            task => task.id === Number(req.params.id)
        );

        if (!task) {
            return res.status(404).json({
                message: "Task not found"
            });
        }

        tasks = tasks.filter(
            task => task.id !== Number(req.params.id)
        );

        writeTasks(tasks);

        res.status(200).json({
            message: "Task deleted successfully"
        });

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});

module.exports = router;