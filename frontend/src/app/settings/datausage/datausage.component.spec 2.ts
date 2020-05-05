import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatausageComponent } from './datausage.component';

describe('DatausageComponent', () => {
  let component: DatausageComponent;
  let fixture: ComponentFixture<DatausageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatausageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatausageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
