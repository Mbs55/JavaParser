import {type ProjectData} from './display'
export  async function sendTo(projectPath:string){
    
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
    if(!response.ok){
        throw new Error('Request failed')
    }
    const res=await response.json();
    return res as ProjectData;


}
export  async function analyze(res:ProjectData){
    const analysis=await fetch(
        "http://localhost:8000/AIService/analyze",
        {method:"POST",
            headers:{
            "Content-Type":"application/json"
        },body:JSON.stringify(res)
    },
    )
    const response=await analysis.json();
        console.log(analysis.status)
        console.log(response)
    return response
}