import { Router } from "express";
import mongoose from "mongoose";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
const JWT_SECRET = '1234';
const route=Router()


mongoose.connect('mongodb://127.0.0.1:27017/registrationjwt')
.then(()=> console.log("mongodb connected...."))
.catch(err=> console.error("mongodb connection error", err))

const db = mongoose.connection
const user = db.collection('user')



function verifyToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; 

  if (!token) return res.status(401).json({ error: 'Access Denied' });

  try {
    const verified = jwt.verify(token, JWT_SECRET);
    req.user = verified; 
    next();
  } catch (err) {
    res.status(403).json({ error: 'Invalid Token' });
  }
}

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

route.get('/dashboard',(req,res)=>{
  try{
      res.sendFile('dashboard.html',{root: './public'});
  }catch(error){
      console.error(error)
      res.status(500).json({error:"error occured"})
  }
})

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

route.post('/register',async (req, res) => {
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
  const hashedPassword = await bcrypt.hash(password, 10);

  const newUser = { name, email, password:hashedPassword };
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
  console.log("Login request received");

  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required' });
  }

  user.findOne({ email })
    .then(foundUser => {
      if (!foundUser) {
        return res.status(401).json({ error: 'Invalid email or password' });
      }

      bcrypt.compare(password, foundUser.password)
        .then(isMatch => {
          if (isMatch) {
           
            const token = jwt.sign(
              { id: foundUser._id, email: foundUser.email },
              JWT_SECRET,
              { expiresIn: '1h' } // token expires in 1 hour
            );

            res.status(200).json({ message: 'Login successful', token });

          } else {
            res.status(401).json({ error: 'Invalid email or password' });
          }
        })
        .catch(err => {
          console.error('Error comparing password:', err);
          res.status(500).json({ error: 'Internal Server Error' });
        });
    })
    .catch(err => {
      console.error('Error logging in:', err);
      res.status(500).json({ error: 'Internal Server Error' });
    });
});


export default route