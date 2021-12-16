import { Component, OnInit } from '@angular/core';
import { stringify } from 'querystring';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-std',
  templateUrl: './show-std.component.html',
  styleUrls: ['./show-std.component.scss']
})
export class ShowStdComponent implements OnInit {


  constructor(private service: SharedService) { }

  StudentList: any = [];

  ModalTitle: string = '';
  ActivateAddEditStdComp: boolean = false;
  std: any;
  ngOnInit(): void {
    this.refreshStdList();
  }

  addClick() {
    this.std = {
      student_id: "",
      student_name: "",
      student_city: "",
      student_course: ""
    }
    this.ModalTitle = "Add Student";
    this.ActivateAddEditStdComp = true;

  }

  editClick(id) {
    this.std = id;
    this.ModalTitle = "Edit Student";
    this.ActivateAddEditStdComp = true;

  }

  deleteClick(id) {
    if (confirm('Are you sure??')) {
      this.service.deleteStudent(id).subscribe(data => {
        alert(data.toString());
        this.refreshStdList();
      })
    }
  }

  closeClick() {
    this.ActivateAddEditStdComp = false;
    this.refreshStdList();
  }

  refreshStdList() {
    this.service.listStudent().subscribe(data => {
      this.StudentList = data.results;
      console.log("student list====", this.StudentList);
    });

  }

}

