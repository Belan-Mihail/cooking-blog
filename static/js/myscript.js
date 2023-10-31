var category = 'food'
setInterval(function () {
$.ajax({
    method: 'GET',
    url: 'https://api.api-ninjas.com/v1/quotes?category=' + category,
    headers: { 'X-Api-Key': 'eNB8L18RTwR2FWqjPxFP9Q==swzK4Ndsww2aGENA'},
    contentType: 'application/json',
    success: function(result) {
        $('#quote').html(result[0].quote);
    },
    error: function ajaxError(jqXHR) {
        console.error('Error: ', jqXHR.responseText);
    }
})
}, 30000);


if ($('#quote').length > 0){
    $.ajax({
        method: 'GET',
        url: 'https://api.api-ninjas.com/v1/quotes?category=' + category,
        headers: { 'X-Api-Key': 'eNB8L18RTwR2FWqjPxFP9Q==swzK4Ndsww2aGENA'},
        contentType: 'application/json',
        success: function(result) {
            $('#quote').html(result[0].quote);
        },
        error: function ajaxError(jqXHR) {
            console.error('Error: ', jqXHR.responseText);
        }
    })
}

$('#quote-btn').click(function() {
	$.ajax({
        method: 'GET',
        url: 'https://api.api-ninjas.com/v1/quotes?category=' + category,
        headers: { 'X-Api-Key': 'eNB8L18RTwR2FWqjPxFP9Q==swzK4Ndsww2aGENA'},
        contentType: 'application/json',
        success: function(result) {
            $('#quote').html(result[0].quote);
        },
        error: function ajaxError(jqXHR) {
            console.error('Error: ', jqXHR.responseText);
        }
    })
});