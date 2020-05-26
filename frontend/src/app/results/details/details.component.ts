import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.less']
})
export class DetailsComponent {

  constructor(public dialogRef: MatDialogRef<DetailsComponent>) { }

  onClickOut(): void {
    this.dialogRef.close();
  }

}
