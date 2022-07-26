# Yuview

## Getting Started

### Main Tech

npm: 8.6.0

Python: 3.9.12

spaCy: 3.3.0

Scrapy: 2.6.1

FastAPI: 0.78.0

React: 18.1.0

PostgreSQL: 13.2

SQLAlchemy: 1.4

### Dependencies

For client-side, run `npm install` or `yarn install`.
For server-side, run `pip install -r requirements.txt` in the /server directory.

## Web App

Open [https://yuview.vercel.app/](https://yuview.vercel.app/) to view it in your browser.

## Public API

Starts the server at root url [https://yuview-production.up.railway.app/](https://yuview-production.up.railway.app/).
Go to the interactive API documentation at [https://yuview-production.up.railway.app/docs](https://yuview-production.up.railway.app/docs).

## Project Motivation

In modern society, it is common for people to make use of online shopping to purchase their products due to its convenience and affordability. However, one thing we realised was that despite the large number of reviews on a product, nobody will actually spend time reading through every single review as it can be very tedious and tiring. Furthermore, although a star rating is displayed to reflect the general satisfaction level of consumers, what buyers are looking for are mostly the adjectives or descriptions given by the reviews, hence the star rating is not as important as the written reviews.

## Aim

We aim to create a web extension that takes in all the reviews for a product and summarises them based on most frequently used phrases or words, thus making reviews easier and more efficient for buyers to digest.
A Google Chrome browser extension that identifies the product a user is interested in from the webpage and retrieves data from various e-commerce sites, collating information such as user ratings, reviews and prices.

## User Stories

- As a buyer who wants to make a choice between multiple products, I want to be able to read reviews more efficiently and get a consensus of others’ opinions.
- As a seller, I want buyers to be more convinced on the products I am selling before they decide on whether they purchase them or not.
- As a user of online shopping websites, I do not want to spend too much time scrolling through each review.

## Core Features
The server employs natural language processing (NLP) techniques to deliver a concise summary of all user reviews and provides an aggregate “value” rating.

The user now has a comparison with different purchase options and is able to access links which redirect them to these sites or bookmark the query.

Fig 1. Home page
![Screenshot 2022-07-25 010741](https://user-images.githubusercontent.com/105497963/180813066-7bf4e4bd-74b4-4c91-9477-89ff58b4bd0a.png)


Fig 2. Top bar, which consists of a search tool as well as a drop down tool
![Screenshot 2022-07-25 011101](https://user-images.githubusercontent.com/105497963/180812897-ac38423c-5dd2-4911-a7f3-383ad74275fe.png)


## Testing
### Regression testing 
Performed upon implementing of each feature to detect errors that could hinder future feature implementations

### User testing
Arranged for friends from outside our project to help to test out our application





## Tech Stack
### spaCy
We used spaCy as our main natural language processing tool in order to process the data that we scraped and then use it to create our reviews
### FastAPI

### Scrapy
We used Scrapy to scrape data of the shopping website
### NodeJS
NodeJS was used for the installation of packages
### Github
Our project is uploaded onto github and any changes are reflected within the repository. It is also used for us to push/pull new content that we are working on.

## Challenges faced
Initially, we intended to work on the data extraction and API first, starting off with Shopee as our first target site. However, we hit a roadblock and realised that Shopee Open API was restricted to sellers and third-party businesses. After trying to find a workaround, we fell back to the less ideal solution of web scraping.

Our approach of directly scraping the HTML DOM using the Scrapy framework was unsuccessful due to the dynamic loading of JS scripts. We then attempted using Selenium + BeautifulSoup to interact with the browser directly. Even though the second approach worked, it was too inefficient due to the time delays required for automated browser input like scrolling and clicking. Eventually, we arrived at the solution of making HTTP requests directly to the Shopee internal API by searching through network data for the link templates.

Originally, we were planning to have our code perform the filtering for multiple product listings at one go, but the code was taking too long to run, hence we decided to adjust the code such that it runs for a single product listing based on the page that the user is on.

## Software engineering practices
Weekly code review: Since our responsibilities were mainly separated into different parts of the code, we decided to review each other’s codes regularly to ensure that our code was working towards our goals and functioning.

Version control using Git/GitHub: We used Github as our main codebase to control versions of our work, allowing us to work on different tasks separately on different branches. This way, we were able to merge our work together with very few clashes. It also made it easier to review each other’s work.

## Architecture

![Relational Diagram](./Architecture.drawio.svg)

## Development Plan

![Screenshot 2022-07-25 233801](https://user-images.githubusercontent.com/105497963/180818474-dc010646-a001-4fc1-909d-3553a082f524.png)



