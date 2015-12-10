var PageSummaryUtils = {
    removeHighlighting: function(sourceTag) {
        sourceTag.html(sourceTag.html().replace(
                /<span class="highlight">(&lt;\/?\s*[a-zA-Z0-9]+?\s*?.*?&gt;)<\/span>/gim,
            "$1"));
    },

    applyHighlighting: function(sourceTag, tagName) {
        var pattern = new RegExp('&lt;\/{0,1}\\s*' + tagName + '(\\s+?.*?)*?&gt;', 'gim');
        sourceTag.html(sourceTag.html().replace(
            pattern,
            '<span class="highlight">$&</span>'));
    },

    // Creates a tabular summary of tags in the page
    buildSummaryContainer: function (tagCounts) {
        if (!tagCounts) {
            return;
        }
        var summaryContainer = $('<div class="container source"></div>');
        var summaryHeader = $('<div class="header"><h2>Tag Summary<h2></div>');
        var headerRow = $('<div class="row">' +
                          '<div class="col-sm-4 text-center">' +
                          '<h4>Tag</h4>' +
                          '</div>' +
                          '<div class="col-sm-4 text-center">' +
                          '<h4>Count</h4>' +
                          '</div>' +
                          '</div>');
        summaryContainer.append(summaryHeader);
        summaryContainer.append(headerRow);
        _.each(_.pairs(tagCounts), function(tag) {
            var name = tag[0];
            var count = tag[1];
            var tagSummary = $('<div class="row">' +
                               '<div class="col-sm-4 text-center">' +
                               '<a href class="tag-name">' + name + '</a>' +
                               '</div>' +
                               '<div class="col-sm-4 text-center">' +
                               '<span class="tag-count">' + count + '</span>' +
                               '</div>' +
                               '</div>');
            summaryContainer.append(tagSummary);
        });
        return summaryContainer;
    },

    // Creates a formatted display for page html
    buildSourceContainer: function(source) {
        if (!source) {
            return;
        }
        var sourceContainer = $('<div class="container source"></div>');
        var sourceHeader = $('<div class="header"><h2> Page Source </h2></div>');
        sourceContainer.append(sourceHeader);
        var sourceWrapper = $('<pre class="page-source-container">' +
                              '  <code class="page-source">' +
                              '  </code>' +
                              '</pre>');
        sourceWrapper.find('.page-source').text(source);
        sourceContainer.append(sourceWrapper);
        return sourceContainer;
    },
};
