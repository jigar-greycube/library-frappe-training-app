// const { tsParticles } = require("@tsparticles/engine");
// const { loadStarShape } = require("@tsparticles/shape-star");

import { tsParticles } from "@tsparticles/engine";
import { loadStarShape } from "@tsparticles/shape-star";

var button = document.querySelector(".confetti-btn-ts")
button.addEventListener("click", function () {
  (async () => {
    console.log("Function Executed11",tsParticles);
    await loadStarShape(tsParticles);
  })();

  // const defaults = {
  //   spread: 360,
  //   ticks: 50,
  //   gravity: 0,
  //   decay: 0.94,
  //   startVelocity: 30,
  //   shapes: ["star"],
  //   colors: ["FFE400", "FFBD00", "E89400", "FFCA6C", "FDFFB8"],
  // };
  
  // function shoot() {
  //   confetti({
  //     ...defaults,
  //     particleCount: 40,
  //     scalar: 1.2,
  //     shapes: ["star"],
  //   });
  
  //   confetti({
  //     ...defaults,
  //     particleCount: 10,
  //     scalar: 0.75,
  //     shapes: ["circle"],
  //   });
  // }
  
  // setTimeout(shoot, 0);
  // setTimeout(shoot, 100);
  // setTimeout(shoot, 200);


  console.log("Function Executed");

})

console.log("Bundle File Excessed")

