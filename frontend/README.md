# AeroTrace
Note: Be sure to add the node_modules folder using the npm command. Alternatively, you can just replace the src folder with the current one after running ng new command.

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.3.20.

## HammerJS npm Installation for Angular Material animations:
Run the command `npm install --save hammerjs` if the Angular CLI didn't install it already.

## i18n Localization for a multi-lingual site:
Type `ng add @angular/localize` to install Angular's i18n tool so that language settings will work.

## Leaflet Library Installation for terminal maps:
Run the command `npm install leaflet --save` and create a relative string url inside `./angular.json` for both `"styles" []` and `"scripts" []` config arrays.

After doing this, follow the tutorial below.

The following link is a tutorial by Chris Engelsma who perfectly explains how to setup the initial map configurations in an angular 8 project.
https://alligator.io/angular/angular-and-leaflet/ 



## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
