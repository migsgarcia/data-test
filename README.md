# Technical Test for Data Engineering Position

As a member of our data Engineering team, your work will focus on delivering long-lived data assets. This assessment is your opportunity to showcase your knowledge of good software and data engineering practices. Please develop your solution as if you were working on a production codebase.

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
- Develop functionality that enables a user/ downstream application to:
    - Calculate the total order amount for each customer.
    - Calculate the average order amount per city.
    - Identify the city with the highest average order amount.
    - Find the customers with the n-th highest total order amount within a given date range.
    - Raise a warning when a change in the week-on-week total order amount changes by more than 50% for any city.
