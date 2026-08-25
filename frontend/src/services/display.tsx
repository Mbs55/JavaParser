import {ReactFlow,Controls,Background,useNodesState,useEdgesState,MarkerType} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import {useMemo,useCallback,useState} from 'react';
import { Search, ChevronDown, ShieldAlert, ShieldCheck, X, Terminal } from "lucide-react";
export const ENTRYPOINT_SCOPE_ID = 'entrypoint:scope';
 
export interface MethodInfo {
    id: string;
    
    name: string;
    signature: string;
    qualifiedSignature: string;
    
    className: string;
    packageName: string;
    filePath: string;
    beginLine: number;
    endLine: number;

    sourceCode: string;

    returnType: string;
    genericTypes: string[];
    thrownExceptions: string[];
    visibility: string;

    isStatic: boolean;
    isFinal: boolean;
    isAbstract: boolean;
    isSynchronized: boolean;
    isNative: boolean;
    annotations: string[];
    outgoingCalls: string[];
    incomingCalls:string[];
    parameters: string[];
    variables: string[];
    isConstructor: boolean;
    containsLambda: boolean;
    endpoint: string;
    httpMethod: string;
    isEntryPoint: boolean;


}
export interface ClassInfo {

    id: string;

    className: string;
    qualifiedName: string;
    packageName: string;

    filePath: string;
    beginLine: number;
    endLine: number;
    sourceCode: string;
    isClass:boolean
    isInterface: boolean;
    isEnum: boolean;
    isRecord: boolean;
    visibility: string;
    
    isAbstract: boolean;
    isFinal: boolean;

    superClass: string;

    implementedInterfaces: string[];
    constructors: string[];
    methods: string[];
    fields: string[];
    annotations: string[];
    imports: string[];
    dependencies: string[];
    genericTypes: string[];



    
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
  | 'VARIABLE'
  | 'IMPORT'
  | 'TYPE'
  | 'EXCEPTION'
  | 'GENERIC' 
  | 'VISIBILITY'
  | 'ENTRYPOINT';

const typeStyles: Record<NodeType, { background: string; color: string; border: string }> = {
  CLASS: { background: '#2563eb', color: '#ffffff', border: '1px solid #1e40af' },
  METHOD: { background: '#dc2626', color: '#ffffff', border: '1px solid #991b1b' },
  INTERFACE: { background: '#7c3aed', color: '#ffffff', border: '1px solid #5b21b6' },
  ANNOTATION: { background: '#fde68a', color: '#111827', border: '1px solid #d97706' },
  FIELD: { background: '#10b981', color: '#ffffff', border: '1px solid #047857' },
  PARAMETER: { background: '#f97316', color: '#ffffff', border: '1px solid #c2410c' },
  VARIABLE: { background: '#6b7280', color: '#ffffff', border: '1px solid #374151' },
  IMPORT: {
    background:'#0ea5e9',
    color:'#fff',
    border:'1px solid #0369a1'
},

TYPE:{
    background:'#14b8a6',
    color:'#fff',
    border:'1px solid #0f766e'
},

EXCEPTION:{
    background:'#ef4444',
    color:'#fff',
    border:'1px solid #991b1b'
},

GENERIC:{
    background:'#8b5cf6',
    color:'#fff',
    border:'1px solid #6d28d9'
},

VISIBILITY:{
    background:'#475569',
    color:'#fff',
    border:'1px solid #1e293b'
},
ENTRYPOINT:{
    background: '#f59e0b',
    color: '#111827',
    border: '1px solid #b45309'
},
};

const typeLabels: Record<NodeType, string> = {
  CLASS: 'Class',
  METHOD: 'Method',
  INTERFACE: 'Interface',
  ANNOTATION: 'Annotation',
  FIELD: 'Field',
  PARAMETER: 'Parameter',
  VARIABLE: 'Variable',
  IMPORT:"Import",
  TYPE:"Type",
  EXCEPTION:"Exception",
  GENERIC:"Generic",
  VISIBILITY:"Visibility",
  ENTRYPOINT:"Entrypoint",
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
    const entrypointScopeId = 'entrypoint:scope';
    addNode(entrypointScopeId, 'ENTRYPOINT', 'Entrypoint Scope', 0, -2 * ySpacing);

    classes.forEach((cls) => {
      const clsMethods = methods.filter((m) => m.className === cls.className);

      
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
      cls.imports.forEach((imp,i)=>{
    const id=`import:${imp}`;
    addNode(id,"IMPORT",imp,classCenterX+contentWidth/2+2*xSpacing,baseY+i*60);
    addEdge(cls.id,id,"IMPORTS");
    });
    const visId=`visibility:${cls.visibility}`;
addNode(visId,"VISIBILITY",cls.visibility,classCenterX,baseY-ySpacing);
addEdge(cls.id,visId,"HAS_VISIBILITY");
cls.genericTypes.forEach((g,i)=>{
    const id=`generic:${g}`;
    addNode(id,"GENERIC",g,classCenterX-contentWidth/2-xSpacing,baseY-2*ySpacing-i*60);
    addEdge(cls.id,id,"HAS_GENERIC");
  });
let yCursor = baseY + ySpacing * 1.6;
cls.constructors.forEach((c,i)=>{
    const id=`ctor:${c}`;
    addNode(id,"METHOD",c,classCenterX+contentWidth/2+xSpacing,yCursor+i*60);
    addEdge(cls.id,id,"DECLARES_CONSTRUCTOR");
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


      clsMethods.forEach((m) => {
        const methodLabel = `${m.signature}${m.isEntryPoint ? `\n[${m.httpMethod || 'HTTP'}] ${m.endpoint || ''}` : ''}`;
        addNode(m.id, 'METHOD', methodLabel, classCenterX, yCursor);
        addEdge(cls.id, m.id, 'DECLARES');
        if (m.isEntryPoint) {
          addEdge(entrypointScopeId, m.id, 'ENTRYPOINT');
        }
        yCursor += ySpacing;
        const typeId=`type:${m.returnType}`;
        addNode(typeId,"TYPE",m.returnType,classCenterX+xSpacing,yCursor);
        addEdge(m.id,typeId,"RETURNS");
        const visId=`visibility:${m.visibility}`;
addNode(visId,"VISIBILITY",m.visibility,classCenterX-xSpacing,yCursor);
addEdge(m.id,visId,"HAS_VISIBILITY");
m.genericTypes.forEach((g,i)=>{
    const id=`generic:${g}`;
    addNode(id,"GENERIC",g,classCenterX+(i+1)*100,yCursor-ySpacing);
    addEdge(m.id,id,"HAS_GENERIC");
});
m.thrownExceptions.forEach((e,i)=>{
    const id=`exception:${e}`;
    addNode(id,"EXCEPTION",e,classCenterX+(i+1)*110,yCursor+ySpacing);
    addEdge(m.id,id,"THROWS");
});

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
      m.incomingCalls.forEach((incoming) => {
        if (!createdNodes.has(incoming)) {
          const callerNode = nodes.find((n) => n.id === m.id);
          const x = callerNode ? callerNode.position.x - xSpacing : 0;
          const y = callerNode ? callerNode.position.y + ySpacing : 0;
          addNode(incoming, 'METHOD', incoming, x, y);
        }
        addEdge(m.id, incoming, 'CALLED_BY');
      });

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

  const onInit = useCallback((instance: any) => {
    const firstClassNode = initialNodes.find((node) => node.id === classes[0]?.id);
    const targetNode = firstClassNode ?? initialNodes.find((node) => node.id === ENTRYPOINT_SCOPE_ID);

    if (targetNode && instance?.setCenter) {
      instance.setCenter(targetNode.position.x, targetNode.position.y, {
        zoom: 0.65,
        duration: 0,
      });
    }

    if (instance?.fitView) {
      instance.fitView({
        padding: 0.2,
        maxZoom: 0.7,
        duration: 0,
      });
    }
  }, [classes, initialNodes]);

  return (
    <div style={{ width: '100vw', height: '100vh', margin: 0, padding: 0, overflow: 'hidden' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onInit={onInit}
        fitView
        fitViewOptions={{ padding: 0.2, maxZoom: 0.7 }}
        minZoom={0.2}
        maxZoom={1.2}
      >
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}



export interface Vulnerability {
  type: string;
  severity: string;
  cwe: string;
  line: number;
  description: string;
  recommendation: string;
}

export interface AnalyzeResponse {
  methodName: string;
  methodId: string;
  methodPackage: string;
  className: string;
  status: "SAFE" | "VULNERABLE";
  overall_risk: "CRITICAL" | "HIGH" | "MEDIUM" | "LOW";
  confidence: number;
  summary: string;
  vulnerabilities: Vulnerability[];
}

interface AnalysisDashboardProps {
  analysis: AnalyzeResponse[];
}


const COLORS = {
  bg: "#0B0E14",
  surface: "#12151E",
  surfaceRaised: "#171B26",
  border: "#232838",
  borderLight: "#2E3446",
  text: "#E8EAF2",
  muted: "#8992A8",
  faint: "#535B70",
  critical: "#FF4365",
  high: "#FF9D42",
  medium: "#FFD166",
  low: "#5FD9B4",
  safe: "#3ED598",
  criticalTint: "rgba(255,67,101,0.12)",
  highTint: "rgba(255,157,66,0.12)",
  mediumTint: "rgba(255,209,102,0.12)",
  lowTint: "rgba(95,217,180,0.12)",
  safeTint: "rgba(62,213,152,0.12)",
} as const;

const SEVERITY_ORDER = ["CRITICAL", "HIGH", "MEDIUM", "LOW"] as const;
type Sev = (typeof SEVERITY_ORDER)[number];
const SEVERITY_COLOR: Record<Sev, string> = { CRITICAL: COLORS.critical, HIGH: COLORS.high, MEDIUM: COLORS.medium, LOW: COLORS.low };
const SEVERITY_TINT: Record<Sev, string> = { CRITICAL: COLORS.criticalTint, HIGH: COLORS.highTint, MEDIUM: COLORS.mediumTint, LOW: COLORS.lowTint };
const SEVERITY_RANK: Record<Sev, number> = { CRITICAL: 4, HIGH: 3, MEDIUM: 2, LOW: 1 };

const FONTS = {
  mono: "'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace",
  sans: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif",
};

const norm = (s: string) => (s || "").toUpperCase() as Sev;

function methodRank(m: AnalyzeResponse): number {
  if (!m.vulnerabilities.length) return 0;
  return Math.max(...m.vulnerabilities.map((v) => SEVERITY_RANK[norm(v.severity)] || 0));
}

export function AnalysisDashboard({ analysis }: AnalysisDashboardProps) {
  const [query, setQuery] = useState("");
  const [severityFilter, setSeverityFilter] = useState<Sev | "ALL">("ALL");
  const [statusFilter, setStatusFilter] = useState<"ALL" | "VULNERABLE" | "SAFE">("ALL");
  const [expanded, setExpanded] = useState<Set<string>>(() => new Set());

  const stats = useMemo(() => {
    const vulns = analysis.flatMap((m) => m.vulnerabilities);
    const counts: Record<Sev, number> = { CRITICAL: 0, HIGH: 0, MEDIUM: 0, LOW: 0 };
    vulns.forEach((v) => {
      const sev = norm(v.severity);
      if (counts[sev] !== undefined) counts[sev] += 1;
    });
    const vulnerable = analysis.filter((m) => m.status === "VULNERABLE").length;
    return {
      total: analysis.length,
      vulnerable,
      safe: analysis.length - vulnerable,
      totalVulns: vulns.length,
      counts,
    };
  }, [analysis]);

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return analysis
      .filter((m) => {
        if (statusFilter !== "ALL" && m.status !== statusFilter) return false;
        if (severityFilter !== "ALL" && !m.vulnerabilities.some((v) => norm(v.severity) === severityFilter)) return false;
        if (q && !`${m.methodName} ${m.className} ${m.methodPackage}`.toLowerCase().includes(q)) return false;
        return true;
      })
      .sort((a, b) => methodRank(b) - methodRank(a) || b.confidence - a.confidence);
  }, [analysis, query, severityFilter, statusFilter]);

  const toggle = (id: string) =>
    setExpanded((prev) => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });

  const dateStr = new Date().toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });

  return (
    <div style={{ background: COLORS.bg, color: COLORS.text, fontFamily: FONTS.sans, minHeight: "100%" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
        .ad-chip { transition: background-color 150ms ease, color 150ms ease, border-color 150ms ease; }
        .ad-card { transition: border-color 150ms ease; }
        .ad-card:hover { border-color: ${COLORS.borderLight}; }
        .ad-chev { transition: transform 180ms ease; }
        .ad-input::placeholder { color: ${COLORS.faint}; }
        .ad-input:focus { outline: none; border-color: ${COLORS.borderLight}; }
      `}</style>

      <div style={{ maxWidth: "980px", margin: "0 auto", padding: "40px 24px" }}>
        {/* Header */}
        <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: "16px", marginBottom: "32px" }}>
          <div>
            <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "12px", color: COLORS.faint, fontFamily: FONTS.mono, fontSize: "11px", letterSpacing: "0.14em" }}>
              <Terminal size={13} />
              SECURITY AUDIT REPORT
            </div>
            <h1 style={{ fontSize: "28px", fontWeight: 700, letterSpacing: "-0.01em", margin: 0 }}>Security Analysis</h1>
            <p style={{ color: COLORS.muted, fontSize: "14px", marginTop: "6px" }}>Security analysis of the analyzed Java project</p>
          </div>
          <div style={{ color: COLORS.faint, fontFamily: FONTS.mono, fontSize: "11px", textAlign: "right", whiteSpace: "nowrap" }}>
            GENERATED {dateStr.toUpperCase()}
            <br />
            {stats.total} METHOD{stats.total === 1 ? "" : "S"} SCANNED
          </div>
        </div>

        {/* Stat tiles */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "12px", marginBottom: "16px" }}>
          {[
            { label: "EntryPoints Analyzed", value: stats.total, color: COLORS.text },
            { label: "Vulnerable Methods", value: stats.vulnerable, color: stats.vulnerable ? COLORS.critical : COLORS.text },
            { label: "Safe Methods", value: stats.safe, color: COLORS.safe },
            { label: "Total Vulnerabilities", value: stats.totalVulns, color: stats.totalVulns ? COLORS.high : COLORS.text },
          ].map((s) => (
            <div key={s.label} style={{ background: COLORS.surface, border: `1px solid ${COLORS.border}`, borderRadius: "10px", padding: "14px 16px" }}>
              <div style={{ color: COLORS.faint, fontSize: "11px", letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: "6px" }}>{s.label}</div>
              <div style={{ fontFamily: FONTS.mono, fontSize: "24px", fontWeight: 600, color: s.color }}>{s.value}</div>
            </div>
          ))}
        </div>

        {/* Severity distribution — width encodes real proportion of findings */}
        <div style={{ background: COLORS.surface, border: `1px solid ${COLORS.border}`, borderRadius: "10px", padding: "16px 18px", marginBottom: "28px" }}>
          <div style={{ color: COLORS.faint, fontSize: "11px", letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: "10px" }}>Severity Overview</div>
          {stats.totalVulns > 0 ? (
            <>
              <div style={{ display: "flex", width: "100%", height: "10px", borderRadius: "999px", overflow: "hidden", background: COLORS.border }}>
                {SEVERITY_ORDER.map((sev) =>
                  stats.counts[sev] > 0 ? (
                    <div key={sev} title={`${sev} \u00b7 ${stats.counts[sev]}`} style={{ width: `${(stats.counts[sev] / stats.totalVulns) * 100}%`, background: SEVERITY_COLOR[sev] }} />
                  ) : null
                )}
              </div>
              <div style={{ display: "flex", flexWrap: "wrap", gap: "8px 20px", marginTop: "12px" }}>
                {SEVERITY_ORDER.map((sev) => (
                  <div key={sev} style={{ display: "flex", alignItems: "center", gap: "8px", fontSize: "12px", color: COLORS.muted }}>
                    <span style={{ width: "8px", height: "8px", borderRadius: "999px", background: SEVERITY_COLOR[sev], display: "inline-block" }} />
                    {sev.charAt(0) + sev.slice(1).toLowerCase()}
                    <span style={{ fontFamily: FONTS.mono, color: COLORS.text }}>{stats.counts[sev]}</span>
                  </div>
                ))}
              </div>
            </>
          ) : (
            <div style={{ color: COLORS.muted, fontSize: "13px" }}>No vulnerabilities detected across the scanned methods.</div>
          )}
        </div>

        {/* Controls */}
        <div style={{ display: "flex", flexWrap: "wrap", gap: "12px", marginBottom: "12px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "8px", flex: 1, minWidth: "220px", background: COLORS.surface, border: `1px solid ${COLORS.border}`, borderRadius: "8px", padding: "9px 12px" }}>
            <Search size={15} color={COLORS.faint} />
            <input
              className="ad-input"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search by method, class or package..."
              style={{ background: "transparent", border: "none", color: COLORS.text, fontSize: "13px", width: "100%" }}
            />
            {query && (
              <button onClick={() => setQuery("")} aria-label="Clear search" style={{ background: "transparent", border: "none", cursor: "pointer" }}>
                <X size={14} color={COLORS.faint} />
              </button>
            )}
          </div>

          <div style={{ display: "flex", gap: "6px", flexWrap: "wrap" }}>
            {(["ALL", "VULNERABLE", "SAFE"] as const).map((s) => (
              <button
                key={s}
                className="ad-chip"
                onClick={() => setStatusFilter(s)}
                style={{
                  fontSize: "12px",
                  fontFamily: FONTS.mono,
                  padding: "8px 12px",
                  borderRadius: "7px",
                  border: `1px solid ${statusFilter === s ? COLORS.borderLight : COLORS.border}`,
                  background: statusFilter === s ? COLORS.surfaceRaised : "transparent",
                  color: statusFilter === s ? COLORS.text : COLORS.muted,
                  cursor: "pointer",
                }}
              >
                {s}
              </button>
            ))}
          </div>
        </div>

        <div style={{ display: "flex", gap: "6px", flexWrap: "wrap", marginBottom: "28px" }}>
          <button
            className="ad-chip"
            onClick={() => setSeverityFilter("ALL")}
            style={{
              fontSize: "12px",
              fontFamily: FONTS.mono,
              padding: "6px 11px",
              borderRadius: "999px",
              border: `1px solid ${severityFilter === "ALL" ? COLORS.borderLight : COLORS.border}`,
              background: severityFilter === "ALL" ? COLORS.surfaceRaised : "transparent",
              color: severityFilter === "ALL" ? COLORS.text : COLORS.muted,
              cursor: "pointer",
            }}
          >
            ALL SEVERITIES
          </button>
          {SEVERITY_ORDER.map((sev) => {
            const active = severityFilter === sev;
            return (
              <button
                key={sev}
                className="ad-chip"
                onClick={() => setSeverityFilter(active ? "ALL" : sev)}
                style={{
                  fontSize: "12px",
                  fontFamily: FONTS.mono,
                  padding: "6px 11px",
                  borderRadius: "999px",
                  border: `1px solid ${active ? SEVERITY_COLOR[sev] : COLORS.border}`,
                  background: active ? SEVERITY_TINT[sev] : "transparent",
                  color: active ? SEVERITY_COLOR[sev] : COLORS.muted,
                  cursor: "pointer",
                }}
              >
                {sev}
              </button>
            );
          })}
        </div>

        {/* Method list */}
        <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
          {filtered.length === 0 && (
            <div style={{ textAlign: "center", padding: "48px 0", color: COLORS.faint }}>
              <ShieldAlert size={22} style={{ margin: "0 auto 10px" }} />
              <div style={{ fontSize: "13px" }}>No methods match the current filters.</div>
            </div>
          )}

          {filtered.map((method) => {
            const isOpen = expanded.has(method.methodId);
            const topSev = method.vulnerabilities.length
              ? method.vulnerabilities.reduce((worst, v) => (SEVERITY_RANK[norm(v.severity)] > SEVERITY_RANK[norm(worst.severity)] ? v : worst)).severity
              : null;
            const accent = topSev ? SEVERITY_COLOR[norm(topSev)] : COLORS.safe;

            return (
              <div
                key={method.methodId}
                className="ad-card"
                style={{ background: COLORS.surface, border: `1px solid ${COLORS.border}`, borderLeft: `3px solid ${accent}`, borderRadius: "10px", overflow: "hidden" }}
              >
                <button
                  onClick={() => toggle(method.methodId)}
                  style={{ display: "block", width: "100%", textAlign: "left", background: "transparent", border: "none", cursor: "pointer", padding: "16px 18px", color: "inherit" }}
                >
                  <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: "16px" }}>
                    <div style={{ minWidth: 0 }}>
                      <div style={{ fontFamily: FONTS.mono, fontSize: "14.5px", fontWeight: 600 }}>{method.methodName}()</div>
                      <div style={{ color: COLORS.muted, fontSize: "12.5px", marginTop: "3px" }}>{method.className}</div>
                      <div style={{ color: COLORS.faint, fontSize: "11px", fontFamily: FONTS.mono, marginTop: "1px" }}>{method.methodPackage}</div>
                    </div>

                    <div style={{ display: "flex", alignItems: "center", gap: "8px", flexShrink: 0 }}>
                      {method.status === "VULNERABLE" ? (
                        <span style={{ display: "flex", alignItems: "center", gap: "4px", background: COLORS.criticalTint, color: COLORS.critical, fontSize: "11px", fontFamily: FONTS.mono, padding: "4px 9px", borderRadius: "999px" }}>
                          <ShieldAlert size={12} /> VULNERABLE
                        </span>
                      ) : (
                        <span style={{ display: "flex", alignItems: "center", gap: "4px", background: COLORS.safeTint, color: COLORS.safe, fontSize: "11px", fontFamily: FONTS.mono, padding: "4px 9px", borderRadius: "999px" }}>
                          <ShieldCheck size={12} /> SAFE
                        </span>
                      )}
                      <span style={{ background: SEVERITY_TINT[norm(method.overall_risk)] || COLORS.border, color: SEVERITY_COLOR[norm(method.overall_risk)] || COLORS.muted, fontSize: "11px", fontFamily: FONTS.mono, padding: "4px 9px", borderRadius: "999px" }}>
                        {method.overall_risk}
                      </span>
                      <ChevronDown className="ad-chev" size={16} color={COLORS.faint} style={{ transform: isOpen ? "rotate(180deg)" : "rotate(0deg)" }} />
                    </div>
                  </div>

                  <div style={{ display: "flex", alignItems: "center", gap: "12px", marginTop: "12px" }}>
                    <span style={{ fontSize: "11px", color: COLORS.faint, fontFamily: FONTS.mono, letterSpacing: "0.06em" }}>CONFIDENCE</span>
                    <div style={{ flex: 1, height: "5px", borderRadius: "999px", background: COLORS.border, overflow: "hidden" }}>
                      <div style={{ width: `${method.confidence * 100}%`, height: "100%", background: accent }} />
                    </div>
                    <span style={{ fontSize: "11px", color: COLORS.muted, fontFamily: FONTS.mono }}>{(method.confidence * 100).toFixed(0)}%</span>
                  </div>

                  <p style={{ color: COLORS.muted, fontSize: "13px", lineHeight: 1.55, marginTop: "12px" }}>{method.summary}</p>
                </button>

                {isOpen && method.vulnerabilities.length > 0 && (
                  <div style={{ borderTop: `1px solid ${COLORS.border}`, padding: "16px 18px", background: COLORS.surfaceRaised }}>
                    <div style={{ color: COLORS.faint, fontSize: "11px", letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: "12px" }}>
                      Findings ({method.vulnerabilities.length})
                    </div>
                    <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
                      {method.vulnerabilities.map((vulnerability, index) => (
                        <div key={`${method.methodId}-${index}`} style={{ background: COLORS.surface, border: `1px solid ${COLORS.border}`, borderRadius: "8px", padding: "14px" }}>
                          <div style={{ display: "flex", alignItems: "center", flexWrap: "wrap", gap: "8px", marginBottom: "10px" }}>
                            <strong style={{ fontSize: "13.5px" }}>{vulnerability.type}</strong>
                            <span style={{ background: SEVERITY_TINT[norm(vulnerability.severity)], color: SEVERITY_COLOR[norm(vulnerability.severity)], fontSize: "10.5px", fontFamily: FONTS.mono, padding: "2px 8px", borderRadius: "999px" }}>
                              {norm(vulnerability.severity)}
                            </span>
                            <span style={{ background: COLORS.border, color: COLORS.muted, fontSize: "10.5px", fontFamily: FONTS.mono, padding: "2px 8px", borderRadius: "999px" }}>
                              {vulnerability.cwe}
                            </span>
                            <span style={{ color: COLORS.faint, fontSize: "10.5px", fontFamily: FONTS.mono, padding: "2px 8px" }}>LINE {vulnerability.line}</span>
                          </div>
                          <p style={{ color: COLORS.muted, fontSize: "12.5px", lineHeight: 1.6, marginBottom: "10px" }}>{vulnerability.description}</p>
                          <div style={{ borderLeft: `2px solid ${accent}`, paddingLeft: "10px" }}>
                            <div style={{ color: accent, fontSize: "10.5px", fontFamily: FONTS.mono, letterSpacing: "0.06em", marginBottom: "3px" }}>FIX</div>
                            <p style={{ color: COLORS.text, fontSize: "12.5px", lineHeight: 1.6 }}>{vulnerability.recommendation}</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}