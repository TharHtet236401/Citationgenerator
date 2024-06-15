function generateCitation() {
    // Get input values
    const author = document.getElementsByClassName('writer')[0].value;
    const publicYear = document.getElementById('publicYear').value;
    const title = document.getElementById('title').value;
    const website = document.getElementById('website').value;
    const link = document.getElementById('link').value;
    const date = document.getElementById('date').value;
   
    // Generate citation  
    const citation = `${formatAuthorName(author)} (${publicYear}) '${title}', '${website}', Available at: '${link}' (Accessed: ${date})`;

    // Display the result
    const citationResult = document.getElementById('citationResult');
    citationResult.textContent = `${citation}`;
}

function formatAuthorName(fullName) {
    // Split the full name into first and last names
    const names = fullName.split(' ');

    // Check if there are at least two names
    if (names.length >= 2) {
        // Extract the first letter of the first name
        const firstInitial = names[0].charAt(0).toUpperCase();
        const secondInitial = names[names.length-1].charAt(0).toUpperCase();
        const middleInitial = names.slice(1, -1).join(" ").charAt(0).toUpperCase();
        

        
        // Combine the last name and the first initial
        return `${secondInitial +names[names.length - 1].slice(1)},${middleInitial}.${firstInitial}.`;
    } else {
        // If only one name, return as is
        return fullName;
    }
}

function copyToClipboard() {
    // Get the text content of the citationResult div
    var citationResult = document.getElementById("citationResult");
    var range = document.createRange();
    range.selectNode(citationResult);

    // Create a selection and select the range
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);

    // Execute 'copy' command
    document.execCommand('copy');

    // Deselect the text
    selection.removeAllRanges();

    // Alert the user
    alert("Copied the citation to clipboard");
}


