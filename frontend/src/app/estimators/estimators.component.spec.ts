import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EstimatorsComponent } from './estimators.component';

describe('EstimatorsComponent', () => {
  let component: EstimatorsComponent;
  let fixture: ComponentFixture<EstimatorsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EstimatorsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EstimatorsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
