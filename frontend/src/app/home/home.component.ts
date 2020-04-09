import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less']
})
export class HomeComponent implements OnInit {
 


  constructor() { }

  ngOnInit() {
  }

  
  // constructor(private api: ApiService) {
  //   this.getMovies();
  // }
  // getMovies = () => {
  //   this.api.getCity().subscribe(
  //     data => {
  //       this.cities = data;
       
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
