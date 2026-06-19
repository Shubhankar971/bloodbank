const express=require("express");

const router=express.Router();

router.post("/donor-ai",(req,res)=>{


const data=req.body;


res.json({

message:"AI donor matching activated",
data:data

});


});

module.exports=router;
