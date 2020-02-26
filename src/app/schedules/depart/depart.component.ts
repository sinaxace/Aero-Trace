import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-depart',
  templateUrl: './depart.component.html',
  styleUrls: ['./depart.component.less']
})
export class DepartComponent implements OnInit {

  isSpecific: boolean;
  

  constructor() { }

  ngOnInit() {
    this.isSpecific = false;
  }

}
