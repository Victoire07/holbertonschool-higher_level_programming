const div = document.getElementById('toggle_header');
const header = document.querySelector('header');
div.addEventListener('click',() => {
  if (header.classList.contains('red')) {
    header.classList.remove('red')
    header.classList.add('green')
  }
});
