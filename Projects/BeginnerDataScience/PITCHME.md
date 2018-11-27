---?image=https://source.unsplash.com/c4XoMGxfsVU/
### Using Machine Learning to Predict Hong Kong Property Prices
+++
## 1. The question
* How much is where I am worth right now?  
* Is the price advertised on ad fair??
* If I want to live in [X] neigborhood with [Y] square-foot worth of space in a [Z]-year-old building. How much money do I need???
+++
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
---
## 2. Getting the data
+++
### Centaline Data
![centaline](pitch/2-centadata)
---
## 3. Exploratory Data Analysis
+++
### Findings
+++
### More Findings
---
## 4. Data Wrangling
+++
### Data Preparation & Feature Engineering
* one-hot encoding the region
+++
### Applying some Domain Knowledge
* Small-Medium vs Large Flats: 1076 SqFt
* Using the CCI to 'normalize' prices
---
## 5. Training the Model
---
## 6. Evaluate
+++
### Performance Metrics
+++
### Hyperparameters Tuning
+++
### Under the hood
![single full decision tree in forest](data/tree.png)
---
## 7. Deploy & Perform
+++
### The baseline
* Baseline predict = historical average
* Baseline errors = historical average error
+++
### Conclusion

---
## 8. Further Questions to Answer
