dailychallenge
mkdir user-management-api
cd user-management-api

npm init -y

npm install express bcrypt

const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static("public"));

const userRoutes = require("./routes/users");

app.use("/", userRoutes);

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
const express = require("express");
const bcrypt = require("bcrypt");
const fs = require("fs");

const router = express.Router();

const FILE_PATH = "./users.json";


// Read users
function readUsers() {
    try {
        const data = fs.readFileSync(FILE_PATH);

        return JSON.parse(data);

    } catch (error) {

        throw new Error("Unable to read users file");
    }
}


// Write users
function writeUsers(users) {
    try {

        fs.writeFileSync(
            FILE_PATH,
            JSON.stringify(users, null, 2)
        );

    } catch (error) {

        throw new Error("Unable to write users file");
    }
}


// =====================
// REGISTER
// =====================
router.post("/register", async (req, res) => {

    try {

        const {
            firstName,
            lastName,
            email,
            username,
            password
        } = req.body;

        if (
            !firstName ||
            !lastName ||
            !email ||
            !username ||
            !password
        ) {
            return res.status(400).json({
                message: "All fields are required"
            });
        }

        const users = readUsers();

        const existingUser = users.find(
            user =>
                user.username === username ||
                user.password === password
        );

        if (existingUser) {

            return res.status(400).json({
                message:
                    "Username or password already exists"
            });
        }

        const hashedPassword =
            await bcrypt.hash(password, 10);

        const newUser = {
            id: users.length + 1,
            firstName,
            lastName,
            email,
            username,
            password: hashedPassword
        };

        users.push(newUser);

        writeUsers(users);

        res.status(201).json({
            message: "User registered successfully"
        });

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =====================
// LOGIN
// =====================
router.post("/login", async (req, res) => {

    try {

        const { username, password } = req.body;

        const users = readUsers();

        const user = users.find(
            user => user.username === username
        );

        if (!user) {

            return res.status(401).json({
                message:
                    "Username or password incorrect"
            });
        }

        const validPassword =
            await bcrypt.compare(
                password,
                user.password
            );

        if (!validPassword) {

            return res.status(401).json({
                message:
                    "Username or password incorrect"
            });
        }

        res.status(200).json({
            message: "Login successful"
        });

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =====================
// GET ALL USERS
// =====================
router.get("/users", (req, res) => {

    try {

        const users = readUsers();

        res.json(users);

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});


// =====================
// GET USER BY ID
// =====================
router.get("/users/:id", (req, res) => {

    const users = readUsers();

    const user = users.find(
        user => user.id === Number(req.params.id)
    );

    if (!user) {

        return res.status(404).json({
            message: "User not found"
        });
    }

    res.json(user);
});


// =====================
// UPDATE USER
// =====================
router.put("/users/:id", async (req, res) => {

    try {

        const users = readUsers();

        const user = users.find(
            user => user.id === Number(req.params.id)
        );

        if (!user) {

            return res.status(404).json({
                message: "User not found"
            });
        }

        user.firstName =
            req.body.firstName || user.firstName;

        user.lastName =
            req.body.lastName || user.lastName;

        user.email =
            req.body.email || user.email;

        user.username =
            req.body.username || user.username;

        if (req.body.password) {

            user.password =
                await bcrypt.hash(
                    req.body.password,
                    10
                );
        }

        writeUsers(users);

        res.json({
            message: "User updated successfully",
            user
        });

    } catch (error) {

        res.status(500).json({
            message: error.message
        });
    }
});

module.exports = router;

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>

<h1>Register</h1>

<form action="/register" method="POST">

<input type="text"
name="firstName"
placeholder="First Name"
required>

<br><br>

<input type="text"
name="lastName"
placeholder="Last Name"
required>

<br><br>

<input type="email"
name="email"
placeholder="Email"
required>

<br><br>

<input type="text"
name="username"
placeholder="Username"
required>

<br><br>

<input type="password"
name="password"
placeholder="Password"
required>

<br><br>

<button id="registerBtn" disabled>
Register
</button>

</form>

<script>

const inputs =
document.querySelectorAll("input");

const button =
document.getElementById("registerBtn");

inputs.forEach(input => {

    input.addEventListener("input", () => {

        const filled =
        [...inputs].every(
        input => input.value.trim() !== ""
        );

        button.disabled = !filled;

    });

});

</script>

</body>
</html>

node server.js
