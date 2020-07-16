import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { AccountComponent } from './account/account.component';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.less']
})
export class NavComponent {

  constructor(public dialog: MatDialog) { }

  ngOnInit() {
  }

  myAccount(): void {
    this.dialog.open(AccountComponent);
  }

}


