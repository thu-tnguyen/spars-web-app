// $(function(){
//     $('#searchInput').keyup(function(){
//         $.ajax({
//             type: "GET",
//             url: '/browse/',
//             remote: {
//                 url: "{% url 'browse' %}",
//                 replace: function(url, query) {
//                     return url + "?q=" + query;
//                 }
//             },
//             success: searchSuccess,
//             dataType: 'html'
//         });
//     });
// });

// function searchSuccess(data, textStatus, jqXHR)
// {
//     $('#search-results').html(data);
// }



$(document).ready(function() {
    $('#table_id').DataTable({
        dom: 'B<"clear">lfrtip',
        buttons: {
            name: "primary",
        }
    })
})