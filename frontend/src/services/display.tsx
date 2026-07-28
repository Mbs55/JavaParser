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

type NodeType =
  | 'CLASS'
  | 'METHOD'
  | 'INTERFACE'
  | 'ANNOTATION'
  | 'FIELD'
  | 'PARAMETER'
  | 'VARIABLE';

const typeStyles: Record<NodeType, { background: string; color: string; border: string }> = {
  CLASS: { background: '#2563eb', color: '#ffffff', border: '1px solid #1e40af' },
  METHOD: { background: '#dc2626', color: '#ffffff', border: '1px solid #991b1b' },
  INTERFACE: { background: '#7c3aed', color: '#ffffff', border: '1px solid #5b21b6' },
  ANNOTATION: { background: '#fde68a', color: '#111827', border: '1px solid #d97706' },
  FIELD: { background: '#10b981', color: '#ffffff', border: '1px solid #047857' },
  PARAMETER: { background: '#f97316', color: '#ffffff', border: '1px solid #c2410c' },
  VARIABLE: { background: '#6b7280', color: '#ffffff', border: '1px solid #374151' },
};

const typeLabels: Record<NodeType, string> = {
  CLASS: 'Class',
  METHOD: 'Method',
  INTERFACE: 'Interface',
  ANNOTATION: 'Annotation',
  FIELD: 'Field',
  PARAMETER: 'Parameter',
  VARIABLE: 'Variable',
};

export function ProjectDashboard({ projectData }: ProjectDashboardProps) {
  if (!projectData) {
    return <div style={{ padding: '20px' }}>No project data available.</div>;
  }

  const { classes = [], methods = [] } = projectData;

  const { initialNodes, initialEdges } = useMemo(() => {
    const nodes: any[] = [];
    const edges: any[] = [];
    const createdNodes = new Set<string>();
    const edgeIds = new Set<string>();

    const xSpacing = 220;
    const ySpacing = 110; 
    const clusterGap = 160; 

    const addNode = (
      id: string,
      type: NodeType,
      name: string,
      x: number,
      y: number
    ) => {
      if (createdNodes.has(id)) return;

      const style = typeStyles[type];

      nodes.push({
        id,
        position: { x, y },
        data: { label: `${typeLabels[type]}\n${name}` },
        style: {
          background: style.background,
          color: style.color,
          border: style.border,
          borderRadius: '8px',
          padding: '10px',
          fontSize: '12px',
          whiteSpace: 'pre-wrap',
          wordBreak: 'break-word',
          textAlign: 'center' as const,
          minWidth: '140px',
        },
      });

      createdNodes.add(id);
    };

    const addEdge = (source: string, target: string, label: string) => {
      const id = `${source}-${label}-${target}`;
      if (edgeIds.has(id)) return;
      edgeIds.add(id);

      edges.push({
        id,
        source,
        target,
        label,
        animated: label === 'CALLS',
        style: label === 'CALLS' ? { stroke: '#dc2626' } : undefined,
        markerEnd: {
          type: MarkerType.ArrowClosed,
        },
      });
    };
    let clusterStartX = 0;

    classes.forEach((cls) => {
      const clsMethods = methods.filter((m) => m.className === cls.className);

      // Width needed to fit the widest row of parameters/variables under any method
      const methodContentSlots = clsMethods.reduce((max, m) => {
        const w = Math.max(m.parameters.length, m.variables.length, 1);
        return Math.max(max, w);
      }, 1);

      const annotationSlots = Math.max(cls.annotations.length, 1);
      const contentSlots = Math.max(methodContentSlots, annotationSlots, 1);
      const contentWidth = contentSlots * xSpacing;

      const hasFields = cls.fields.length > 0;
      const hasInterfaces = cls.implementedInterfaces.length > 0;

      const leftMargin = hasFields ? xSpacing : 0;
      const rightMargin = hasInterfaces ? xSpacing : 0;

      const classCenterX = clusterStartX + leftMargin + contentWidth / 2;
      const baseY = 0;

      addNode(cls.id, 'CLASS', cls.className, classCenterX, baseY);

      if (cls.superClass) {
        const superId = `class:${cls.superClass}`;
        addNode(superId, 'CLASS', cls.superClass, classCenterX, baseY - ySpacing);
        addEdge(cls.id, superId, 'EXTENDS');
      }


      const annCount = cls.annotations.length;
      cls.annotations.forEach((ann, i) => {
        const annId = `annotation:${ann}`;
        const offset = (i - (annCount - 1) / 2) * xSpacing;
        addNode(annId, 'ANNOTATION', ann, classCenterX + offset, baseY - 2 * ySpacing);
        addEdge(cls.id, annId, 'ANNOTATED_WITH');
      });

      cls.implementedInterfaces.forEach((inter, i) => {
        const interId = `interface:${inter}`;
        addNode(
          interId,
          'INTERFACE',
          inter,
          classCenterX + contentWidth / 2 + xSpacing,
          baseY + i * ySpacing * 0.8
        );
        addEdge(cls.id, interId, 'IMPLEMENTS');
      });

      
      cls.fields.forEach((field, i) => {
        const fieldId = `field:${cls.id}:${field}`;
        addNode(
          fieldId,
          'FIELD',
          field,
          classCenterX - contentWidth / 2 - xSpacing,
          baseY + i * ySpacing * 0.8
        );
        addEdge(cls.id, fieldId, 'HAS_FIELD');
      });

      let yCursor = baseY + ySpacing * 1.6;

      clsMethods.forEach((m) => {
        addNode(m.id, 'METHOD', m.signature, classCenterX, yCursor);
        addEdge(cls.id, m.id, 'DECLARES');
        yCursor += ySpacing;

        if (m.parameters.length > 0) {
          const pCount = m.parameters.length;
          m.parameters.forEach((param, i) => {
            const paramId = `param:${m.id}:${param}`;
            const offset = (i - (pCount - 1) / 2) * xSpacing;
            addNode(paramId, 'PARAMETER', param, classCenterX + offset, yCursor);
            addEdge(m.id, paramId, 'HAS_PARAMETER');
          });
          yCursor += ySpacing * 0.85;
        }

        if (m.variables.length > 0) {
          const vCount = m.variables.length;
          m.variables.forEach((v, i) => {
            const varId = `var:${m.id}:${v}`;
            const offset = (i - (vCount - 1) / 2) * xSpacing;
            addNode(varId, 'VARIABLE', v, classCenterX + offset, yCursor);
            addEdge(m.id, varId, 'DECLARES_VARIABLE');
          });
          yCursor += ySpacing * 0.85;
        }

        m.annotations.forEach((ann) => {
          const annId = `annotation:${ann}`;
          addNode(annId, 'ANNOTATION', ann, classCenterX, yCursor);
          addEdge(m.id, annId, 'ANNOTATED_WITH');
          yCursor += ySpacing * 0.7;
        });

        yCursor += ySpacing * 0.4;
      });

      const clusterWidth = leftMargin + contentWidth + rightMargin;
      clusterStartX += clusterWidth + clusterGap;
    });
    methods.forEach((m) => {
      m.outgoingCalls.forEach((out) => {
        if (!createdNodes.has(out)) {
          
          const callerNode = nodes.find((n) => n.id === m.id);
          const x = callerNode ? callerNode.position.x + xSpacing : 0;
          const y = callerNode ? callerNode.position.y + ySpacing : 0;
          addNode(out, 'METHOD', out, x, y);
        }
        addEdge(m.id, out, 'CALLS');
      });
    });

    return { initialNodes: nodes, initialEdges: edges };
  }, [classes, methods]);

  if (methods.length === 0 && classes.length === 0) {
    return <div style={{ padding: '20px' }}>No project data to display.</div>;
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