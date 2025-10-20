// Install first:
// npm init -y
// npm install express cors bcrypt jsonwebtoken

const express = require("express");
const cors = require("cors");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const app = express();
app.use(cors());
app.use(express.json());

const SECRET_KEY = "1234";  // use .env in real apps

// Simulated database
const users = [
  {
    email: "test@example.com",
    passwordHash: bcrypt.hashSync("password123", 10) // pre-hashed
  }
];

app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const user = users.find(u => u.email === email);

  if (!user) return res.status(400).json({ message: "User not found" });

  const validPassword = await bcrypt.compare(password, user.passwordHash);
  if (!validPassword) return res.status(401).json({ message: "Invalid password" });

  const token = jwt.sign({ email: user.email }, SECRET_KEY, { expiresIn: "1h" });
  res.json({ token });
});

app.get("/protected", (req, res) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.sendStatus(401);

  const token = authHeader.split(" ")[1];
  jwt.verify(token, SECRET_KEY, (err, user) => {
    if (err) return res.sendStatus(403);
    res.json({ message: `Hello ${user.email}` });
  });
});

app.listen(4000, () => console.log("✅ Server running on port 4000"));
