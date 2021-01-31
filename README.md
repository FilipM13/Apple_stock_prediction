# STOCK PRICE PREDICTION  

## ABSTRACT
After dogecoin exploded I thought that stock price prediction can be fun project.  
Crypto currency is very unpredictable so I decided to use regular stock data.  
Apple was random choice.

## AIM
In this project I focused on few goals:  
- using machine learning  
- comparing many ML models with accuracy score  
- creating dependent variable based on independent variables  
- visualisation of data

## APPROACH
#### I divided project into separate steps:  
#### 1. Downloading data and preprocessing it:  
- Table had to be reversed to work properly.  
- Based on opening price I created dependent variable (direction).  
If next opening price is higher than current one, direction is 1.  
If next opening price is lower than current one, direction is -1.  
If next opening price is equal to current one, direction is 0.  
Example:
```  
open_price = [0,1,2,3,4,4,4,5,4,3,2,1]
open_price_direction = [1,1,1,1,0,0,1,-1,-1,-1,-1]
```

#### 2. Data analysis and prediction:  
- Splitting data into train and test sets (80% : 20%).  
- Creating ML classification model.  
- Training model.  
- Prediction based on test set.  

#### 3. Evaluation:  
- Creating confusion matrix from prediction and test set.  
- Getting accuracy score of model.  

#### 4. Visualisation:  
- Creating plot of downloaded data.  
- Adding dependent variable (red, green and blue areas on graph):  
 - red - indicates where price is going down  
 - blue - indicates where price does not change  
 - green - indicates where price is going up

## EVALUATION
| Model Name             |   Best Accuracy   |
|------------------------|:-----------------:|
| RandomForestClassifier |        66%        |
| DecisionTree           |        62%        |
| KNeighbors             |        60%        |
| LogisticRegression     |        57%        |
| GaussianNB             |        55%        |
| SVC(rbf)               |        55%        |
| SVC(linear)            | too long run time |

## CONCLUSIONS
Stocks are very unpredictable. It's difficult to make good predictions without knowledge of market.  
Global events have great impact on stock behaviours.  
In case of Apple such event may be new product release, PR actions, random scandal.  
Model accuracy may be improved by encoding date into independent variables.  
Perhaps season of the year has influence on stock price  
(ex. rising more dynamically in the end of the year).  
Maybe using other stocks' data will improve Apple stock prediction.  
There might be correlation between stock behaviour of number of companies.  

## CREATED GRAPH 
### FULL VIEW  
![entire data presentation](https://raw.githubusercontent.com/FilipM13/Apple_stock_prediction/main/Plot.png "Full graph")
### DETAIL CLOSEUP 1
![detailed closeup](https://raw.githubusercontent.com/FilipM13/Apple_stock_prediction/main/Closeup1.png "Closeup 1")  
### DETAIL CLOSEUP 2
![detailed closeup with blue area](https://raw.githubusercontent.com/FilipM13/Apple_stock_prediction/main/Closeup2.png "Closeup 2")  

## SOURCES  
- Apple stock price: https://www.nasdaq.com/market-activity/stocks/aapl/historical  
