# Startup database and Recommendation Engine --- Editing

Detailed documentation can be found in the [PDF report](https://github.com/K-AlfredIwasaki/job_hunting_made_easy/blob/master/startup_db_recommendation.pdf)

## Problem: Finding a startup that matches your interest is hard

## Project Overviews
![Alt text](https://github.com/K-AlfredIwasaki/job_hunting_made_easy/blob/master/images/04%20-%20Project%20Overview-1.png?raw=true "Title")


## Technologies
- Data Collection and Preprocessing  --- Selenium, BeautifulSoup, Python, Jupyter Notebook
- Data Exploration and Visualization --- R, ggplot, ggmap, dplyr, Rmarkdown
- Recommendation Enmgine             --- scikit-learn for feature scaling and ML algorithms

## Data Collection and Preprocessing

![Alt text](https://github.com/K-AlfredIwasaki/job_hunting_made_easy/blob/master/images/05%20-%20Data%20Collection%20and%20Preprocessing%20Scheme-1.png?raw=true "Title")

## Data Exploration and Visualization


## Recommendation Engine

#### How the recommendation engine should work:
Given user inputs such as industry, company size, and year founded, it provides a few companies that matches the inputs

#### Algorithm choice: K-nearest neighbors (KNN)
KNN works well for multi-class problems like this problem where we want to assign the user input to a label (company) as outputs out of all the different labels.  It also produces several neighbors which we can use as a secondary recommendations for the user.

#### How KNN works: 
A green dot as the user input and other dots are startups in the database. KNN calculates the distance between the green dot and other dots and come up with K dots that are closest to the green dot. The shorter the distance is is, the better matches between the input and the neighbors are. These neighbors become the recommendation.

![Alt text](https://github.com/K-AlfredIwasaki/job_hunting_made_easy/blob/master/images/22%20-%20Feature%20Transformation%20and%20Engineering-1.png?raw=true "Title")

![Alt text](https://github.com/K-AlfredIwasaki/job_hunting_made_easy/blob/master/images/23%20-%20Recommendation%20Output-1.png?raw=true "Title")

## Future Development 

##### Data collection
Incorporate more data sources such as Glassdoor. 
Create data pipeline that is based on once a day batch processing from multiple data sources.
Improve algorithms for various data extraction works by utilizing existing NLP packages.

##### Data storage
Store the data in database such as PostgreSQL for better data management and data retrieving capability.
Data preprocessing

#### Data preprocessing
Clean up codes and streamline the process.
Incorporate better handlings.

#### Recommendation Engine
Store companies also-viewed for each company profile at linked in Graph DB such as Neo4j and generate startup recommendations based on the DB.

#### Interface
Create a Web application using Flask and develop GUI to enable users to input their preferences and to view recommendation outputs.

