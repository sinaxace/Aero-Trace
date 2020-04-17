import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-arrive',
  templateUrl: './arrive.component.html',
  styleUrls: ['./arrive.component.less']
})
export class ArriveComponent implements OnInit {

  isSpecific: boolean;

  constructor() { }

  ngOnInit() {
    this.isSpecific = false;
  }

}
