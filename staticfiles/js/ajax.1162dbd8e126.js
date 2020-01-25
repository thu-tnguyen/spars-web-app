$(function() {
    var checkedCategories = [];
    $('input:checked').each(function(){
        checkedCategories.push($(this).val());
        alert(checkedCategories);
    });
    $.ajax({
        type: "GET",
        url: '/search/',
        data: {
            'q' : '',
            's' : 'all',
        },
        success: searchSuccess,
        dataType: 'html'
    }); // load initial browse page
    q = '';
    s = 'all'; // fix this
    tagline = '';
    $('#searchInput').keyup(function() {
        $.ajax({
            type: "GET",
            url: '/search/',
            data: {
                'q' : $('#searchInput').val(),
                's' : s,
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
    // $('#searchSelect').checked(function() {
    //     alert($(this).val());
    // });
    $( "select option:selected" ).each(function() {
        tagline += $( this ).text() + " ";
        console.log("tagline: " + tagline);
      });
    
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}

// remote: {
//     url: "{% url 'browse' %}",
//     replace: function(url, query) {
//         return url + "?q=" + query;
//     }
// },