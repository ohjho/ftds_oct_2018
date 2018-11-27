---?image=https://source.unsplash.com/c4XoMGxfsVU/
### Using Machine Learning to Predict Hong Kong Property Prices
+++?image=https://source.unsplash.com/c4XoMGxfsVU/
## 1. The question
@ul
* How much is where I am worth right now?  
* Is the price advertised on ad fair??
* If I want to live in **_[X]_ neigborhood** with **_[Y]_ square-foot worth of space** in a **_[Z]_-year-old building**. How much money do I need???
@ulend
+++?image=https://source.unsplash.com/c4XoMGxfsVU/
#### A Supervised Regression Machine Learning Problem
@ul
* Target provided in Training
* Target value is continuous, not discrete
@ulend
---
@title[Data Science Workflow]
#### Data Scince Workflow
The eight-fold path!
![Data Science Workflow by IBM](https://developer.ibm.com/dwblog/wp-content/uploads/sites/73/WatsonExplorer-DSX-p1-768x511.png)
---?image=https://source.unsplash.com/xekxE_VR0Ec/
## 2. Getting the data
+++
### Centadata Site
![centaline](Projects/BeginnerDataScience/pitch/2-centadata.png)
+++
### Centadata - centadataall
![centadata](Projects/BeginnerDataScience/pitch/2-centadataall.png)
+++
### Centaline Site
![Centaline Site](Projects/BeginnerDataScience/pitch/2-centadata-site.png)
+++
### Datasette
![datasette](Projects/BeginnerDataScience/pitch/2-datasette.png)
+++
### Raw Data
![rawdata](Projects/BeginnerDataScience/pitch/2-rawdata.png)

---?image=https://source.unsplash.com/FumjLlfuvhg/
## 3. Exploratory Data Analysis
+++
### Data Summary
![data summary](Projects/BeginnerDataScience/pitch/3-data-summary.png)
+++
### Price Per Sqft Dist
![price dist](Projects/BeginnerDataScience/pitch/3-area-dist.png)
+++
### Area by region
![region size](Projects/BeginnerDataScience/pitch/3-area.png)
+++
### Price by region
![region price](Projects/BeginnerDataScience/pitch/3-price-per-sqf.png)
+++
### Price vs Size
![price vs size](Projects/BeginnerDataScience/pitch/3-price-size.png)
+++
### Top 10 in 2018
![top 10](Projects/BeginnerDataScience/pitch/3-top10-2018.png)
---?image=https://source.unsplash.com/npxXWgQ33ZQ/
## 4. Data Wrangling
+++?image=https://source.unsplash.com/npxXWgQ33ZQ/
### Data Preparation & Feature Engineering
@ul
* one-hot encoding the region
* convert price to price per SqFt
* categorize flat types
@ulend
+++?image=https://source.unsplash.com/npxXWgQ33ZQ/
### Applying some Domain Knowledge
@ul
* Small-Medium vs Large Flats: 1076 SqFt
* Using the CCI to 'normalize' prices
@ulend
---?image=https://source.unsplash.com/KkYWWpurqbE/
## @color[white](5. Training the Model)
+++
### Target Dist
![target dist](Projects/BeginnerDataScience/pitch/5-targetdist.png)
+++
### Model Comparison
![model compare](Projects/BeginnerDataScience/pitch/5-model-compare.png)
+++
### Predict vs Actual
![predict vs actual](Projects/BeginnerDataScience/pitch/5-predict-actual.png)
+++
### Feature Importance
![feature importance](Projects/BeginnerDataScience/pitch/5-feature-importance.png)

---?image=https://source.unsplash.com/sD_o5hGKBeE/
## 6. Evaluate
+++?image=https://source.unsplash.com/sD_o5hGKBeE/
### @color[grey](Performance Metrics)
+++?image=https://source.unsplash.com/sD_o5hGKBeE/
### @color[grey](Hyperparameters Tuning)
+++
### Under the hood
![single full decision tree in forest](Projects/BeginnerDataScience/pitch/6-small_tree.png)

---?image=https://source.unsplash.com/_sCyfy3rppM/
## 7. Deploy & Perform
+++?code=Projects/BeginnerDataScience/predict_hk_prop.py&lang=python&title=The Deployed Model Code
+++?image=https://source.unsplash.com/_sCyfy3rppM/
### @color[grey](The baseline)
* Baseline predict = historical average
* Baseline errors = historical average error
+++?image=https://source.unsplash.com/_sCyfy3rppM/
### @color[grey](Conclusion)

---?image=https://source.unsplash.com/ckxoFlEtlUc/
## 8. Further Questions to Answer
+++?image=https://source.unsplash.com/ckxoFlEtlUc/
### To be continued...
@ul
* model for large flats
* model for dettached, bespoke, luxury homes
* model for rent???
* expanding the data set in time to improve the model?
@ulend
+++?image=https://source.unsplash.com/ckxoFlEtlUc/
### and more!
@ul
* analyze time series to identify trends in neigborhood
  * Classification problem?
* combine with other data size:
  * Population
  * Crime Rate
  * Starbucks Store Locations
@ulend
