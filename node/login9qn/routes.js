import { Router } from "express";
import mongoose from "mongoose";
const route=Router()


mongoose.connect('mongodb://127.0.0.1:27017/registration')
.then(()=> console.log("mongodb connected...."))
.catch(err=> console.error("mongodb connection error", err))

const db = mongoose.connection
const user = db.collection('user')

route.get('/',(req,res)=>{
    try{
        res.sendFile('index.html',{root: './public'});
        res.status(200).json({message:"hi"})
    }catch(error){
        console.error(error)
        res.status(500).json({error:"error occured"})
    }
})

route.get('/register',(req,res)=>{
    try{
        res.sendFile('register.html',{root: './public'})
    }catch(error){
        console.error(error)
        res.status(500).json({error:"error occured"})

    }
})

route.get('/login',(req,res)=>{
    try{
        res.sendFile('login.html',{root: './public'})
    }catch(error){
        console.error(error)
        res.status(500).json({error:"error occured in login"})
    }
})


function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

route.post('/register', (req, res) => {
  console.log('hi');

  const { name, email, password } = req.body;

  // Check if body exists
  if (!name || !email || !password) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  // Validate email format
  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email format' });
  }

  const newUser = { name, email, password };
  console.log(newUser);

  user.insertOne(newUser)
    .then(result => {
      console.log('User registered:', result);
      res.status(201).json({ message: 'User registered successfully' });
    })
    .catch(err => {
      console.error('Error registering user:', err);
      res.status(500).json({ error: 'Internal Server Error' });
    });
});

  
route.post('/user', (req, res) => {  
    console.log("hi")
    const { email, password } = req.body;
    user.findOne({ email, password })
      .then(user => {
        if (user) {
          res.status(200).json({ message: 'Login successful' });
        } else {
          res.status(401).json({ error: 'Invalid email or password' });
        }
      })
      .catch(err => {
        console.error('Error logging in:', err);
        res.status(500).json({ error: 'Internal Server Error' });
      });
  })

export default route