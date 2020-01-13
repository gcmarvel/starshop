const source = document.querySelector('#tryname');
const result = document.querySelector('#showname');

const typeHandler = function(e) {
  console.log(result)
  result.innerHTML = e.target.value;
};

source.addEventListener('input', typeHandler);
source.addEventListener('propertychange', typeHandler);