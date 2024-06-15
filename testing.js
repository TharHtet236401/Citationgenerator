
let count = 0;

function createNewInput() {
    // Create a new input element
    var newInput = document.createElement('input');


    count++;

    // Add a class to the new input
    newInput.className = 'new-input'+ count;

    // Set input type to text (you can change it to other types as needed)
    newInput.type = 'text';
    
    console.log(newInput.className);
    // Append the new input to the body
    document.body.appendChild(newInput);
}
