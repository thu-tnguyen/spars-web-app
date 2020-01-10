$(function() {
    checkedCategories = [];
    q = '';
    s = 'all'; // fix this
    $(".categoricalCheck").click(function(){
        checkedCategories = [];
        $('input:checked').each(function(){
            if (!checkedCategories.includes($(this).val())) {
                checkedCategories.push($(this).val());
            } 
        });
        console.log('curr: ' + checkedCategories);
        $.ajax({ data: getData() });
    });
    $.ajax({ data: getData() }); // load initial browse page

    $('#searchInput').keyup(function() {
        q = $('#searchInput').val();
        $.ajax({ data: getData() });
    });
    $('#searchSelect').change(function() {
        s = $('#searchSelect').val();
        $.ajax({ data: getData() });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}

$.ajaxSetup({
        type: "GET",
        url: '/search/',
        success: searchSuccess,
        dataType: 'html',
        traditional: true,
});

function getData() {
    // alert(checkedCategories);
    return {
        'q' : q,
        's' : s,
        'cat' : checkedCategories.toString(),
    };
}

// remote: {
//     url: "{% url 'browse' %}",
//     replace: function(url, query) {
//         return url + "?q=" + query;
//     }
// },