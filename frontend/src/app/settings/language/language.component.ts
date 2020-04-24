import { Component, OnInit, ViewEncapsulation } from '@angular/core';

/* Note: This is the first time I'm using the Shadow DOM 
  Here's a reference towhat I did through a YouTube tutorial:
  https://youtu.be/MfDZ1BrmnKM
  It discusses the difference between Emulated vs Shadow DOM in Angular too.
*/
@Component({
  selector: 'app-language',
  templateUrl: './language.component.html',
  styleUrls: ['./language.component.less'],
  encapsulation: ViewEncapsulation.Emulated
})
export class LanguageComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
