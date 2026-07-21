import {ReactFlow,Controls,Background,useNodesState,useEdgesState,MarkerType} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import {useMemo} from 'react';
export interface MethodInfo{
  id:string;
  className:string;
  packageName:string;
  signature:string;
  sourceCode:string;
  annotations:string[];
  outgoingCalls:string[];
  parameters:string[];
  variables:string[];
  beginLine:number;
  endLine:number;
}
export interface ClassInfo{
  
    id:string;
    className:string;
    packageName:string;
    qualifiedName:string;
    sourceCode:string;
    filePath:string;
    beginLine:number;
    endLine:number;
    superClass:string;
    implementedInterfaces:string[];
    methods :string[]
    fields :string[];
    annotations:string[];
    dependencies:string[];
}

export interface ProjectData{
  classes:ClassInfo[];
  methods:MethodInfo[];
}

export interface ProjectDashboardProps {
  projectData: ProjectData;
}

export  function ProjectDashboard({ projectData }: ProjectDashboardProps) {
  if (!projectData) {
    return <div style={{ padding: '20px' }}>No project data available.</div>;
  }

  const {classes=[],methods=[]}=projectData;
  const {initialNodes,initialEdges}=useMemo(()=>{
    const nodes:any[]=[];
    const edges:any[]=[];
    const columns = Math.max(1, Math.ceil(Math.sqrt(methods.length)));
    const xSpacing = 280;
    const ySpacing = 120;
  

    methods.forEach((m,index)=>{
        const nodeId=m.id;
        const x=(index % columns)*xSpacing;
        const y=(Math.floor(index/columns))*ySpacing;
        nodes.push({
        id: nodeId,
        position: { x, y },
        data: { label: `${m.id}` }, 
        sourceCode:m.sourceCode,
        style: {
          color:'red',
          border: '1px solid #1a192b',
          borderRadius: '8px',
          padding: '10px',
          background: '#ffffff',
          fontSize: '12px',
          whiteSpace: 'pre-wrap',
          wordBreak: 'break-all',
        },
      });

      })
      methods.forEach((m)=>{
        m.outgoingCalls.forEach((out,callIndex)=>{
          edges.push({
          id: `e-${m.id}->${out}-${callIndex}`,
          source: m.id,
          target: out,
          animated: true,
          markerEnd: {
            type: MarkerType.ArrowClosed,
          },
        });
        })
        
      })
      return {initialNodes:nodes,initialEdges:edges}},[methods])
  if (methods.length === 0) {
    return <div style={{ padding: '20px' }}>No methods to display.</div>;
  }

  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, , onEdgesChange] = useEdgesState(initialEdges);
  return (
    <div style={{ width: '100%', height: '80vh', border: '1px solid #e2e8f0', borderRadius: '8px' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        fitView
      >
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}
  
  //   <div style={{ fontFamily: 'sans-serif', padding: '24px', maxWidth: '1200px', margin: '0 auto' }}>
  //     <header style={{ marginBottom: '32px', borderBottom: '1px solid #eee', paddingBottom: '16px' }}>
  //       <h1 style={{ margin: '0 0 8px 0' }}>Project Analysis Dashboard</h1>
  //       <p style={{ margin: 0, color: '#666' }}>
  //         Total Classes: <strong>{classes.length}</strong> | Total Methods: <strong>{methods.length}</strong>
  //       </p>
  //     </header>

  //     {/* Classes Section */}
  //     <section style={{ marginBottom: '40px' }}>
  //       <h2 style={{ marginBottom: '16px' }}>Classes ({classes.length})</h2>
  //       {classes.length === 0 ? (
  //         <p style={{ color: '#666', fontStyle: 'italic' }}>No classes found in this project.</p>
  //       ) : (
  //         <div style={{ overflowX: 'auto' }}>
  //           <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
  //             <thead>
  //               <tr style={{ backgroundColor: '#f8f9fa', borderBottom: '2px solid #dee2e6' }}>
  //                 <th style={{ padding: '12px' }}>Class Name</th>
  //                 <th style={{ padding: '12px' }}>Package</th>
  //                 <th style={{ padding: '12px' }}>Superclass</th>
  //                 <th style={{ padding: '12px' }}>Lines</th>
  //                 <th style={{ padding: '12px' }}>File Path</th>
  //               </tr>
  //             </thead>
  //             <tbody>
  //               {classes.map((cls, index) => (
  //                 <tr key={cls.id || index} style={{ borderBottom: '1px solid #dee2e6' }}>
  //                   <td style={{ padding: '12px', fontWeight: 'bold' }}>{cls.className}</td>
  //                   <td style={{ padding: '12px', color: '#555' }}>{cls.packageName || 'default'}</td>
  //                   <td style={{ padding: '12px', color: '#666' }}>{cls.superClass || 'None'}</td>
  //                   <td style={{ padding: '12px' }}>{cls.beginLine} - {cls.endLine}</td>
  //                   <td style={{ padding: '12px', fontSize: '13px', color: '#666', wordBreak: 'break-all' }}>
  //                     {cls.filePath}
  //                   </td>

  //                 </tr>
  //               ))}
  //             </tbody>
  //           </table>
  //         </div>
  //       )}
  //     </section>

  //     {/* Methods Section */}
  //     <section>
  //       <h2 style={{ marginBottom: '16px' }}>Methods ({methods.length})</h2>
  //       {methods.length === 0 ? (
  //         <p style={{ color: '#666', fontStyle: 'italic' }}>No methods found in this project.</p>
  //       ) : (
  //         <div style={{ overflowX: 'auto' }}>
  //           <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
  //             <thead>
  //               <tr style={{ backgroundColor: '#f8f9fa', borderBottom: '2px solid #dee2e6' }}>
  //                 <th style={{ padding: '12px' }}>Method Signature</th>
  //                 <th style={{ padding: '12px' }}>Class Name</th>
  //                 <th style={{ padding: '12px' }}>Package</th>
  //                 <th style={{ padding: '12px' }}>Lines</th>
  //               <th style={{ padding: '12px' }}>outgoing 1</th>

  //               </tr>
  //             </thead>
  //             <tbody>
  //               {methods.map((method, index) => (
  //                 <tr key={method.id || index} style={{ borderBottom: '1px solid #dee2e6' }}>
  //                   <td style={{ padding: '12px', fontFamily: 'monospace', fontSize: '13px', color: '#d63384' }}>
  //                     {method.signature}
  //                   </td>
  //                   <td style={{ padding: '12px' }}>{method.className}</td>
  //                   <td style={{ padding: '12px', color: '#555' }}>{method.packageName || 'default'}</td>
  //                   <td style={{ padding: '12px' }}>{method.beginLine} - {method.endLine}</td>
  //                   <td style={{ padding: '12px' }}>{method.outgoingCalls[0]}</td>
  //                 </tr>
  //               ))}
  //             </tbody>
  //           </table>
  //         </div>
  //       )}
  //     </section>
  //   </div>
