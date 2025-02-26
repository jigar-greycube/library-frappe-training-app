// JS Confetti
import JSConfetti from 'js-confetti'

const jsConfetti = new JSConfetti()

jsConfetti.addConfetti()

var button = document.querySelector(".confetti-btn");
button.addEventListener("click", function(){
    jsConfetti.addConfetti()
});
