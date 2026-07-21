package com.example.demo.controller;
import org.springframework.web.bind.annotation.*;
import com.example.demo.model.*;
import com.example.demo.service.AnalyzerService;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
@RequestMapping("/api/v1")
@CrossOrigin(origins = "http://localhost:5173")
public class AnalyzeController {

    private final AnalyzerService AnalyzeService;
    @Autowired
    public AnalyzeController(AnalyzerService As){
        AnalyzeService=As;
    }
    @GetMapping("/health")
    public String Health(){
        return "{'health':'Api ok'}";
    }
    @PostMapping("/Analyze")
    public Project Analyze(@RequestBody AnalyzeRequest req){
        Project p=AnalyzeService.AnalyzeProject(req);
        return p;
    }
}
    

