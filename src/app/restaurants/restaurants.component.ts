import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-restaurants',
  templateUrl: './restaurants.component.html',
  styleUrls: ['./restaurants.component.less']
})
export class RestaurantsComponent implements OnInit {

  // TODO: grab ratings through service API and load them dynamically into Angular.
  rating: boolean[] = [true, true, true, false, false]; // for now, just a fixed boolean array

  constructor() { }

  ngOnInit() {

  }

}
