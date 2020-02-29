import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'Aero-Trace';
  movies = [{ title:'test'}];

  constructor(private api: ApiService) {
    this.getMovies();
  }
  getMovies = () => {
    this.api.getAllMovies().subscribe(
      data => {
        this.movies = data;
      },
      error => {
        console.log(error);
      }
    )
  }

  }
