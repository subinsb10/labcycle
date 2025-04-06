import { Router } from "express";
const route=Router()

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

export default route