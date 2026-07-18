package com.example.demo.model;
public class AnalyzeRequest {

    private String projectPath;
    public AnalyzeRequest(){}
    public AnalyzeRequest(String pp){
        this.projectPath=pp;
    }
    public String getProjectPath() {
        return projectPath;
    }

    public void setProjectPath(String projectPath) {
        this.projectPath = projectPath;
    }
}