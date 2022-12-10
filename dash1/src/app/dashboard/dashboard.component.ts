import { Component, OnInit } from '@angular/core';
import { UploadService } from 'src/app/upload.service';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  private serverUrl = 'http://127.0.0.1:8080'; 
  //private selectedfile:File;
  //resp=[];
  
  imageDir:any="http://localhost:8080/static/uploaded_images/";

  constructor(private uploadService: UploadService) { }
  file: any=null;
  prediction:any;
  ngOnInit(): void {
    this.prediction=[];
  }

  onFilechange(event: any) {
    console.log(event.target.files[0]);
    this.file = event.target.files[0]
  }
  
  upload() {
    if (this.file) {
      this.uploadService.uploadfile(this.file).subscribe(resp=> {
        //alert("Uploaded")
        console.log(resp);
        this.prediction=resp
      })
    } else {
      alert("Please select a file first")
    }
  }
 
}
 