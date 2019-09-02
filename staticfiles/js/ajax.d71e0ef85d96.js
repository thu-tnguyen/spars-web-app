$(function(){
    $('#searchInput').keyup(function(){
        $.ajax({
            type: "GET",
            url: '/browse/',
            data: {
                'q': $('#searchInput').val(),
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