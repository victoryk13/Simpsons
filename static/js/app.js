var quoteUrl = 'https://thesimpsonsquoteapi.glitch.me/quotes'
Plotly.d3.json(quoteUrl, function(error, response) {
if (error) return console.warn(error);

d3.select('.blockquote')
    .append('p')
    .attr('class', 'mb-0')
    .text(response[0]['quote'])

d3.select('.blockquote')
    .append('footer')
    .attr('class', 'blockquote-footer')
    .text(response[0]['character'])
});
