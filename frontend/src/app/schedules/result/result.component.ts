import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';


@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.less']
})
export class ResultComponent implements OnInit {

  isSpecific: boolean;
  dic_country_city_dep = {}
  country_city_drop_list_dep = {}
  country_list_dep = {}
  select_country = '';

  constructor(private country_dep_api: ApiService) {
    this.getdropdown();
    this.country_city_drop_list_dep = {}
    this.dic_country_city_dep = {}
  }
  country_city_droplist_dep=[];
  country_droplist_dep = [];
  city_droplist_dep = [];
  getdropdown = () => {
    this.country_dep_api.getCountryCityDep().subscribe(
      data => {
        this.country_city_drop_list_dep = data
        this.country_droplist_dep = Object.keys(this.country_city_drop_list_dep)
        console.log(this.country_city_drop_list_dep);
        console.log(Object.keys(this.country_city_drop_list_dep));
        console.log(this.country_city_drop_list_dep['CAN']);
        console.log('---this.select_country..get dropdown-');
        // console.log(this.country_city_selected);
      }
    )
  };
  ngOnInit() {
  }

}
