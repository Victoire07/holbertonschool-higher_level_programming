const red_header = document.querySelector('#red_header');
const header = document.querySelector('header');
red_header.addEventListener('click', () => {
  header.classList.add('red');
});
