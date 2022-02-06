# Bank-Marketing-Prediction

## Context:

##### Bank Marketing
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed.



## Content: 


### Bank Client Data:

1 - age (numeric)

2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur", "student","blue-collar","self-employed","retired","technician","services")

3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)

4 - education (categorical: "unknown","secondary","primary","tertiary")

5 - default: has credit in default? (binary: "yes","no")

6 - balance: average yearly balance, in euros (numeric)

7 - housing: has housing loan? (binary: "yes","no")

8 - loan: has personal loan? (binary: "yes","no")

related with the last contact of the current campaign:

9 - contact: contact communication type (categorical: "unknown","telephone","cellular")

10 - day: last contact day of the month (numeric)

11 - month: last contact month of year (categorical: "jan", "feb", "mar", …, "nov", "dec")

12 - duration: last contact duration, in seconds (numeric)

other attributes:

13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)

15 - previous: number of contacts performed before this campaign and for this client (numeric)

16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

output variable (desired target):

17 - y - has the client subscribed a term deposit? (binary: "yes","no")


## Aim: 

This Dataset is contains of information about the customers whom having account in a client's bank. For Targetting a new product we segregate our customers based on their current subscription. 

From the Information about the Current Subscription who are all the target customer to reach, by the correct approach the client can earn better profit by selling the new upcoming product.



## Solution: 

To Solve this Problem I'll use a colaborative apporach of Classification.

Here I thought of Using Clustering Based Classification, whereas Clustering is an Unsupervised Learning (i.e.,) it won't have target variable, but in this dataset I have a Target variable called 'Subscription'. If I do Clustering, it probably may ended up into two classes of 0 or 1 (i.e.,) Either the Final customer is Subscribed or Not Subscribed.



## Working Procedure:

* Classifiying Data, Once I get accurate Classification of Data.



