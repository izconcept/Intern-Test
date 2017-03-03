/**
* Created by IzKevin on 2017-03-03.
*/

// Stores the ordered list of books
var books;

// Used to sort an array of numbers
function sortNumber(a,b) {
    return a - b;
}

// Creates the table
function displayTable() {
    $(".removeable").remove()

    books.forEach(function(book) {
        $("table").append("<tr class='removeable'></tr>")
        Object.keys(book).forEach(function(key) {
            $("tr").last().append("<td>" + book[key] + "</td>")
        })
    })
}

function sortCatalog(header) {
    // Declare a dictionary that will store the contents as keys and their locations as values
    dic = {};

    for(i = 0; i < books.length; i++) {
        // If there are more one key has several books associated with it, store those index locations in an array
        if(dic[books[i][header]] instanceof Array) {
            dic[books[i][header]].push(i)
        }
        else if(books[i][header] in dic) {
            arr = [dic[books[i][header]], i]
            dic[books[i][header]] = arr;
        } else {
            dic[books[i][header]] = i;
        }
    }

    // Will be used as a lookup table to sort the new books list
    sorted = Object.keys(dic)

    // Check if it's a number or not to determine how to sort it
    if(isNaN(sorted[0])) {
        sorted.sort()
    } else {
        sorted.sort(sortNumber)
    }

    // Create a newBooks object to replace the books object with the correctly sorted version
    newBooks = []

    // Iteratively create the the new books object using the sorted list as a look up table
    for(i = 0 ; i < sorted.length; i++) {
        // If it's an array, iterate over that array
        if(dic[sorted[i]] instanceof Array) {
            for(j = 0; j < dic[sorted[i]].length ; j++) {
                newBooks.push(books[dic[sorted[i]][j]]);
            }
        } else {
            newBooks.push(books[dic[sorted[i]]]);
        }
    }

    books = newBooks;
    displayTable();
}

function reverseCatalog() {
    books.reverse();
    displayTable();
}