function searchTable() {
    // Get input field values and convert them to uppercase for case-insensitive search
    var inputStudentNo = document.getElementById("searchStudentNo").value.toUpperCase();
    var inputName = document.getElementById("searchName").value.toUpperCase();
    var inputEmail = document.getElementById("searchEmail").value.toUpperCase();
    var inputPhone=document.getElementById("searchPhone").value.toUpperCase();
    // Get the table and its rows
    var table = document.getElementById("studentTable");
    var rows = table.getElementsByTagName("tr");

    // Loop through each row in the table
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        var rowData = row.getElementsByTagName("td");
        // Initialize boolean variables to track found values
        var foundStudentNo = false;
        var foundName = false;
        var foundEmail = false;
        var foundPhone = false;

        // Loop through each cell (td) in the row
        for (var j = 0; j < rowData.length; j++) {
            var cell = rowData[j];

            // Check if the cell content contains the input value and set corresponding found flag
            if (j === 0 && cell.innerHTML.toUpperCase().indexOf(inputStudentNo) > -1) {
                foundStudentNo = true;
            }
            if (j === 1 && cell.innerHTML.toUpperCase().indexOf(inputName) > -1) {
                foundName = true;
            }
                        if (j === 2 && cell.innerHTML.toUpperCase().indexOf(inputEmail) > -1) {
                foundEmail = true;
            }
            if (j === 3 && cell.innerHTML.toUpperCase().indexOf(inputPhone) > -1) {
                foundPhone = true;
            }
        }

         // Show or hide the row based on the search result
        if (foundStudentNo && foundName && foundEmail && foundPhone) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    }
}

function resetSearch() {
    // Get the table and its rows
    var table = document.getElementById("studentTable");
    var rows = table.getElementsByTagName("tr");

    // Display all rows
    for (var i = 0; i < rows.length; i++) {
        rows[i].style.display = "";
    }

    // Reset search input field
    document.getElementById("searchStudentNo").value = "";
    document.getElementById("searchName").value = "";
    document.getElementById("searchEmail").value = "";
    document.getElementById("searchPhone").value = "";
}