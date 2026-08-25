import './App.css'
import {useState} from 'react';
import {sendTo,analyze} from './services/api.ts'
import {ProjectDashboard,AnalysisDashboard,type ProjectData,type AnalyzeResponse} from './services/display'

export default function App() {
  const [path,setPath]=useState<string>("");
  const [result,setResult]=useState<ProjectData | null>(null);
  const [analysis,setAnalysis]=useState<AnalyzeResponse[] | null>(null);
  const send=async()=>{
    if(path == "")
      return;
    const res = await sendTo(path);
    setResult(res as ProjectData);
  }

    const Analyze=async()=> {
      if(!result)
      return;
      try{
      const analysis=await analyze(result)
      setAnalysis(analysis as AnalyzeResponse[]);}
      catch(error){
        console.error("Analysis failed:",error)
      }
    
    }
    if(analysis){
        return (
      <div>

        <AnalysisDashboard analysis={analysis} />

      </div>
    );
      }
    if(result){
            return (
      <div>
        <ProjectDashboard projectData={result} />
        <br />
        <div>
          <button onClick={Analyze}>Analyze</button>
        </div>
        
        </div>
        );
      }
   return (
    <div>

      <input
        type="text"
        value={path}
        placeholder="Enter the java path"
        className="border p-2 rounded"
        onChange={(e) => setPath(e.target.value)}
      />

      <button onClick={send}>
        Visualize
      </button>

      <p>
        Targeting: {path}
      </p>

    </div>
  ); 
  }
   



