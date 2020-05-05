
/* Note:
        We're pretty much translating css keyframe animations
        into Angular 8 code. Angular might make a css parser in the future.
    Tutorial: https://fireship.io/lessons/hammerjs-angular-5-animations-for-mobile-gestures-tutorial/

    Original animate.css keyframes: https://github.com/daneden/animate.css/tree/master/source
    Compare css keyframes with exported keyframe array to understand again.
*/
import { style } from "@angular/animations";

// all we're doing is exporting variables that defines keyframes to be used in the app's animation
export const slideOutLeft = [
    style({ transform: 'translate3d(0, 0, 0)', offset: 0 }),
    style({ visibility: 'hidden', transform: 'translate3d(-150%, 0, 0)', offset: 1 }) // the offset 1 is 100% within css keyframes
];

export const slideInLeft = [
    style({ transform: 'translate3d(150%, 0, 0)', visibility: "visible", offset: 0 }),
    style({ transform: 'translate3d(0, 0, 0)', offset: 1 }) // the offset 1 is 100% within css keyframes
];