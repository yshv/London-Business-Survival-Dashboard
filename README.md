
# COMP0034 Coursework 1 template repository
## Youtube link to demo 

https://www.youtube.com/watch?v=oSYrUlxZnpY
## Github Link

https://github.com/ucl-comp0035/coursework-1-yshv
## Specific techniques used:

- The linter pylint has been used throughout to maintain code quality and readability 
- The github issues function has been used breifly, however was not found to be particularly useful when working as an individual. 

### Questions to be answered using the dataset

- 1) Which areas are fastest growing in terms of business survivability. (May have cheaper rent, expenditure etc).
   Areas with the highest rate of increase of survivability (highest 1st differential) against time.
      > Pie chart?, maybe 5-8 highest (maybe too cluttered) 
      > Sideways bar chart, maybe 5 highest (much cleaner) 
      > For a broader sense you could use a heat map / Choropleth Map 
      
- 2) Which areas are best in terms of business survivability. (To start / branch new business).
      > Pie chart
      > For a broader sense you could use a heat map / Choropleth Map 
      > For specifics use line chart to compare multiple boroughs across years 

- 3) Which areas require government assistance through business grants, changes in tax policy etc. (Low business survivability/ fastest reducing).
      > Pie chart
      > Line chart to see which deaths / survival percentage are decreasing fastest
      > Choropleth 

- 4) Which areas have most business deaths? (Swoop in and buy cheap equipment from failed businesses).
      > Pie chart to quickly check all in terms of deaths/total deaths 
      > Line chart to see which deaths / survival percentage are decreasign fastest
      > Choropleth Map 

- 5) How successful previous government initiatives/ policies have been for small businesses? (Did business survivability increase after implementation?
      > Use pie chart to check if the ratio of deaths compared to all the other boroughs has decreased
      > Use line chart to clearly see if there has been a decrease 
### Target audience

[MP's](MP_persona.pdf)\
[New business owners](new_business_persona.pdf)
[Business owners looking to expland](expansion_business_persona.pdf)
## Visualisation Explaination 
### Choropleth Map 

The target audience for this graph is both MP's (policy makers) and both new and established business owners. The primary use of this visualisation is to give a quick overview of all the London boroughs for every data metric we have. 

As I plan to implement all of the data metrics for the visualisation I believe it will answer questions 1-5, **however** it will only do so in a broad sense, as it would be slightly difficult to compare multiple boroughs in great details and will only give a good overall understanding. 

This visualisation will use the entirety of the dataset and I plan to give the user the option an overview for every metric, survival rates, deaths, births and active business. 

A very important aspect of the choropleth is the colour spectrum decision, as we have great outliers in deaths, active and births due to Westminster much larger in these aspects than the other boroughs. Another important aspect is the colour choice itself, as business deaths are viewed as a negative often represented by red orange etc, and business births are seen as a positive green blue etc, therefore, it would be a good idea to change the colour spectrum for the different data types. 

https://medium.com/nightingale/how-to-choose-the-colors-for-your-data-visualizations-50b2557fa335

Evaluation:

The choropleth map is very useful for getting an overview of the London boroughs for various data types, and the decision to make it a animation type based on time helped join the data together to show a story of sorts over multiple years, rather than manually changing from year to year. However, the user is able to hover over boroughs to get more detailed numbers and other datapoints. 

However, there are some issues with this visualisation. Firstly, the colour spectrum was a very difficult choice due to Westminster being a great outlier in regards to births, deaths and active metrics. Perhaps, I should have changed my data to be percentage change as birth, death and active rates rather than flat numbers. This would have been better to show a change across years also. 

Another issue with this visualisation is the time delay between generating the images. This is most likely due to the animation needing to rendered every time the data type is changed and the large dataset being used every time. This could be resolved by creating smaller subset dataframes for each visualisation rather than loading the entire thing every time. This could also be solved by not using dash and using a framework which allows for server side rendering such as next.js allowing for a significantly smoother experience for generating the animation. The decision to use different colour schemes for different data types was also very effective, to clearly show different types of data are being viewed.

### Multi line chart

The target audience for this map is again both MP's and business owners. As this visualisation type allows for speciic comparison between different boroughs. 

As I, once again, intend to integrate this chart with all the data metrics (thus requires all data) I have this chart can answer questions 1-5, however to varying degrees. It will be more useful for check specifics rather than getting a broad overview of all london boroughs. However, you will be able to add as many boroughs to the chart, but this will lead to cluttered data, thus suited more to comparing specific boroughs. 

The chart type is very useful to all named personas, due to its simplicity. This chart will show you the data (depends on selection) across multiple years and will allow for multiple boroughs to be added for comparison. This graph is relatively simple, therefore does not require too much explaination. The colours are distinct for the boroughs being compared, and the graph is accompanied by a lengend as well as hover data to show the exact numbers and which colour represents which borough. 

Evaluation:

Due to the simplicity of this graph, there is very little that can go wrong. The graph allows the user to pick specific boroughs and compare them. Giving a legend and allowing for further detail when the cursor highlights data. Overall, this visualisation easily meets the requirements of the MP's and business owners. This graph could be improved by having more data types such as rate of change, rather than flat numbers and percentages, however this can be inferred by the user. 
### Multi line chart

The target audience for this visualisation is primarily MP's as it allows them to see whicha areas have a greater proportion of deaths, reduced births. This chart allows for a quick indepth comparison, which is not provided by the choropleth (as the choropleth is used more so to paint an overall picture). This graph type answers questions, 3,4 and 5 as it shows which areas are the worst/best by births, deaths and active businesses. It does not anwer 1 or 2, due to not being able to show survival rates, however, these can be inferred. 

Only the births, deaths and active data types are being used with this graph as they are the only ones compatable. Due to large number of boroughs this visualisation suffers from being cluttered and overwhelming the user, therefore, I have decided to get rid of the very long legend which shows colours very similar to eachother and reply more so on the hover function which gives the boroughs name, allowing for a more dynamic experience. 


Evaluation:

This visualisation suffers from being overshadowed by the more versitile choropleth animation as it is able to show less types of data. However, it does allow for all the percentages to be seen in one go rather than requiring the hover with their cursor (choropleth). This graph, as expected, does suffer from cluttering, however the decision to remove the redundant legened was very helpful. This visualisation could also be aided by being turned into a animation, as this would allow use to see the shift in deaths, birth and active shares amoung the boroughs. 

https://www.bluegranite.com/blog/data-visualization-remove-chart-clutter-and-focus-on-the-insights


