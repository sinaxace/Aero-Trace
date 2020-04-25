import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-arrive',
  templateUrl: './arrive.component.html',
  styleUrls: ['./arrive.component.less']
})
export class ArriveComponent implements OnInit {

  isSpecific: boolean;

  constructor(private country_dep_api: ApiService) {
    this.countryDropListArr();
   }
   
   country_city_list=[];
   country_list = [];
   city_list = [];   

   countryDropListArr = () => {

   };
  ngOnInit() {
    this.isSpecific = false;
  }

}
