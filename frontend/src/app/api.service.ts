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
    getAllMovies(): Observable < any > {
      return this.http.get(this.baseurl + '/tasks/',
        { headers: this.httpHeaders });
    }

    //Departure country and city API url
    getCountryCityDep(): Observable < any > {
      return this.http.get(this.baseurl + '/Dep_Country_City_list/',
        { headers: this.httpHeaders });
    }

    //Departure flight schedule today
    getDepFlightSchedule(): Observable < any > {
      return this.http.get(this.baseurl + '/Dep_Flight_Schedule/',
        { headers: this.httpHeaders });
    }

    registerUser(userData): Observable<any> { 
      console.log(userData);
      return this.http.get(this.baseurl + '/users/', userData);
    }
  
  }

