import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { FormControl } from '@angular/forms';

/* Note: This is the first time I'm using the Shadow DOM 
  Here's a reference towhat I did through a YouTube tutorial:
  https://youtu.be/MfDZ1BrmnKM
  It discusses the difference between Emulated vs Shadow DOM in Angular too.
*/
@Component({
  selector: 'app-language',
  templateUrl: './language.component.html',
  styleUrls: ['./language.component.less'],
  // Encapsulation has to be disabled in order for the
  // component style to apply to the select panel.
  encapsulation: ViewEncapsulation.None
})
export class LanguageComponent implements OnInit {

  panelColor = new FormControl('red'); // TODO: Change internal styles of form option background (got stuck too long)

  constructor() { }

  ngOnInit() {
  }

}
