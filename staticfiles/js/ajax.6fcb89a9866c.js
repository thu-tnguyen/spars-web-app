$(function(){
    $('#search').keyup(function(){
        $.ajax({
            type: "GET",
            url: '/browse/',
            data: {
                'q': $('#searchInput').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]')
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}