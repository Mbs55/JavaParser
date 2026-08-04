package com.example.demo.model;

import java.util.*;

public class MethodInfo {

    public String id;
    public String name;
    public String signature;
    public String qualifiedSignature;
    public String className;
    public String packageName;
    public String filePath;
    public int beginLine;
    public int endLine;
    public String sourceCode;
    public String returnType;
    public List<String> genericTypes = new ArrayList<>();
    public List<String> thrownExceptions = new ArrayList<>();
    public String visibility;
    public boolean isEntryPoint;
    public String httpMethod;
    public String endpoint;
    public boolean isStatic;
    public boolean isFinal;
    public boolean isAbstract;
    public boolean isSynchronized;
    public boolean isNative;
    public List<String> annotations = new ArrayList<>();
    public List<String> outgoingCalls = new ArrayList<>();
    public List<String> incomingCalls = new ArrayList<>();
    public List<String> parameters = new ArrayList<>();
    public List<String> variables = new ArrayList<>();
    public boolean isConstructor;
    public boolean containsLambda;

    @Override
    public String toString() {
        return "MethodInfo{" +
                "\nid='" + id + '\'' +
                ",\nqualifiedSignature='" + qualifiedSignature + '\'' +
                ",\nreturnType='" + returnType + '\'' +
                ",\nvisibility='" + visibility + '\'' +
                ",\nparameters=" + parameters +
                ",\nannotations=" + annotations +
                ",\noutgoingCalls=" + outgoingCalls +
                ",\nvariables=" + variables +
                ",\nthrows=" + thrownExceptions +
                "\n}";
    }
}