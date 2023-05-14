
const mySelect = document.getElementById('car_color')
const output = document.getElementById('exibir_cor');

mySelect.addEventListener('change', function() {
  const selectedOption = mySelect.options[mySelect.selectedIndex].value;
  const existing_class = output.classList[0];
  output.classList.remove(existing_class);
  output.classList.add(`p_${selectedOption}`);
});