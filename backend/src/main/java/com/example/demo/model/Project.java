package com.example.demo.model;
import java.util.*;
import com.example.demo.*;

public class Project {
    public List<MethodInfo> methods;
    public List<ClassInfo> classes;

    public void addMethod(MethodInfo m){
        this.methods.add(m);
    }
    public void addClasses(ClassInfo c){
        this.classes.add(c);
    }
    // public void addGraph(CallGraph C){
    //     this.graph=C;
    // }

}
