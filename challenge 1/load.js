/**
* Created by IzKevin on 2017-03-03.
*/
$(function() {
    $.ajax({
        type: "GET",
        // Hosting JSON on personal server so I can retrieve it without having to run a local server to distribute files
        url: "http://izkevin.com/distributer/parsedXML.txt",
        success: function(data) {
            file = JSON.parse(data);

            // Create headers for the table
            headers = Object.keys(file['catalog']['book'][0]);
            headers.forEach(function(header) {
                $("#tHead").append("<th>"+header+"</th>");
            });

            // Store catalog in our global books variable
            books = file['catalog']['book'];

            displayTable()
        }
    })
})
// Collumn sorts the table based on the header that was clicked
$('table').on("click", "th", function() {

    // If table is already sorted by the selected header, reverse the order of the sort
    if($(this).hasClass("selected")) {
        reverseCatalog()
    } else {
        $('th').removeClass("selected")
        $(this).addClass("selected")
        header = $(this).text()
        sortCatalog(header);
    }
})