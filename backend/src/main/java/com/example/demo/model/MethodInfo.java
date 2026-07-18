package com.example.demo.model;
import java.util.*;

public class MethodInfo {

    public String id;
    public String className;
    public String packageName;
    public String signature;
    public String sourceCode;

    public List<String> annotations = new ArrayList<>();
    public List<String> outgoingCalls = new ArrayList<>();
    public List<String> incomingCalls = new ArrayList<>();
    public List<String> parameters = new ArrayList<>();
    public List<String> variables = new ArrayList<>();

    public int beginLine;
    public int endLine;

    @Override
    public String toString() {
        return "MethodInfo{" +
                "\nid='" + id + '\'' +
                ",\nclassName='" + className + '\'' +
                ",\npackageName='" + packageName + '\'' +
                ",\nsignature='" + signature + '\'' +
                ",\nparameters=" + parameters +
                ",\nannotations=" + annotations +
                ",\noutgoingCalls=" + outgoingCalls +
                ",\nvariables=" + variables +
                ",\nbeginLine=" + beginLine +
                ",\nendLine=" + endLine +
                "\n}";
    }
}