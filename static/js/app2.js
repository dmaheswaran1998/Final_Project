// function initial() {
  
//     var selector=d3.select("#selDataset");
  
//     updating the dropdown menu

var selector=d3.select("#selDataset");

d3.select("#btn-twitter").on("click",updateData);

function updateData() {


    

    d3.json("/twitter_data").then(function(data) {
        console.log(data);
        leaders=data[0];
        for (const [key] of Object.entries(leaders)) {
            selector
            .append("option")
            .append("value")
            .text(`${key}`)
            .property("value", name)
            
        }
    
    
        initial_tweet_text=data[2].Andrews;
        initial_tweet_sentiment=data[1].Andrews;
        initial_tweet_time=data[0].Andrews;
    
        updatePanel(initial_tweet_text);
        updateBar(initial_tweet_sentiment);
        updateLine(initial_tweet_time);
        
    
    
            
    });
    
}

d3.select("#selDataset").on("change", optionChanged);
  
function optionChanged() {
    var selector=d3.select("#selDataset");
  //Assign the value of the dropdown menu option to a variable
    var dropdown_value = selector.property("value");

    d3.json("/twitter_data").then(function(data) {
        tweet_text=data[2];
        tweet_sentiment=data[1];
        tweet_time=data[0];
  
        for (const [key, value] of Object.entries(tweet_text)) {
            if (key==dropdown_value){
                
                
                var name=value;

                updatePanel(name)

            }    
        
        }

        for (const [key, value] of Object.entries(tweet_sentiment)) {
            if (key==dropdown_value){
                
                var sentiment=value;

                updateBar(sentiment);

            }  
           
            
        }
        
        for (const [key, value] of Object.entries(tweet_time)) {
            if (key==dropdown_value){
                
                var time=value;



                updateLine(time);

            }  
           
            
        }
    
    });   
    


}

function updatePanel(newdata) {
    var panel_select=d3.select("#sample-metadata");
    d3.select("#sample-metadata").html("");
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
        marker:{
            color: ['rgba(222,45,38,0.8)', 'rgba(0, 230, 64, 1)',]
        },
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

function updateLine(newdata){
    var time=[];
    var frequency_neg=[];
    for (const [key, value] of Object.entries(newdata.negative)) {
        time.push(key) 
        frequency_neg.push(value)
    
    }

    var frequency_pos=[];

    for (const [key, value] of Object.entries(newdata.positive)) {
        frequency_pos.push(value)
    
    }
    
    var trace1 = {
        x: time,
        y: frequency_pos,
        type: 'scatter',
        mode: 'markers',
        mode: 'markers',
        name: 'Positive Sentiment',
        line: {
            color: 'rgba(0, 230, 64, 1)',
            width: 2
        }
    };
      
    var trace2 = {
        x: time,
        y: frequency_neg,
        type: 'scatter',
        name: 'Negative Sentiment',
        line: {
            color: 'rgba(222,45,38,0.8)',
            width: 2
        }
    };

    var layout = {
        title: 'Time Series Graph',
        xaxis: {
          title: 'Time',
          showgrid: false,
          zeroline: false
        },
        yaxis: {
          title: 'Frequency',
          showline: false
        }
    };

    var data = [trace1, trace2];

    Plotly.newPlot('line', data, layout);
}



