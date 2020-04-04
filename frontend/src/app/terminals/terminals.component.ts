import { Component, OnInit } from '@angular/core';
import * as L from "leaflet"; // leaflet.js library

@Component({
  selector: 'app-terminals',
  templateUrl: './terminals.component.html',
  styleUrls: ['./terminals.component.less']
})
export class TerminalsComponent implements OnInit {

  private map;

  constructor() { }

  private initMap(): void {
    this.map = L.map('map', {
      center: [39.8282, -98.5795],
      zoom: 3
    });

    const tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    tiles.addTo(this.map);
  }

  ngOnInit() {
  }

  ngAfterViewInit() {
    this.initMap();
  }

}
