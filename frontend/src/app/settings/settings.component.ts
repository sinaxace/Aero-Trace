import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.less']
})
export class SettingsComponent implements OnInit {

  isChanged: boolean = false;

  constructor() { }

  ngOnInit() {
  }

}
