const express = require('express');
const fs = require('fs/promises');
const path = require('path');
const router = express.Router();

const DATA_PATH = path.join(__dirname, 'tasks.json');

// Helper to read tasks
async function readTasks() {
    const data = await fs.readFile(DATA_PATH, 'utf8');
    return JSON.parse(data);
}

// Helper to write tasks
async function writeTasks(tasks) {
    await fs.writeFile(DATA_PATH, JSON.stringify(tasks, null, 2));
}

// GET /tasks - Retrieve all
router.get('/', async (req, res) => {
    try {
        const tasks = await readTasks();
        res.json(tasks);
    } catch (error) {
        res.status(500).json({ message: "Error reading tasks" });
    }
});

// GET /tasks/:id - Retrieve specific task
router.get('/:id', async (req, res) => {
    try {
        const tasks = await readTasks();
        const task = tasks.find(t => t.id === parseInt(req.params.id));
        if (!task) return res.status(404).json({ message: "Task not found" });
        res.json(task);
    } catch (error) {
        res.status(500).json({ message: "Error retrieving task" });
    }
});

// POST /tasks - Create new task
router.post('/', async (req, res) => {
    const { title, description } = req.body;
    if (!title) return res.status(400).json({ message: "Title is required" });

    try {
        const tasks = await readTasks();
        const newTask = {
            id: tasks.length > 0 ? tasks[tasks.length - 1].id + 1 : 1,
            title,
            description: description || "",
            completed: false
        };
        tasks.push(newTask);
        await writeTasks(tasks);
        res.status(201).json(newTask);
    } catch (error) {
        res.status(500).json({ message: "Error saving task" });
    }
});

// PUT /tasks/:id - Update task
router.put('/:id', async (req, res) => {
    const { title, description, completed } = req.body;
    try {
        const tasks = await readTasks();
        const index = tasks.findIndex(t => t.id === parseInt(req.params.id));
        
        if (index === -1) return res.status(404).json({ message: "Task not found" });

        tasks[index] = { 
            ...tasks[index], 
            title: title || tasks[index].title,
            description: description || tasks[index].description,
            completed: completed !== undefined ? completed : tasks[index].completed 
        };

        await writeTasks(tasks);
        res.json(tasks[index]);
    } catch (error) {
        res.status(500).json({ message: "Error updating task" });
    }
});

// DELETE /tasks/:id - Remove task
router.delete('/:id', async (req, res) => {
    try {
        const tasks = await readTasks();
        const newTasks = tasks.filter(t => t.id !== parseInt(req.params.id));
        
        if (tasks.length === newTasks.length) {
            return res.status(404).json({ message: "Task not found" });
        }

        await writeTasks(newTasks);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: "Error deleting task" });
    }
});

module.exports = router;

const express = require('express');
const taskRouter = require('./tasks.router');

const app = express();
const PORT = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Routes
app.use('/tasks', taskRouter);

// Global Error Handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});