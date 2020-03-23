import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EstimatedComponent } from './estimated.component';

describe('EstimatedComponent', () => {
  let component: EstimatedComponent;
  let fixture: ComponentFixture<EstimatedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EstimatedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EstimatedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
