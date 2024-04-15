# Technical Test for Data Engineering Position

This test is designed for candidates to demonstrate their knowledge of good software and data engineering practices.

As part of solving this, we are looking to assess:
- Your problem-solving approach.
- Your ability to turn your solution into working code and choosing appropriate technology.
- How you structure and test your code and your ability to work with others.


Instructions:

- Use Python and Pandas to complete the tasks outlined below.
- Feel free to use any additional libraries if necessary.
- Please provide comments to explain your thought process and approach.
- Try to optimize your code for efficiency and readability.

Install and run pytest

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
pytest ./tests -v
```

________

**Customer Shopping Patterns**


> As a data analyst, I want to be able to analyze and gain insights from sales data that includes information about customer orders and customer demographics.


The task involves developing a data pipeline to complete the user story above using sample data sources that will be provided.


Dataset:
You will be working with two datasets:

`Orders.csv`
```
Contains information about orders including 
order_id, customer_id, order_date, and order_amount.
```
`Customers.csv`

```
Contains information about customers including 
customer_id, customer_name, and customer_city.
```


Tasks:
- Load the datasets into Pandas dataframes from sample data.
- Perform data cleaning if necessary (e.g., handling missing values).
- Merge the two datasets on the 'customer_id' column.
- Calculate the total order amount for each customer.
- Find the top 10 customers with the highest total order amount.
- Calculate the average order amount per city.
- Identify the city with the highest average order amount.