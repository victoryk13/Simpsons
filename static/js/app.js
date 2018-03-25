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


var namesUrl = "top_50_characters";
Plotly.d3.json(namesUrl, function(error, response) {
    if (error) return console.warn(error);

    for (var i = 0; i < response.length; i++){
        d3.select("#simpsonsDropdown")
              .append('option')
              .attr('value', response[i])
              .text(response[i])
    }

});

function appendInnerHMTL(response) {

              d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Character Name')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Character Name'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('First Appearance')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['First Appearance'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Flesch Readability')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Flesch Readability'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Flesch-Kincaid Grade')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Flesch-Kincaid Grade'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Gender')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Gender'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Hair')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Hair'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Occupation')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Occupation'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Sentence Count')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Sentence Count'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Syllable Count')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Syllable Count'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Word Count')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Word Count'])

            d3.select("#metaList")
              .append('li')
              .attr('class', 'list-group-item d-flex justify-content-between align-items-center')
              .text('Status')
              .append('span')
              .attr('class', 'badge badge-primary badge-pill')
              .text(response[0]['Status'])


}

function getSimpsonsData() {

        sampleValue = document.getElementById("simpsonsDropdown").value;

        document.getElementById("metaList").innerHTML = ""

        var endPointCharacterData = '/character_metadata/' + sampleValue
        Plotly.d3.json(endPointCharacterData, function(error, response) {

            if (error) return console.warn(error);

            appendInnerHMTL(response)

        });
};

