$(function() {
    checkedCategories = [];
    queryList = window.location.search.split('&');
    if (queryList.length > 1) {
        q = queryList[0].substring(3).replace(/\+/g, ' ').trim();
        s = queryList[1].substring(2);
    } else {
        q = '';
        s = 'all'
    }

    $(".categoricalCheck").click(function(){
        checkedCategories = [];
        $('input:checked').each(function(){
            if (!checkedCategories.includes($(this).val())) {
                checkedCategories.push($(this).val());
            } 
        });
        console.log('curr: ' + checkedCategories);
        getData(s, q, checkedCategories);
    });
    getData(s, q, checkedCategories); // load initial browse page

    $('#searchInput').keyup(function() {
        q = $('#searchInput').val();
        getData(s, q, checkedCategories);
    });
    $('#searchSelect').change(function() {
        s = $('#searchSelect').val();
        
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

function getData(s, q, checkedCategories) {
    setInterval(function() {
        $.ajax({ 
            data: {
            'q' : q,
            's' : s,
            'cat' : checkedCategories.toString(),
            },
        });
    }, 400);
}
