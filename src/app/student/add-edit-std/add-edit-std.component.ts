import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-std',
  templateUrl: './add-edit-std.component.html',
  styleUrls: ['./add-edit-std.component.scss']
})
export class AddEditStdComponent implements OnInit {

  constructor(private service: SharedService) { }

  @Input() std: any;
  student_id!: string;
  student_name!: string;
  student_city!: string;
  student_course!: string;


  ngOnInit(): void {
    this.student_id = this.std.student_id;
    this.student_name = this.std.student_name;
    this.student_city = this.std.student_city;
    this.student_course = this.std.student_course;
    console.log(this.std);
  }
  addStudent() {
    var val = {
      student_id: this.student_id,
      student_name: this.student_name,
      student_city: this.student_city,
      student_course: this.student_course
    };
    this.service.addStudent(val).subscribe(res => {
      alert(res.toString());
    });


  }

  updateStudent() {
    var val = {
      student_id: this.student_id,
      student_name: this.student_name,
      student_city: this.student_city,
      student_course: this.student_course
    };
    this.service.updateStudent(val, this.std.id).subscribe(res => {
      alert(res.toString());
    });
  }

}
