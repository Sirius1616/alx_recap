const myHeading = document.querySelector("#Heading1");
const myButton = document.querySelector("#Button");

let count = 1;

myButton.onclick = () => {
  myButton.textContent = "Try again later";
  myHeading.textContent = `${count} clicks so far`

  count += 1;
};



