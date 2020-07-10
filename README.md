# Accurately Predicting Listed Sales Prices

##### Contributors:
##### - Jake Miller Brooks, brooksjacobm@gmail.com
##### - Nick Pardue, nickpardue@gmail.com
##### - Raven Welch, RavenNHWelch@gmail.com

### [Our Presentation]

![for_sale.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/for_sale.png)

### Our Business Problem
We sought out to create a tool that prospective home buyers could use to estimate how over/underpriced a listed house within Washington's King County is.

We were given data about King County, sourced from [Kaggle]. Using this data, we sought to find out the following:
- Which variable has the greatest impact on a house's price?
- How do geographical features, such as proximity to water, affect the sales price of a house?
- How can points of interest help predict sales price?
- To what degree does location play a role in predicting sales price?

### Data Sets
Our Sourced Data
- [House Sales in King County]

[Our Cleaned Data] 


### Cleaned Data Description
We analyzed a dataset of 21,597 houses, each containing the following *relevant* variables:
 - sqft_living
    - The home's total square footage.
 - lat
    - The home's latitudinal coordinate.
 - long
     - The home's longitudinal coordinate.
 - price
    - The price each home was sold at (our prediction target).
 - log_price
    - A function of log(price), used to give our pricing data a log normal distribution.
 

### Exploratory Analysis

 ##### Figure 1: sqft_living's Impact on Price
 - We found that, while holding all other variable constant, sqft_living accounted for 48.4% of the variation in price (R^2 = 0.484).
 
![sqft_r2.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/sqft_r2.png)

 ##### Figure 2: King County Houses by Price
 - We saw that houses seem to be more expensive around the water, as well as the city of Seattle, and decided to check measure the effect of distance from a single central location, next.
 
![houses_by_price](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/houses_by_price.png)

 ##### Figure 3: Price Predicted by Distance & Bearing from a Point of Interest (PoI)
- We calculated each house's distance and bearing from the Space Needle in downtown Seattle, and found that those variables in conjunction with sqft_living accounted for 70.5% of the variation in price (R^2 = 0.705), with all other variables constant. However, we believed that only using one PoI wouldn't be a fair representation of the many attractions spread out around King County that would add value to a house.
 
![space_needle_db_r2.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/space_needle_db_r2.png)

 ##### Figure 4: Using Zip Codes as Points of Interest
 - We thought about using zip codes as our additional PoI's, but decided that using the 70 different zip codes within the dataset wasn't going to be the best metric, as there are too many, and there is too much variation as to relative distance to other zip codes for each house within any given zip code.

![KC_zipcodes.gif](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/KC_zipcodes.gif)

##### Figure 5: Creating Geographic PoI's
- We created clusters of our houses based off of their lat/long values, and then used the centers of each of those "clusters" as our Geographic PoI's.

![lat_long_clusters.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/lat_long_clusters.png)

![geo_poi.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/geo_poi.png)

### Modeling

 ##### Figure 1: Results on Training Data Set
 - We split our original data set into a training and a test set (80:20), and then used our new model on the training set. We found out that in predicting the price of a house in King County, sqft_living, and a house's distance and bearing from the center of each of the above clusters, we could account for 80.4% of the variation in price, while holding all other variables constant. 
 ![price_by_geo_pois.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/price_by_geo_pois.png)
 
 ##### Figure 2: Residuals of Training and Test Sets
 - After plotting the residuals of the training and test sets, we concluded that our model succesfully accomplished what we set out to do, as it also accounted for 80% of the variation in the test set's price values. 
 ![train_test_residuals.png](https://github.com/RavenNHW/Mod_2_Project/blob/master/Images/train_test_residuals.png)




### Limitations
- We only had a single year's worth of data.
- The original listing date for each house was not included, nor was the original listing price. We would have loved to look into how long a house was on the market impacted its final sale price.
- Our information on proximity to water was limited, as only 0.68% of our original dataset were listed as being a "waterfront" location. Everything else was either "not a waterfront" location, or had a missing value.


### Future Research
- Find a more appropriate polynomial model, as our model did not perform as well on higher sales prices.
- Utilize a more advanced geostatistical technique, such as 'kriging' that could better define local neighborhoods and their differences, better than our six "geographical points of interest."
- With more years of data, try to explore any spatiotemporal effects that may be present within a longer range of dates.


### Reproducing Our Data
Download the [Original King County House Dataset] from our repo, and run the code found in our [Cleaning Script] to produce a copy of our final dataset. This can also be accomplished at the start of our [Technical Notebook].

### Repo Navigation


### Sources of Images Used in Presentation
- Slide 1: https://webassets.inman.com/wp-content/uploads/2018/01/shutterstock_752498263.jpg
- Slide 3: https://www.kingcounty.gov/~/media/operations/GIS/maps/vmc/images/zipcodes_586.ashx?la=en
- Slide 7: https://www.seattleandsound.com/wp-content/uploads/2019/03/mopop.jpg
- Slide 7: https://cdn.getyourguide.com/img/tour_img-1748533-148.jpg
- Slide 7: https://www.pikeplacefish.com/
- Slide 7: https://upload.wikimedia.org/wikipedia/commons/2/23/Space_Needle_2011-07-04.jpg
- Slide 8: https://cdn0.iconfinder.com/data/icons/social-media-essentials/30/Confuse-512.png
- Slide 11: https://www.dictionary.com/e/wp-content/uploads/2018/03/Thinking_Face_Emoji-Emoji-Island-300x300.png
- Slide 12: https://upload.wikimedia.org/wikipedia/commons/4/4a/Simple_kriging_80_50.png


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [our presentation]: <https://github.com/RavenNHW/Mod_2_Project/blob/master/presentation.pdf>
   [kaggle]: <https://www.kaggle.com/>
   [house sales in king county]: <https://www.kaggle.com/harlfoxem/housesalesprediction>
   [our cleaned data]: <https://github.com/RavenNHW/Mod_2_Project/blob/master/data/cleaned_df.pkl>
   [cleaning script]: <https://github.com/RavenNHW/Mod_2_Project/blob/master/data/cleaning_script.py>
   [original king county house dataset]: <https://github.com/RavenNHW/Mod_2_Project/blob/master/data/kc_house_data.csv>
      

   [technical notebook]: <>



