const express = require('express');
const mongoose = require('mongoose');


const app = express();

app.use(express.json());

mongoose.connect('mongodb://127.0.0.1:27017/studentdb', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));


const studentSchema = new mongoose.Schema({
  name: String,
  age: Number,
  grade: String
});


const Student = mongoose.model('Student', studentSchema);

// {
//     "name": "sb Doe",
//     "age": 21,
//     "grade": "B"
//   }


app.post('/students', async (req, res) => {
  const { name, age, grade } = req.body;
  const newStudent = new Student({ name, age, grade });
  try {
    await newStudent.save();
    res.status(201).json(newStudent);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


app.get('/students', async (req, res) => {
  try {
    const students = await Student.find();
    res.status(200).json(students);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


app.get('/students/:id', async (req, res) => {
  try {
    const student = await Student.findById(req.params.id);
    if (student) {
      res.status(200).json(student);
    } else {
      res.status(404).json({ message: 'Student not found' });
    }
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Update a student by ID  http://localhost:3000/students/67f2a4b0fa4b0f92895b15f9
app.put('/students/:id', async (req, res) => {
  try {
    const student = await Student.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (student) {
      res.status(200).json(student);
    } else {
      res.status(404).json({ message: 'Student not found' });
    }
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


app.delete('/students/:id', async (req, res) => {
  try {
    const student = await Student.findByIdAndDelete(req.params.id);
    if (student) {
      res.status(200).json({ message: 'Student deleted' });
    } else {
      res.status(404).json({ message: 'Student not found' });
    }
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
