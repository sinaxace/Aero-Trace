import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-schedules',
  templateUrl: './schedules.component.html',
  styleUrls: ['./schedules.component.less']
})
export class SchedulesComponent implements OnInit {

  optional: string = "gate"; // gates for depart, carousels for arrive
  isSpecific: boolean;
  isShowSelectCity = true;
  dic_country_city_dep = {}
  country_city_drop_list_dep = {}
  country_list_dep = {}
  select_country = '';
  today: Date;



  constructor(private country_dep_api: ApiService) {
    this.getdropdown();
    this.country_city_drop_list_dep = {}
    this.dic_country_city_dep = {}
    this.today = new Date();

  }


  country_city_droplist_dep = [];
  country_droplist_dep = [];
  city_droplist_dep = [];

  country_city_selected(event: any) {
    this.isShowSelectCity = false;
    this.select_country = event.target.value;
    this.city_droplist_dep = this.country_city_drop_list_dep[this.select_country];
    return this.select_country;
  }

  getTime(time: any) {
    console.log(time);
  }

  getdropdown = () => {
    this.country_dep_api.getCountryCityDep().subscribe(
      data => {
        this.country_city_drop_list_dep = data
        this.country_droplist_dep = Object.keys(this.country_city_drop_list_dep)
        console.log(this.country_city_drop_list_dep);
        console.log(Object.keys(this.country_city_drop_list_dep));
        console.log(this.country_city_drop_list_dep['CAN']);
        console.log('---this.select_country..get dropdown-');
        console.log(this.country_city_selected);
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
