function fst(myname){
    setTimeout(()=>{
        console.log("first function",myname);
    },2000);
}

function snd(name,callback){
    setTimeout(()=>{
       console.log("second function", name);
    callback(name);
    },1000);
    
}

// function third(city){
//     console.log("third function", city);
// }

snd("Alice", fst);