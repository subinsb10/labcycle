const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://127.0.0.1:27017/todoApp', {
});

// Mongoose schema and model
const TodoSchema = new mongoose.Schema({
  text: String,
  completed: Boolean
});

const Todo = mongoose.model('Todo', TodoSchema);

// Create a new todo
app.post('/todos', async (req, res) => {
  const todo = new Todo({ text: req.body.text, completed: false });
  await todo.save();
  res.json(todo);
});

// Get all todos with optional filter
app.get('/todos', async (req, res) => {
  const filter = req.query.filter;
  let todos;

  if (filter === 'completed') {
    todos = await Todo.find({ completed: true });
  } else if (filter === 'pending') {
    todos = await Todo.find({ completed: false });
  } else {
    todos = await Todo.find();
  }

  res.json(todos);
});

// Toggle completed status
app.put('/todos/:id', async (req, res) => {
  const todo = await Todo.findById(req.params.id);
  if (!todo) return res.status(404).json({ error: 'Todo not found' });

  todo.completed = !todo.completed;
  await todo.save();
  res.json(todo);
});

// Delete a todo
app.delete('/todos/:id', async (req, res) => {
  await Todo.findByIdAndDelete(req.params.id);
  res.json({ message: 'Todo deleted' });
});

// Start the server
app.listen(3000, () => {
  console.log(' Server started on http://localhost:3000');
});

