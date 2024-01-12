# Predicting-Delinquency-In-Utility-Bills-With-Residents-Of-City-Of-Stillwater

## COS: Project Report
### Introduction to Project/ Background Information 
Established in 1889, Stillwater, Oklahoma, the home of Oklahoma State University, has transformed itself from a small agricultural community to a micropolitan area with a market area of 85,000 people (about the seating capacity of the Los Angeles Memorial Coliseum) during the school year and approximately 46,000 permanent residents. A unique characteristic of Stillwater is that the main power driver for its economy is the campus. However, as the City of Stillwater continues to grow, the municipality building has noticed a growing problem of people defaulting on their utility bills, which poses a financial obligation to the taxpayers of the community. This concern of delinquent account is becoming increasingly significant as the community is responsible for the debt of their neighbors and business owners. 

To address this issue, a Business Analytics and Data Science year-long project has been initiated to assist the micropolitan area in predicting potential delinquent accounts, discovering risk factors in their temporary and permanent citizens, and allowing the City of Stillwater to intervene to help these individuals pay their utility bills on time. This project will provide valuable insights that can help the City intervene early on and take corrective action, reducing the burden on the taxpayers and improving the financial stability of the community. 

### Business Problem/ Questions 
The City of Stillwater is faced with a significant business problem related to delinquency issues in the local community regarding utility bill payments. As households or businesses default on their utility bills, the city incurs a financial burden that accumulates and results in substantial financial losses. The responsibility of collecting delinquent accounts falls on the city, which can be a laborious and costly process. If left unaddressed, these delinquencies can negatively impact the city’s credit ability to keep the costs out of the taxpayers' pockets.

Therefore, it is essential to develop a strategy to predict and prevent delinquencies in utility bills to reduce the burden on taxpayers and improve the financial stability of the community. By leveraging data science techniques and census data, the City of Stillwater can identify patterns and correlations between the demographics of households and the likelihood of delinquency. This analysis can be used to create a predictive model that identifies households that are at higher risk of becoming delinquent on their utility bills. 

Using this model, the city can intervene early and take corrective action to prevent delinquency and reduce the burden on taxpayers. Additionally, this strategy can help the city improve the quality of life in the community. By addressing this business problem proactively, the City of Stillwater can ensure the financial stability of the community and provide better services to its residents. 


### The questions we want to take on include: 

- **Understanding the data library** – This includes understanding all the variables form the various tables provided, understanding the format, metrics to quantify, and the relation of the variables to our broad question of the effects of those variables on delinquency. 

- **Observing clusters and trends followed by accounts** – This includes plotting graphs to observe or identify patterns to choose specific variables to further investigate their impact on delinquency. 
  - *How much revenue is lost due to delinquent utility bills, and what is the impact on the City’s budget? How does this affect the citizens of Stillwater?* 
 
- **Relating said patterns to delinquent accounts** – Understanding the impact of the variables on each other and checking for correlation among them. 
  - *Are there any external factors, such as economic conditions, that contribute to delinquency, and how can they be mitigated?*
 
- **Creating model to predict the credit offense amount for new and existing users** – To create different models on the variables selected and comparing their accuracies.
  - *How can the city measure the success of its strategy to prevent delinquency and what metrics should be used to track progress?* 

As we delved into the data and conducted our analysis, we aimed to answer several key questions to gain deeper insights into the delinquency issues related to utility bill payments in the City of Stillwater. 

Through our research, we hoped to gain a better understanding of the factors that contributed to delinquency risk and determined the most effective strategies to mitigate delinquency. 

Furthermore, we explored the demographics of households that were more likely to become delinquent on their utility bills and assessed how these factors could be leveraged to prevent delinquency. 

By answering these questions and gaining valuable insights into the data, we developed a comprehensive and data-driven approach to address the delinquency issues in the City of Stillwater.

### Data description and Data Collection:
The Data is provided in 4 different tables which contain various elements involving the customer details and their billing information. We have four tables containing about 61 variables, each of which gives us information about the location of the customer, their deposit details, or their bills. However, some of these tables and variables were null, and we are ignoring those variables for our analysis. 

PFB the data dictionary for the key tables which we are using in our analysis:

table 1

table 2

- **Primary Keys:**
  - *UTCSID and UTLCID are the primary keys which help to identify a unique customer.*

- **Data Facts:**
  - *After removing all the commercial customers from the dataset, we have the following data facts considered for our analysis and prediction model:*
    - *Total number of distinct residential UTCSID and UTLCID: 16,516*
    - *Distinct residential addresses where the City of Stillwater provides services: 6,918*

- **Scrapping Data:**
  - *As part of the secondary research, we were planning to add socioeconomic data to our existing company data set.*
  - *To get socioeconomic parameters, we are looking at census data. However, we have census data on an aggregate level of a tract rather than individual addresses.*
  - *To accommodate that, we have worked on finding the corresponding tract values for individual addresses.*
    - *We have found the website: [FFIEC GeoMap](https://geomap.ffiec.gov/ffiecgeomap/). This website outputs the tract for any address given as input.*
    - *Since we had over 4000+ individual rows, we decided on writing a scraping code instead of manually entering the addresses into the site.*

