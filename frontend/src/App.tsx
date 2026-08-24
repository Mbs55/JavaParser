import './App.css'
import {useState} from 'react';
import {sendTo,analyze} from './services/api.ts'
import {ProjectDashboard,type ProjectData} from './services/display'

export default function App() {
  const [path,setPath]=useState<string>("");
  const [result,setResult]=useState<ProjectData | null>(null);
  const [analysis,setAnalysis]=useState<any>(null);
  const send=async()=>{
    if(path == "")
      return;
    const res = await sendTo(path);
    setResult(res as ProjectData);
  }
  if(result){
    console.log('analyze result', result)
    
    const Analyze=async()=> {
      const analysis=await analyze(result)
      setAnalysis(analysis)
    }

    return (
      <div>
        <ProjectDashboard projectData={result} />
        <br />
        <div>
          <button onClick={Analyze}>Analyze</button>
        </div>
        
        </div>
        )
  }
  if(analysis){
    return(
      <div>
        {analysis}
      </div>
    )
  }
  return (
    <div>
      <input type="text" value={path} placeholder="Enter the java path" className="border p-2 rounded" onChange={(e)=>setPath(e.target.value)}/>
      <button onClick={send}>Visualize</button>
      <p>Targeting:{path}</p>
      </div>
  )
}
