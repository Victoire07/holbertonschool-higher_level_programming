const button = document.getElementById('add_item');
const list = document.querySelector('.my_list');
button.addEventListener('click', () => {
  const nvoElement = document.createElement('li');
  nvoElement.textContent = 'Item';
  list.appendChild(nvoElement);
});
