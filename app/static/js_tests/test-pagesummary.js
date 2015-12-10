QUnit.test( "Test applyHighlighting", function( assert ) {
    var sourceTag = $('<pre><code class="page-source">&lt; madeUpTag someprop &gt;</code></pre>');
    PageSummaryUtils.applyHighlighting(sourceTag, 'madeUpTag');
    var modifiedHtml = sourceTag.find('.page-source').html();
    assert.equal(modifiedHtml, '<span class="highlight">&lt; madeUpTag someprop &gt;</span>', 'Highlighting applied')
});

QUnit.test( "Test removeHighlighting", function( assert ) {
    var sourceTag = $('<pre><code class="page-source">&lt; madeUpTag someprop &gt;</code></pre>');
    PageSummaryUtils.applyHighlighting(sourceTag, 'madeUpTag');
    var modifiedHtml = sourceTag.find('.page-source').html();
    assert.equal(
        sourceTag.find('.page-source').html(),
        '<span class="highlight">&lt; madeUpTag someprop &gt;</span>',
        'Highligting applied');
    PageSummaryUtils.removeHighlighting(sourceTag);
    assert.equal(
        sourceTag.find('.page-source').html(),
        '&lt; madeUpTag someprop &gt;',
        'Highligting removed');
});

QUnit.test( "Test buildSummaryContainer", function( assert ) {
    var tagCounts = {
        div: 4,
    };
    var summaryContainer = PageSummaryUtils.buildSummaryContainer(tagCounts);
    assert.equal(summaryContainer.find('.tag-name').html(), 'div', 'Tag name');
    assert.equal(summaryContainer.find('.tag-count').html(), '4', 'Tag count');
});

QUnit.test( "Test buildSourceContainer", function( assert ) {
    var source = '<html><head><title>Test HTML</title></head><body><h1>Test HTML</h1></body></html>'
    var sourceContainer = PageSummaryUtils.buildSourceContainer(source);
    assert.equal(
        sourceContainer.find('.page-source').html(),
        source.replace(/</g, '&lt;').replace(/>/g, '&gt;'),
        'Page Source View');
});

