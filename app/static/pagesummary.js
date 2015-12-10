$(document).ready(function() {
    $('.error').hide();
    $('#summary-spinner').hide();

    $(document).ajaxStart(function(){
        $('#summary-spinner').show();
    });
    $(document).ajaxStop(function(){
        $('#summary-spinner').hide();
    });

    // Handle highlighting of source
    var SCROLLTOP_OFFSET = 100;
    $('body').on('click', '.tag-name', function(event) {
        event.preventDefault();
        var sourceTag = $('.page-source');
        PageSummaryUtils.removeHighlighting(sourceTag);

        var tagName = $(this).html();
        PageSummaryUtils.applyHighlighting(sourceTag, tagName);
        $('html, body').animate({
        scrollTop: $(".highlight").offset().top - SCROLLTOP_OFFSET
    }, 200);

    });

    // Add summary of page and page source
    function buildSummary(response) {
        if (!response || !response.summary || !response.source) {
            $('.error').show();
            return;
        }
        $('.error').hide();
        $('.summary').remove();
        $('.source').remove();

        var summaryContainer = PageSummaryUtils.buildSummaryContainer(response.summary);
        $('body').append(summaryContainer);

        var sourceContainer = PageSummaryUtils.buildSourceContainer(response.source);
        $('body').append(sourceContainer);
    };

    // Handle form submission via AJAX
    $('.form').submit(function(event) {
        event.preventDefault();
        $.ajax({
            url: '/pagesummary',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                buildSummary(response);
            },
            error: function(error) {
                console.log(error);
                $('.error').show();
            }
        });
    });

});
