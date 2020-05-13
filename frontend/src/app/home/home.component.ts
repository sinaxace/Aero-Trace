import { Component, OnInit } from '@angular/core';
import { ApiService } from "../api.service";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { throwError } from 'rxjs';  // Angular 6/RxJS 6

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.less'],
  providers: [ApiService]
})
export class HomeComponent implements OnInit {

  ngOnInit(){};

}



