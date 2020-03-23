import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DepartComponent } from './depart.component';

describe('DepartComponent', () => {
  let component: DepartComponent;
  let fixture: ComponentFixture<DepartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DepartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DepartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
