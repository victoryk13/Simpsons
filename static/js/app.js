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


var namesUrl = "top_50_character";
Plotly.d3.json(namesUrl, function(error, response) {
    if (error) return console.warn(error);

    for (var i = 0; i < response.length; i++){
        d3.select("#simpsonsDropdown")
              .append('option')
              .attr('value', response[i])
              .text(response[i])
    }

});

// function getSimpsonsData() {
//         sampleValue = document.getElementById("simpsonsDropdown").value;

//         var endPointCharacterData = '/character_metadata/' + sampleValue
//         Plotly.d3.json(endPointCharacterData, function(error, response) {

//             if (error) return console.warn(error);

//             console.log(response[0]['Occupation'])

//         });
// };
