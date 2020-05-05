import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  //httpOptions used for making API calls
  private httpOptions: any;

  //the actual JWT token
  public token: string;

  //the token expiration date
  public token_expires: Date;

  //the username of the logged in user
  public username: string;

  //error messages reveiced from the login attempt
  public errors: any = [];

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

  constructor(private http: HttpClient) {
    this.httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
   }
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
      return this.http.post(this.baseurl + '/users/', userData);
    }
  
    public login(user) {
      this.http.post('http://127.0.0.1:8000/api-token-auth/', JSON.stringify(user), this.httpOptions).subscribe(
          data => {
              this.updateData(data['token']);
          },
          err => {
              this.errors = err['error'];
          }
      );
    }
  
  // Refreshes the JWT token, to extend the time the user is logged in
  public refreshToken() {
    this.http.post('http://127.0.0.1:8000/api-token-refresh/', JSON.stringify({ token: this.token }), this.httpOptions).subscribe(
        data => {
            this.updateData(data['token']);
        },
        err => {
            this.errors = err['error'];
        }
    );
}

public logout() { 
    this.token = null;
    this.token_expires = null;
    this.username = null;
}
private updateData(token) { 
    this.token = token;
    this.errors = [];

    //decode the token to read the username and expiration timestamp
    const token_parts = this.token.split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    console.log(token_decoded);
    this.token_expires = new Date(token_decoded.exp * 1000);
    this.username = token_decoded.username;
}
  
  }

