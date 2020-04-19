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
  country_city_list_dep={}
  country_list_dep={}

  constructor(private countryApi: ApiService) { 
    this.getdropdown();
    this.country_city_list_dep={}
    this.dic = {}
  }


  dict = [1,2,4]; // create an empty array
  countrytest=[];
  citytest=[]; 



  getdropdown = () => {
    this.api.getCountryCityDep().subscribe(
      data => {
        this.country_city_list_dep = data
        this.country_list_dep=Object.keys(this.country_city_list_dep)
        console.log(this.country_city_list_dep);
        console.log(Object.keys(this.country_city_list_dep))
        
      }
    )
  };
  // show=[]
  // showvalue;
  // onChangeCountry() {
  //   console.log(this.showvalue);
  // }
  
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
