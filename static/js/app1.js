// function initial() {
  
//     var selector=d3.select("#selDataset");
  
//     updating the dropdown menu

d3.select("#btn-twitter").on("click",updateData);

function updateData() {


    

    d3.json("/twitter_data").then(function(data) {
        console.log(data);
        var negative_time=data[0].negative;
        var positive_time=data[0].positive;
        var sentiment=data[1];
        var example_tweets=data[2].trump_tweets;
        
    
        updatePanel(example_tweets);
        updateBar(sentiment);
        updateLine(negative_time, positive_time);
        
    
    
            
    });
    
}



function updatePanel(newdata) {
    var panel_select=d3.select("#sample-metadata");
    d3.select("#sample-metadata").html("");
    //name=[]
    name1=[]
    frequency=[]
    for (const [key, value] of Object.entries(newdata)) {
        //name.push(key) 
        frequency.push(value)
        name1.push(key)
    }
    
    var i;
    for (i = 0; i < name1.length; i++) {
        panel_select
        .append("p")
        .text(`${name1[i]}: ${frequency[i]}`)
    }
}

function updateBar(newdata) {
    //name=[]
    sentiment=[]
    frequency=[]
    for (const [key, value] of Object.entries(newdata)) {
        //name.push(key) 
        frequency.push(value)
        sentiment.push(key)
    }

    var trace1 ={
        x: frequency,
        y: sentiment,
        name: "Trump Charts",
        type: "bar",
        orientation: "h"
    };
    
    var layout = {
        title: 'Sentiment',
        showlegend: false,
        hovermode: 'closest',
        xaxis: {title:"Percentage" },
        yaxis: {title:"Sentiment" },
        margin: {t:30}
    };
    
    
    var bar_chart = [trace1];
    
    
    Plotly.newPlot("bar", bar_chart, layout);


   
}

function updateLine(negative, positive){
    var time=[];
    var frequency_neg=[];
    for (const [key, value] of Object.entries(negative)) {
        time.push(key) 
        frequency_neg.push(value)
    
    }

    var frequency_pos=[];

    for (const [key, value] of Object.entries(positive)) {
        frequency_pos.push(value)
    
    }
    
    var trace1 = {
        x: time,
        y: frequency_pos,
        type: 'scatter',
        name: 'Positive Sentiment'
    };
      
    var trace2 = {
        x: time,
        y: frequency_neg,
        type: 'scatter',
        name: 'Negative Sentiment'
    };


    var data = [trace1, trace2];

    Plotly.newPlot('line', data);
}

updateData();



