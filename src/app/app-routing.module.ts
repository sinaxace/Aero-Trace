/* Angular Routing Reference: https://angular.io/guide/router 
  This is the first level of routing in the application. 
  Nested routes are within their component's routing module.
  Note: Use 'ng g m <component-name> --routing' in Angular CLI to generate module files.
*/
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SchedulesComponent } from './schedules/schedules.component';
import { TerminalsComponent } from './terminals/terminals.component';
import { RestaurantsComponent } from './restaurants/restaurants.component';
import { EstimatorsComponent } from './estimators/estimators.component';
import { HomeComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { DepartComponent } from './schedules/depart/depart.component';
import { ArriveComponent } from './schedules/arrive/arrive.component';
import { ResultComponent } from './schedules/result/result.component';
import { ReviewsComponent } from './reviews/reviews.component';
import { WrittenreviewComponent } from './writtenreview/writtenreview.component';

// routes is a Singleton array that contains metadata for component navigation
const routes: Routes = [
  {
    path: 'schedules', component: SchedulesComponent, children: [
      {
        path: 'depart', component: DepartComponent
      },
      {
        path: 'arrive', component: ArriveComponent
      },
      {
        path: '', redirectTo: 'depart', pathMatch: 'full' // First loads to depart component
      }
    ]
  },
  { path: 'result', component: ResultComponent },
  { path: 'terminals', component: TerminalsComponent },
  { path: 'restaurants', component: RestaurantsComponent },
  { path: 'reviews', component: ReviewsComponent },
  { path: 'writtenreview', component: WrittenreviewComponent},
  { path: 'estimators', component: EstimatorsComponent },
  { path: '', component: HomeComponent, pathMatch: 'full' }, // The empty default route is home page
  { path: '**', component: PageNotFoundComponent } // if cannot find page for some reason
];

@NgModule({
  imports: [RouterModule.forRoot(
    routes,
    { enableTracing: true } // to debug in stacktrace
  )],
  exports: [RouterModule]
})
export class AppRoutingModule { }
