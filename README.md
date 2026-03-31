<h1 align="center">🎬 Audience Sentiment & Box Office Performance Report</h1>

Industry Background & Business ContextThe Hollywood Landscape operates on a prevailing assumption: high review scores generate word-of-mouth, which directly translates to Box Office revenue. As production budgets soar past $200M and theaters face increasing competition from streaming platforms, studios can no longer afford to greenlight projects based purely on "gut feeling" or perceived script quality.

An in-depth analysis was conducted analyzing the top-grossing theatrical releases from 2023–2026, encompassing over 140 global releases and **$28.4 Billion** in total box office revenue. The objective of this report is to evaluate the true financial impact of post-release audience and critic sentiment, utilizing both descriptive analytics and machine learning.

<h2> Northstar Objectives:</h2>
<ul>
   <li>Sentiment Mapping: Quantify the leniency gap between professional critics (Rotten Tomatoes) and general audiences (IMDb).</li>
   <li>Financial Correlation: Determine the exact correlation between review scores, hype volume (total votes), and final global revenue.</li>
   <li>Predictive Viability: Evaluate if early sentiment metrics can accurately forecast final box office numbers using a Random Forest AI model.</li>
</ul>

<h2>Executive Summary</h2>
<h3><b>1. The Sentiment Landscape: Critics vs. Audiences</b></h3><br>

![Dashboard Screenshot](https://github.com/Nimna404/audience-sentiment-predictor/blob/61700399f88a6ea832966586b9c2064058c2ea97/Images/audience-sentiment-predictor.png)

<br>
<table border="1" align="center" width="100%">
  <tr>
     <th width="50%"><b>Key Insights: The Audience Forgiveness Gap</b></th>
     <th width="50%"><b>Strategic Recommendations</b></th>
  </tr>
    
  <tr>
    <td valign="top">
       <ul>
        <li><strong>1. Baseline Audience Leniency:</strong><br>Mapping Rotten Tomatoes against IMDb revealed a massive void in the bottom-right quadrant. Audiences rarely rate a blockbuster below 50/100, whereas critics frequently score the same films below 30/100.</li>
        <br>
        <li><strong>2. The "Popcorn" Effect:</strong><br>Several high-grossing films (e.g., Fast X, Mario Bros) achieved massive financial success despite "Rotten" critic scores, driven entirely by audience scores holding steady above the 65/100 threshold.</li>
        <br>
        <li><strong>3. Top-Heavy Revenue Concentration:</strong><br>The Top 5 grossing movies accounted for a disproportionately massive percentage of the $28.4B total, indicating a "winner-takes-all" theatrical environment.</li>
      </ul>
    </td>
    <td valign="top">
      <ul>
        <li><strong>1. Shift Marketing Focus:</strong><br>Studios should deprioritize "Critic Approved" marketing campaigns for tentpole blockbusters and pivot ad spend toward highlighting audience-driven metrics (e.g., verified audience scores, social media hype).</li>
        <br>
        <li><strong>2. The 65/100 Safety Net:</strong><br>Focus test screenings entirely on ensuring the general audience score clears the 65/100 threshold. Critic appeasement is statistically irrelevant to final revenue for IP-driven films.</li>
      </ul>
    </td>
  </tr>
</table>
<br>
<h3><b>2. Predictive Analytics: Forecasting the Box Office</b></h3>

A RandomForestRegressor machine learning model was deployed to test if final Box Office revenue could be accurately predicted using only three variables: RT Score, IMDb Rating, and IMDb Vote Volume.
<br>
<table border="1" align="center" width="100%">
  <tr>
    <th width="50%"><b>Model Performance Metrics</b></th>
    <th width="50%"><b>Business Interpretation & Next Steps</b></th>
  </tr>
  <tr>
    <td valign="top">
      <ul>
        <li><strong>R-Squared ($R^2$) Score: 0.34</strong><br>The model explains 34% of the variance in global box office revenue.</li>
        <br>
        <li><strong>Mean Absolute Error (MAE): $113.9M</strong><br>On average, the model's prediction deviates from the actual revenue by $114 million.</li>
        <br>
        <li><strong>Executive Simulation:</strong><br>Input: 88% RT, 75/100 IMDb, 500k Votes.<br>AI Prediction: $423,283,455</li>
      </ul>
    </td>
    <td valign="top">
      <ul>
        <li><strong>1. Sentiment &ne; Dollars:</strong><br>An $R^2$ of 0.34 mathematically proves that making a "good" movie does not guarantee a profitable one. Sentiment accounts for barely one-third of financial success.</li>
        <br>
        <li><strong>2. The Missing 66%:</strong><br>The majority of box office variance is driven by external operational factors. To achieve a production-grade forecasting model ($R^2 > 0.75$), Phase 2 of this architecture must integrate data for Production Budget, Marketing (P&A) Spend, and Existing IP/Franchise Status.</li>
      </ul>
    </td>
  </tr>
</table>
<br>
<h2>Dataset Structure & Data Dictionary</h2>
The data was extracted via a custom Python pipeline querying the TMDb and OMDb APIs. The raw JSON was cleaned, cast to appropriate data types, and scaled using pandas to create "the_audience_cleaned.csv" (142 rows).
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Column Name</th>
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Title</td>
      <td>String</td>
      <td>The official theatrical release title.</td>
    </tr>
    <tr>
      <td>Year</td>
      <td>Integer</td>
      <td>The year of theatrical release (2023 - 2026).</td>
    </tr>
    <tr>
      <td>IMDb_Rating</td>
      <td>Float</td>
      <td>General audience rating, scaled from 1-10 to 10-100 for 1:1 comparative analysis.</td>
    </tr>
    <tr>
      <td>IMDb_Votes</td>
      <td>Integer</td>
      <td>Total volume of user ratings; utilized as a proxy for cultural "hype" and engagement.</td>
    </tr>
    <tr>
      <td>Box_Office</td>
      <td>Integer</td>
      <td>Total global theatrical revenue in USD (cleaned of symbols and commas).</td>
    </tr>
    <tr>
      <td>RT_Score</td>
      <td>Integer</td>
      <td>Professional critic approval rating percentage (Rotten Tomatoes).</td>
    </tr>
  </tbody>
</table>
<br>
<h2>Technical Pipeline & Repository Structure</h2>
<h3>Tools Utilized:</h3>
<ul>
   <li>Python (Data Engineering): requests (API extraction), pandas (cleaning, NaN handling, regex), time (rate-limit throttling).</li>

   <li>Power BI (Visualization): Custom DAX measures, locked-axis scatter plotting, interactive tooltips.</li>

   <li>Scikit-Learn (Machine Learning): RandomForestRegressor, train_test_split (80/20).</li>
</ul>   
<br>

<div align="center">

👉🏼[Read the Comprehensive Technical Case Study on Notion here](https://www.notion.so/Audience-Sentiment-Predictor-333a927116ea80028305d3ffaf4ea8e6?source=copy_link)

© 2026 Nimna D Aluthgamage. All Rights Reserved. Data extracted from public API endpoints (TMDb, OMDb) for portfolio demonstration.

</div>


