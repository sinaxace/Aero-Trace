import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from './material-ui/material-ui.module';
import { OwlDateTimeModule, OwlNativeDateTimeModule } from 'ng-pick-datetime';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SchedulesComponent } from './schedules/schedules.component';
import { RestaurantsComponent } from './restaurants/restaurants.component';
import { EstimatorsComponent } from './estimators/estimators.component';
import { TerminalsComponent } from './terminals/terminals.component';
import { HomeComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { DepartComponent } from './schedules/depart/depart.component';
import { ArriveComponent } from './schedules/arrive/arrive.component';
import { ResultComponent } from './schedules/result/result.component';
@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    SchedulesComponent,
    RestaurantsComponent,
    EstimatorsComponent,
    TerminalsComponent,
    HomeComponent,
    PageNotFoundComponent,
    DepartComponent,
    ArriveComponent,
    ResultComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    OwlDateTimeModule,
    OwlNativeDateTimeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }