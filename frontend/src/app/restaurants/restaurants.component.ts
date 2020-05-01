import { Component } from '@angular/core';
import { trigger, keyframes, animate, transition } from '@angular/animations'; // browser animation imports
import * as slideKey from './slide-keyframes'; // the animate.css library import

@Component({
  selector: 'app-restaurants',
  templateUrl: './restaurants.component.html',
  styleUrls: ['./restaurants.component.less'],
  animations: [ // here is where we define our animations from animate css library
    // first we have an animation trigger called cardAnimator
    trigger('cardAnimator', [
      /* Animation Trigger Descriptions:
          - Every time it's triggered, the animation moves on to the different transition states below.
          - The star * in transition's first arg is a wildcard for any state that transitions. If it fits the wildcard, it runs the 2nd arg.
          - transition() second arg, animate(), has a first arg of 500 milliseconds with the kf import used in keyframe()
      */
      transition('* => slideOutLeft', animate(400, keyframes(slideKey.slideOutLeft))),
      transition('* => slideInLeft', animate(400, keyframes(slideKey.slideInLeft)))
    ])
  ]
})
export class RestaurantsComponent {

  // TODO: grab ratings through service API and load them dynamically into Angular.
  diner = {
    image: "../../assets/images/mcdonalds.jpg",
    rating: [true, true, false, false, false], // for now, just a fixed boolean array
    name: "McDonalds",
    terminal: 1,
    reviews: 0
  };

  animationState: string; // this property takes note of the component's current animation

  /**
   * @method startAnimation simply starts a new animation if the animation state is an empty string.
   * @param state contains the new animation state as a string.
   */
  startAnimation() {
    console.log("sliding");
    if (!this.animationState) {
      this.animationState = "slideOutLeft";
    }
  }

  /**
   * @method resetAnimationState resets the animation state to 
   *              an empty string.
   */
  resetAnimationState() {
    if (this.animationState === "slideOutLeft") { // if doing a slide out animation, do a slide-in
      // editing restaurant details (will make more dynamic as a TODO)
      this.diner.image = "../../assets/images/tim-hortons.png";
      this.diner.rating[2] = true;
      this.diner.name = "Tim Hortons";
      this.diner.terminal = 2;
      this.diner.reviews = 44;

      // finally slide everything back in
      this.animationState = 'slideInLeft';
    } else
      this.animationState = '';
  }

}
