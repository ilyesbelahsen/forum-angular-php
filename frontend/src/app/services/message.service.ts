import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

export interface user {
  id_user: string;
  username: string;
  email: string;
}
@Injectable({
  providedIn: 'root'
})
export class MessageService {

  constructor(private http; HttpClient) { }

  getUser() : Observable<users[]>{
    return this.http.get<Users[]>('http://127.0.0.1/users')
}
}
