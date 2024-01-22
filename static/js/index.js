function deleteUser(event) {
    event.stopPropagation(); 
    var userID = event.currentTarget.getAttribute('data-user-id');
    window.location.href = '/delete/' + userID;
  }

function updateUser(event) {
    event.stopPropagation(); 
    var userID = event.currentTarget.getAttribute('data-user-id');
    window.location.href = '/update/' + userID;
  }


function toggleRow(event,row) {

var hiddenRow = row.nextElementSibling;
hiddenRow.classList.toggle('hide');

if (hiddenRow.classList.contains('hide')) {
    hiddenRow.querySelectorAll('td').forEach( td => td.style.display = 'none');
    
    //hiddenRow.querySelectorAll('td').style.display = 'none';
    } else {
    hiddenRow.querySelectorAll('td').forEach( td => td.style.display = 'table-cell');
    //hiddenRow.querySelector('td').style.display = 'table-cell';
    }
}

