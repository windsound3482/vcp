import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl} from '@angular/forms';


@Component({
  selector: 'app-map-page',
  templateUrl: './map-page.component.html',
  styleUrls: ['./map-page.component.scss']
})
export class MapPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  range = new FormGroup({
    start: new FormControl(),
    end: new FormControl(),
  });

}
