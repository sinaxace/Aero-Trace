import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { ApiService } from "../../api.service";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { throwError } from 'rxjs';  // Angular 6/RxJS 6


// Note: This component is a login/register dialog popup

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.less']
})
export class AccountComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<AccountComponent>,
    private _userService: ApiService) { }

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
    this._userService.registerUser({ 'username': this.user.username, 'email': this.register.email, 'password': this.user.password }).subscribe(
      response => {
        alert('User' + this.user.username + 'Has been created');
      },
      error => console.log(error)

    )

  }

  login() {
    this._userService.login({ 'username': this.user.username, 'password': this.user.password });
  }

  refreshToken() {
    this._userService.refreshToken();
  }

  logout() {
    this._userService.logout();
  }

  onNoClick(): void {
    this.dialogRef.close();
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

}
