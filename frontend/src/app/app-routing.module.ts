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
import { ResultsComponent } from './results/results.component';
import { ReviewsComponent } from './reviews/reviews.component';
import { WrittenreviewComponent } from './writtenreview/writtenreview.component';
import { EstimatedComponent } from './estimated/estimated.component';
import { SettingsComponent } from "./settings/settings.component";
import { OptionsComponent } from './settings/options/options.component';
import { LanguageComponent } from './settings/language/language.component';
import { NotificationsComponent } from './settings/notifications/notifications.component';
import { ThemesComponent } from './settings/themes/themes.component';
import { SecurityComponent } from './settings/security/security.component';
import { AccessibilityComponent } from './settings/accessibility/accessibility.component';
import { DatausageComponent } from './settings/datausage/datausage.component';

// routes is a Singleton array that contains metadata for component navigation
const routes: Routes = [
  {
    path: 'schedules', component: SchedulesComponent, children: [
      {
        path: '', redirectTo: 'results', pathMatch: 'full' // First loads to depart component
      }
    ]
  },
  { path: 'results', component: ResultsComponent },
  { path: 'terminals', component: TerminalsComponent },
  { path: 'restaurants', component: RestaurantsComponent },
  { path: 'reviews', component: ReviewsComponent },
  { path: 'writtenreview', component: WrittenreviewComponent },
  { path: 'estimators', component: EstimatorsComponent },
  { path: 'estimated', component: EstimatedComponent },
  {
    path: 'settings', component: SettingsComponent, children: [
      {
        path: "options", component: OptionsComponent // contains main setting options
      },
      {
        path: "notifications", component: NotificationsComponent
      },
      {
        path: "language", component: LanguageComponent
      },
      {
        path: "themes", component: ThemesComponent
      },
      {
        path: "security", component: SecurityComponent
      },
      {
        path: "accessibility", component: AccessibilityComponent
      },
      {
        path: "data-usage", component: DatausageComponent
      },
      {
        path: '', redirectTo: 'options', pathMatch: 'prefix' // First loads to options component
      }
    ]
  },
  { path: '', component: HomeComponent, pathMatch: 'full' }, // The empty default route is home page
  { path: '**', component: PageNotFoundComponent } // if cannot find page for some reason
];

@NgModule({
  imports: [RouterModule.forRoot(
    routes
    // { enableTracing: true } // to debug in stacktrace
  )],
  exports: [RouterModule]
})
export class AppRoutingModule { }
