import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';


@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.less']
})
export class ResultComponent implements OnInit {

  dep_flight_data = {}


  constructor(private dep_flight_schedule: ApiService) {
    this.getDepFlightSchedule();
    this.dep_flight_data = {}
  }

  dep_flight_scheduleTime =[];
  dep_flight_updatedTime =[];
  dep_flight_status = [];
  dep_flight_termianl = [];
  dep_flight_gate = [];

  getDepFlightSchedule = () => {
    this.dep_flight_schedule.getDepFlightSchedule().subscribe(
      data => {
        this.dep_flight_data = data;
        console.log(this.dep_flight_data);

      }
    )
  };
  ngOnInit() {
  }

}
