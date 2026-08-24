package com.example.demo.model;

import java.util.*;

public class ClassInfo {
    public String id;
    public String className;
    public String qualifiedName;
    public String packageName;
    public String filePath;
    public int beginLine;
    public int endLine;
    public boolean isClass;
    public boolean isInterface;
    public boolean isEnum;
    public boolean isRecord;
    public String visibility;
    public boolean isAbstract;
    public boolean isFinal;
    public String superClass;
    public List<String> implementedInterfaces = new ArrayList<>();
    public List<String> constructors = new ArrayList<>();
    public List<String> methods = new ArrayList<>();
    public List<String> fields = new ArrayList<>();
    public List<String> annotations = new ArrayList<>();
    public List<String> imports = new ArrayList<>();
    public List<String> dependencies = new ArrayList<>();
    public List<String> genericTypes = new ArrayList<>();

    @Override
    public String toString() {
        return "ClassInfo{" +
                "\nqualifiedName='" + qualifiedName + '\'' +
                ",\nmethods=" + methods +
                ",\nfields=" + fields +
                ",\nimports=" + imports +
                ",\ndependencies=" + dependencies +
                "\n}";
    }
}