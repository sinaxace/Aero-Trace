import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

  constructor(private http: HttpClient) { }

  registerUser(userData): Observable<any> { 
    console.log(userData);
    return this.http.post(this.baseurl + '/users/', userData);
    
  }
  

    getAllMovies(): Observable < any > {
      return this.http.get(this.baseurl + '/tasks/',
        { headers: this.httpHeaders });
    }
  
  }

