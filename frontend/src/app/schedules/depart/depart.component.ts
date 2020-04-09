import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-depart',
  templateUrl: './depart.component.html',
  styleUrls: ['./depart.component.less']
})
export class DepartComponent implements OnInit {

  isSpecific: boolean;
  dic={}

  constructor(private api: ApiService) { 
    this.getdropdown();
    this.dic = {}
  }


  dict = [1,2,3]; // create an empty array



  getdropdown = () => {
    this.api.getAllMovies().subscribe(
      data => {
        this.dic = data
        console.log(this.dic);
        console.log(Object.keys(this.dic))
        
      }
    )
  };
  ;

  

  ngOnInit() {
    this.isSpecific = false;
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
}
