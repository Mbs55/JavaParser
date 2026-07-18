package com.example.demo.model;
import java.util.*;

public class ClassInfo {

    public String id;

    public String className;

    public String packageName;

    public String qualifiedName;

    public String sourceCode;

    public String filePath;

    public int beginLine;

    public int endLine;

    public String superClass;

    public List<String> implementedInterfaces = new ArrayList<>();

    public List<String> methods = new ArrayList<>();

    public List<String> fields = new ArrayList<>();

    public List<String> annotations = new ArrayList<>();

    public List<String> dependencies = new ArrayList<>();

    @Override
    public String toString() {
        return "ClassInfo{" +
                "\nqualifiedName='" + qualifiedName + '\'' +
                ",\nmethods=" + methods +
                ",\nfields=" + fields +
                ",\ndependencies=" + dependencies +
                "\n}";
    }
}
