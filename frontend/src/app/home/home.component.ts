import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgModule } from '@angular/core';
import {throwError} from 'rxjs';  // Angular 6/RxJS 6

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less'],
  providers: [ApiService]
})
export class HomeComponent implements OnInit {
  public register: any;
  /**
   * An object representing the user for the login form
   */
  public user: any;

  /**
   * An array of all the BlogPost objects from the API
   */
  public posts;

  /**
   * An object representing the data in the "add" form
   */
  public new_post: any;

  constructor(private _userService: ApiService) { }

  ngOnInit() {
    this.register = {
      email: ''
    };
    
    this.new_post = {};
    this.user = {
      username: '',
      password: ''
    };
  }
  registerUser() {
    this._userService.registerUser({'username': this.user.username,'email':this.register.email ,'password': this.user.password}).subscribe(
      response => {
        alert('User' + this.user.username + 'Has been created');
      },
      error => console.log(error)
    
    )
    
  }

  login() {
    this._userService.login({'username': this.user.username, 'password': this.user.password});
  }

  refreshToken() {
    this._userService.refreshToken();
  }

  logout() {
    this._userService.logout();
  }


}      
        //     },
        //     error => {
        //       console.log(error);
        //     }
        //   );
        // }
        // movieClicked = (movie) => {
        //   console.log(movie.id);
        //   this.api.getOneMovie(movie.id).subscribe(
        //     data => {
        //       this.title = data.title;
        //       this.desc = data.desc;
        //       this.year = data.year;
        //     },
        //     error => {
        //       console.log(error);
        //     }
        //   );
        // }
      
    

