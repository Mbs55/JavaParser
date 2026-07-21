import './App.css'
import {useState} from 'react';
import analyze from './services/api.ts'
import {ProjectDashboard,type ProjectData} from './services/display'

export default function App() {
  const [path,setPath]=useState<string>("");
  const [result,setResult]=useState<ProjectData | null>(null);
  //const [loading,setLoading]=useState<string>("");//Check with it later
  const Analyze=async()=>{
    if(!path) return;
    const res = await analyze(path);
    setResult(res as ProjectData);
  }
  if(result){
    console.log('analyze result', result);
    return (
      <div>
        <ProjectDashboard projectData={result} />
      </div>
    )
  }
  return (
    <div>
      <input type="text" value={path} placeholder="Enter the java path" className="border p-2 rounded" onChange={(e)=>setPath(e.target.value)}/>
      <button onClick={Analyze}>analyze</button>
      <p>Targeting:{path}</p>
      </div>
  )
}
