import { Component } from '@angular/core';
import { ApiService } from '../api.service';

//for dialog pop-up of details component
import { DetailsComponent } from "./details/details.component";
import { MatDialog } from "@angular/material/dialog";

// for swipe animations
import { trigger, keyframes, animate, transition } from '@angular/animations';
import * as slideKey from '../slide-keyframes';


@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.less'],
  animations: [
    trigger('rowSlide', [
      transition('* => slideInDetails', animate(1000, keyframes(slideKey.slideInDetails)))
    ])
  ]
})
export class ResultsComponent {

  animationState: string = '';

  dep_flight_data = {}
  dep_flight_display_data = []
  dep_index = [];
  dep_flight_scheduleTime = [];
  dep_flight_updatedTime = [];
  dep_flight_status = [];
  dep_flight_termianl = [];
  dep_flight_gate = [];

  // amount_flight records the number of result pages there are.
  amount_flight = 0;


  constructor(public dialog: MatDialog, private dep_flight_schedule: ApiService) {
    this.getDepFlightSchedule();
    this.dep_flight_data = {}
    this.dep_index = [];
  }

  showDetails() {
    this.dialog.open(DetailsComponent);
  }

  /**
   * @method onSwipeLeft starts the slideLeft animation and shows the details button
   * @param row contains the data row that was swiped.
   */
  onSwipeLeft(row: any) {
    console.log(row);
    console.log("sliding");
    if (!this.animationState) {
      this.animationState = "slideInDetails";
    }
    row.children[0].style.display = "none";
    row.children[2].style.display = "block";
    row.children[3].style.display = "none";
  }

  /**
   * @method onSwipeRight starts the slideRight animation and hide the details button
   * @param row contains the data row that was swiped.
   */
  onSwipeRight(row: any) {
    row.children[0].style.display = "block";
    row.children[2].style.display = "none";
    row.children[3].style.display = "block";
  }

  /**
   * @method resetAnimationState resets the animation state to 
   *              an empty string.
   */
  resetAnimationState() {
    // this.animationState = '';
  }

  getDepFlightSchedule = () => {
    this.dep_flight_schedule.getDepFlightSchedule().subscribe(
      data => {
        this.dep_flight_data = [];
        // console.log(this.dep_flight_data);
        this.dep_flight_data = data;
        // console.log(this.dep_flight_data);
        // this.dep_flight_display_data = [];
        // this.dep_flight_termianl = this.dep_flight_data['terminal'];
        // this.country_droplist_dep = Object.keys(this.dep_flight_data)
        // console.log(typeof this.dep_flight_data);
        // console.log(this.dep_flight_data);
        // console.log(Object.keys(this.dep_flight_data).length);
        // console.log(Math.ceil((Object.keys(this.dep_flight_data).length) / 10));
        this.amount_flight = Math.ceil((Object.keys(this.dep_flight_data).length) / 10);
        for (var i = 0; i < 6; i++) {
          this.dep_flight_display_data.push(this.dep_flight_data[i])
        }
        // this.dep_index = this.dep_flight_data.;
        // console.log(this.dep_flight_data['flight'][0]);
        // console.log(this.dep_flight_data.)
        // console.log(this.dep_flight_data['terminal']);
        // console.log(Object.keys(this.dep_flight_data));
        // console.log(this.dep_flight_data['CAN']);
        // console.log('---this.select_country..get dropdown-');
        // console.log(this.country_city_selected);
        // this.dep_flight_display_data = Array.from(data);

        // console.log('this.passIndex');
        // this.amount_flight = Math.ceil((Object.keys(this.dep_flight_display_data).length) / 10);
        // console.log(this.amount_flight);
        // console.log(this.dep_flight_display_data);
        // console.log(typeof this.dep_flight_display_data);

      }
    )
  };

  counter(i: number) {
    return new Array(i);
  }

  //get page from user click
  passIndex(pageNumber) {
    console.log(pageNumber);
    // console.log('dep display data')
    // console.log(this.dep_flight_display_data);
    this.dep_flight_display_data = [];

    for (var i = 0; i < 6; i++) {
      this.dep_flight_display_data.push(this.dep_flight_data[pageNumber * 10 + i])
    }
    console.log(this.dep_flight_display_data);

    // return pageNumber
  }

  /**
   * @method shiftNumbers is called when clicking the left or right buttons beside 
   *                the numbers. It basically shifts the page choice to more than the 
   *                default four.
   * @param isNext is a boolean which if true, shifts the number buttons right and if 
   *            false, shifts them back left.
   */
  shiftNumbers(isNext: boolean, index) {
    // grab page button DOM elements
    const pageButtons = document.getElementsByClassName("page"),
      NUMBERS = [],
      CHANGE: number = isNext ? 3 : -3; // either increment or decrement the buttons 


    // convert button textContent into numbers and store it in NUMBERS array.  
    for (let buttons = 0; buttons < pageButtons.length; buttons++) {
      NUMBERS[buttons] = Number.parseInt(pageButtons[buttons].textContent) + CHANGE;
      pageButtons[buttons].textContent = NUMBERS[buttons];
    }

    console.log(index);
  } // end of shiftNumbers method

} // end of ResultComponent
