import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../service/api.service';

import { Countries } from '../../class/Country';

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
  allcountry: Countries[];
  countryDisplay:Countries[];



  getdropdown = () => {
    this.countryApi.getAllCity().subscribe(
      data => {
        this.dic = data;
        console.log(this.dic);
        console.log(Object.keys(this.dic));
      }
    )
  };
  
  ngOnInit() {
    this.isSpecific = false;
    this.countryApi.getAllCity()
    .subscribe
    (
      data=>
      {
        this.allcountry = data;
        console.log('-----Nancy------');
        console.log(this.allcountry);
        console.log('-----Nancy------')
      }
    )
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
