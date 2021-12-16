import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) { }

  listStudent(): Observable<any> {
    return this.http.get<any>(this.APIurl + '/student/list/');
  }

  addStudent(val: any) {
    return this.http.post(this.APIurl + '/student/create/', val);
  }

  updateStudent(val: any, id: any) {
    return this.http.put(this.APIurl + '/student/update/' + id, val);
  }

  detailStudent(val: any) {
    return this.http.get(this.APIurl + '/student/detail/' + val);
  }

  deleteStudent(val: any) {
    return this.http.delete(this.APIurl + '/student/delete/' + val);
  }
}