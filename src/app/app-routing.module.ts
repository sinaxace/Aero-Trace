/* Angular Routing Reference: https://angular.io/guide/router 
  TODO: add the router outlet tag into the root || nav component.html
*/
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SchedulesComponent } from './schedules/schedules.component';
import { TerminalsComponent } from './terminals/terminals.component';
import { RestaurantsComponent } from './restaurants/restaurants.component';
import { EstimatorsComponent } from './estimators/estimators.component';
import { HomeComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

// routes is a Singleton array that contains metadata for component navigation
const routes: Routes = [
  { path: 'schedules', component: SchedulesComponent },
  { path: 'terminals', component: TerminalsComponent },
  { path: 'restaurants', component: RestaurantsComponent },
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
