import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgModule } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less'],
  providers: [ApiService]
})
export class HomeComponent implements OnInit {
  register;


  constructor(private api: ApiService) {
    this.getMovies();
    var cities = {}
  }

  ngOnInit() {
    this.register = {
      username: '',
      password: '',
      email: ''
    };
  }
  registerUser() {
    console.log('alo')
    this.api.registerUser(this.register).subscribe(
      response => {
        alert('User' + this.register.username + 'Has been created');
      },
      error => console.log(error)
    )

   }

  

  getMovies = () => {
    this.api.getAllMovies().subscribe(
      data => {
        const cities = data;
      })
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
      
    

