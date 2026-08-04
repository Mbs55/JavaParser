package com.example.demo.service;
import java.util.*;
import com.github.javaparser.ParserConfiguration;
import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.symbolsolver.JavaSymbolSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.CombinedTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.JarTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.JavaParserTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.ReflectionTypeSolver;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.expr.ArrayInitializerExpr;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.expr.NormalAnnotationExpr;
import com.github.javaparser.ast.expr.SingleMemberAnnotationExpr;
import com.github.javaparser.resolution.declarations.ResolvedMethodDeclaration;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import com.example.demo.model.*;

@Service
public class AnalyzerService{
    private String getRequestMappingPath(ClassOrInterfaceDeclaration clazz) {
        if (clazz == null) {
            return "";
        }
        for (AnnotationExpr annotation : clazz.getAnnotations()) {
            String path = extractRequestMappingPath(annotation);
            if (!path.isBlank()) {
                return path;
            }
        }
        return "";
    }

    private String extractRequestMappingPath(AnnotationExpr annotation) {
        if (annotation == null) {
            return "";
        }
        if (annotation.isSingleMemberAnnotationExpr()) {
            return extractPathValue(annotation.asSingleMemberAnnotationExpr().getMemberValue());
        }
        if (annotation.isNormalAnnotationExpr()) {
            for (com.github.javaparser.ast.expr.MemberValuePair pair : annotation.asNormalAnnotationExpr().getPairs()) {
                String name = pair.getNameAsString();
                if ("path".equals(name) || "value".equals(name)) {
                    return extractPathValue(pair.getValue());
                }
            }
        }
        return "";
    }

    private String extractPathValue(Expression expression) {
        if (expression == null) {
            return "";
        }
        if (expression.isStringLiteralExpr()) {
            return expression.asStringLiteralExpr().asString();
        }
        if (expression.isArrayInitializerExpr()) {
            ArrayInitializerExpr array = expression.asArrayInitializerExpr();
            if (!array.getValues().isEmpty()) {
                return extractPathValue(array.getValues().get(0));
            }
        }
        return expression.toString().replace("\"", "");
    }

    private String normalizePath(String path) {
        if (path == null || path.isBlank()) {
            return "";
        }
        String normalized = path.trim().replace("\"", "");
        if (normalized.equals("/")) {
            return "/";
        }
        if (!normalized.startsWith("/")) {
            normalized = "/" + normalized;
        }
        while (normalized.endsWith("/") && normalized.length() > 1) {
            normalized = normalized.substring(0, normalized.length() - 1);
        }
        return normalized;
    }

    private String concatPaths(String parentPath, String childPath) {
        String normalizedParent = normalizePath(parentPath);
        String normalizedChild = normalizePath(childPath);
        if (normalizedParent.isEmpty()) {
            return normalizedChild;
        }
        if (normalizedChild.isEmpty()) {
            return normalizedParent;
        }
        if (normalizedParent.equals("/")) {
            return normalizedChild;
        }
        if (normalizedChild.equals("/")) {
            return normalizedParent;
        }
        return normalizedParent + normalizedChild;
    }

    public Project AnalyzeProject(AnalyzeRequest req){
            String projectPath=req.getProjectPath();//"(exp)C:\\Users\\M Bs\\Desktop\\java_test";
            Path Root=Paths.get(projectPath);
            if(!Files.isDirectory(Root)){
                    System.out.println("Directory does not exist");
                    return null;
                }
                ProcessBuilder pb = new ProcessBuilder(
    "cmd",
    "/c",
    "mvnw.cmd",
    "dependency:build-classpath",
    "-Dmdep.outputFile=cp.txt"
);      
        try { 
                pb.directory(Root.toFile());
                CombinedTypeSolver ts=new CombinedTypeSolver();
                ts.add(new ReflectionTypeSolver());
                Process process=pb.start();
                int exitCode=process.waitFor();
                if (exitCode == 0) {
                Path deps=Root.resolve("cp.txt");
                byte[] Deps=Files.readAllBytes(deps);
                String out=new String(Deps,StandardCharsets.UTF_8).trim();
                if(out!=null){
                        for(String jp:out.split(";")){
                               try{
                                        ts.add(new JarTypeSolver(jp));
                                }catch(IOException e){
                                        e.printStackTrace();
                        }
                        }
                }
                }
                Files.walk(Root)
                .filter(Files::isDirectory)
                .filter(path -> path.endsWith(Paths.get("src", "main", "java")))
                .forEach(path -> {
                        ts.add(new JavaParserTypeSolver(path));
                });    
                JavaSymbolSolver sS=new JavaSymbolSolver(ts);
                ParserConfiguration config=new ParserConfiguration();
                config.setLanguageLevel(ParserConfiguration.LanguageLevel.BLEEDING_EDGE);
                config.setSymbolResolver(sS);
                StaticJavaParser.setConfiguration(config);
                List<CompilationUnit> units=new ArrayList<>();
                Files.walk(Root).filter(path -> path.toString().endsWith(".java")).forEach(path -> {
                    try {
                        units.add(StaticJavaParser.parse(path));
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });
                Project P=new Project();
                List<MethodInfo> Ms=new ArrayList<>();
                P.methods=Ms;
                List<ClassInfo> Css=new ArrayList<>();
                P.classes=Css;

for (CompilationUnit cu : units) {

    List<MethodDeclaration> methods =
            cu.findAll(MethodDeclaration.class);
    List<ClassOrInterfaceDeclaration> classes=cu.findAll(ClassOrInterfaceDeclaration.class);
    for (ClassOrInterfaceDeclaration c : classes) {

    ClassInfo info = new ClassInfo();

    info.className = c.getNameAsString();

    info.qualifiedName = c.getFullyQualifiedName().orElse("");

    info.packageName = cu.getPackageDeclaration()
            .map(pd -> pd.getNameAsString())
            .orElse("");

    info.id = info.qualifiedName;

    info.sourceCode = c.toString();

    info.filePath = cu.getStorage()
            .map(s -> s.getPath().toString())
            .orElse("");

    info.beginLine = c.getBegin().map(p -> p.line).orElse(-1);
    info.endLine = c.getEnd().map(p -> p.line).orElse(-1);

    info.isClass = !c.isInterface();
    info.isInterface = c.isInterface();
    info.isEnum = false;
    info.isRecord = false;

    if (c.isPublic())
        info.visibility = "public";
    else if (c.isProtected())
        info.visibility = "protected";
    else if (c.isPrivate())
        info.visibility = "private";
    else
        info.visibility = "package-private";

    info.isAbstract = c.isAbstract();
    info.isFinal = c.isFinal();
    if (!c.getExtendedTypes().isEmpty()) {
        info.superClass =
                c.getExtendedTypes()
                        .get(0)
                        .getNameAsString();
    }
    c.getImplementedTypes().forEach(i ->
            info.implementedInterfaces.add(
                    i.getNameAsString()));


    c.getTypeParameters().forEach(tp ->
            info.genericTypes.add(tp.getNameAsString()));


    c.getConstructors().forEach(cons -> {

        try {
            info.constructors.add(
                    cons.resolve().getQualifiedSignature());
        }
        catch (Exception e) {
            info.constructors.add(
                    cons.getDeclarationAsString());
        }

    });


    c.getMethods().forEach(method -> {

        try {

            info.methods.add(
                    method.resolve()
                            .getQualifiedSignature());

        }
        catch (Exception e) {

            info.methods.add(
                    method.getDeclarationAsString());

        }

    });

    c.getFields().forEach(field -> {

        field.getVariables().forEach(v -> {

            info.fields.add(
                    v.getTypeAsString() + " " + v.getNameAsString());

            info.dependencies.add(
                    v.getTypeAsString());

        });

    });

    c.getAnnotations().forEach(a ->
            info.annotations.add(
                    a.getNameAsString()));

    cu.getImports().forEach(i ->
            info.imports.add(
                    i.getNameAsString()));

    P.addClasses(info);
}

    for (MethodDeclaration m : methods) {

    MethodInfo info = new MethodInfo();
        info.isEntryPoint=false;
    info.name = m.getNameAsString();

    try {
        info.qualifiedSignature = m.resolve().getQualifiedSignature();
        info.id = info.qualifiedSignature;
    }
    catch (Exception e) {
        info.id = m.getDeclarationAsString();
        info.qualifiedSignature = info.id;
    }

    info.signature = m.getDeclarationAsString();
    info.filePath = cu.getStorage()
            .map(s -> s.getPath().toString())
            .orElse("");

    info.className = m.findAncestor(ClassOrInterfaceDeclaration.class)
            .map(ClassOrInterfaceDeclaration::getNameAsString)
            .orElse("");

    info.packageName = cu.getPackageDeclaration()
            .map(pd -> pd.getNameAsString())
            .orElse("");

    info.beginLine = m.getBegin()
            .map(p -> p.line)
            .orElse(-1);

    info.endLine = m.getEnd()
            .map(p -> p.line)
            .orElse(-1);

    info.sourceCode = m.toString();

    info.returnType = m.getType().asString();

    if (m.isPublic())
        info.visibility = "public";
    else if (m.isProtected())
        info.visibility = "protected";
    else if (m.isPrivate())
        info.visibility = "private";
    else
        info.visibility = "package-private";

    info.isStatic = m.isStatic();
    info.isFinal = m.isFinal();
    info.isAbstract = m.isAbstract();
    info.isSynchronized = m.isSynchronized();
    info.isNative = m.isNative();

    

    m.getTypeParameters().forEach(tp ->
            info.genericTypes.add(tp.getNameAsString()));

    

    m.getThrownExceptions().forEach(ex ->
            info.thrownExceptions.add(ex.asString()));


    m.getParameters().forEach(p ->
            info.parameters.add(
                    p.getTypeAsString() + " " +
                    p.getNameAsString()));


    m.findAll(com.github.javaparser.ast.body.VariableDeclarator.class)
            .forEach(v ->
                    info.variables.add(
                            v.getTypeAsString() + " " +
                            v.getNameAsString()));


    String classPath = m.findAncestor(ClassOrInterfaceDeclaration.class)
            .map(this::getRequestMappingPath)
            .orElse("");
    String methodPath = "";

    for (AnnotationExpr a : m.getAnnotations()) {
        info.annotations.add(a.getNameAsString());

        if (a.isNormalAnnotationExpr()) {
            NormalAnnotationExpr ann = a.asNormalAnnotationExpr();
            for (com.github.javaparser.ast.expr.MemberValuePair pair : ann.getPairs()) {
                if (pair.getNameAsString().equals("method")) {
                    info.httpMethod = pair.getValue().toString();
                }
            }
        }

        String path = extractRequestMappingPath(a);
        if (!path.isBlank()) {
            methodPath = path;
        }

        switch (a.getNameAsString()) {
            case "RequestMapping":
            case "GetMapping":
            case "PostMapping":
            case "PutMapping":
            case "DeleteMapping":
            case "PatchMapping":
                info.isEntryPoint = true;
                break;
        }

        switch (a.getNameAsString()) {
            case "GetMapping":
                info.httpMethod = "GET";
                break;
            case "PostMapping":
                info.httpMethod = "POST";
                break;
            case "PutMapping":
                info.httpMethod = "PUT";
                break;
            case "DeleteMapping":
                info.httpMethod = "DELETE";
                break;
            case "PatchMapping":
                info.httpMethod = "PATCH";
                break;
        }
    }

    info.endpoint = concatPaths(classPath, methodPath);

    m.findAll(MethodCallExpr.class).forEach(call -> {

        try {

            info.outgoingCalls.add(
                    call.resolve()
                            .getQualifiedSignature());

        }
        catch (Exception e) {

            info.outgoingCalls.add(
                    call.toString());

        }

    });


    info.containsLambda =
            !m.findAll(com.github.javaparser.ast.expr.LambdaExpr.class)
                    .isEmpty();

    P.addMethod(info);
    Map<String,MethodInfo> methodMap=new HashMap<>();
    for(MethodInfo caller:P.methods){
        methodMap.put(caller.id,caller);
    }
    for(MethodInfo caller:P.methods){
        for(String callee:caller.outgoingCalls){
                MethodInfo M=methodMap.get(callee);
                if(M!=null){
                        M.incomingCalls.add(caller.id);
                }
        }
    }
    

}
    
    
}       
return P;
}catch(Exception e){
    e.printStackTrace();
    return null;
}}
        }


