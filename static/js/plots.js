// data is in the data folder under json_data.js
function graphgrades(dataSet){
  // Trace for Grades
  var trace1 = {
    x: dataSet.map(row => row.character_name),
    y: dataSet.map(row => row.Flesch_Kincaid_grade),
    text: dataSet.map(row => row.occupation),
    type: "bar"
  };

  var data = [trace1];

  var layout = {
    title: "Top 50 Character's Flesch_Kincaid Grade",
    barmode: "group"
  };

  return Plotly.newPlot("summaryChart",data, layout);
};


function graphReadability(dataSet){
  // Trace for Readability
  var trace2 = {
    x: dataSet.map(row => row.character_name),
    y: dataSet.map(row => row.Flesch_readability),
    text: dataSet.map(row => row.occupation),
    type: "bar"
  };

  var data = [trace2];

  var layout = {
    title: "Top 50 Character's Readability",
    barmode: "group"
  };

  return Plotly.newPlot("readabilityChart",data, layout);
};

function graphWordCount(dataSet){
  // Trace for word count
  var trace3 = {
    x: dataSet.map(row => row.character_name),
    y: dataSet.map(row => row.word_count),
    type: "bar"
  };

  var data = [trace3];

  var layout = {
    title: "Word Count",
    barmode: "group"
  };

  return Plotly.newPlot("wordChart",data, layout);
};

function graphSyllableCount(dataSet){
  // Trace for syllables
  var trace4 = {
    x: dataSet.map(row => row.character_name),
    y: dataSet.map(row => row.syllable_count),
    type: "bar"
  };
  var data = [trace4];

  var layout = {
    title: "Syllable Count",
    barmode: "group"
  };

  return Plotly.newPlot("syllableChart",data, layout);
}

graphgrades(dataSet)
graphReadability(dataSet)
graphWordCount(dataSet)
graphSyllableCount(dataSet)


