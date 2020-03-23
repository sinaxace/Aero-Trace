import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WrittenreviewComponent } from './writtenreview.component';

describe('WrittenreviewComponent', () => {
  let component: WrittenreviewComponent;
  let fixture: ComponentFixture<WrittenreviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WrittenreviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WrittenreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
