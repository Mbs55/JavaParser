export default async function analyze(projectPath:string){
    
    const response=await fetch(
        "http://localhost:8080/api/v1/Analyze",
        {method:"POST",
            headers:{
            "Content-Type":"application/json"
        },body:JSON.stringify({
            projectPath
        })
    },
    )
    return await response.json();
}