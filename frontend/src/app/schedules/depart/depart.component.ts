import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../service/api.service';


@Component({
  selector: 'app-depart',
  templateUrl: './depart.component.html',
  styleUrls: ['./depart.component.less']
})

export class DepartComponent implements OnInit {

  isSpecific: boolean;
  dic={}

  constructor(private countryApi: ApiService) { 
    this.getdropdown();
    this.dic = {}
  }


  dict = [1,2,4]; // create an empty array
  countrytest=[];



  getdropdown = () => {
    this.countryApi.getAllCity().subscribe(
      data => {
        this.dic = data;
        this.countrytest=Object.keys(this.dic);
        console.log(this.dic["CAN"]);
        console.log(Object.keys(this.dic));
      }
    )
  };
  
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
