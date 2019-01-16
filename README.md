# Capstone Project: Site Specific Restaurant Recommender System

## Edith Iyer-Hernandez

# Problem Statement


A question that I tend to get asked a lot takes on the form "I've got X plans with Y person(or people) they want to go out to eat in Z neighborhood, do you have any recommendations?". I think I get asked this is because I love to eat, I worked in the hospitality industry for a long time and my husband builds and runs awesome restaurant bars for a living. The plans can vary from a simple happy hour to a multi course dinner and person can vary from family member to a rarely seen friend from high school to a professional acquaintance to a first date. The neighborhood tends to be somewhere I've maybe been to once. And I do not take very good notes. I always want to be able to provide insight because I want everyone to have the best eating and/or drinking experience possible. However, when it comes down to it, my brain is too full of other things these days to actually remember that spot in Jackson Heights with the best Vietnamese food I went with my father-in-law's friends four years ago. What I do remember is a cozy place in Bushwick with friendly staff, no-frills yet creative dishes and a volcano bowl cocktail.

__[The Infatuation](https://www.theinfatuation.com)__ is a restaurant review website that I personally love. I find their reviews to be thoughtful, thorough and candid. I am slightly biased because one of the founders' favorite places was my husband's bar. They do a great job of reviewing diverse options and take into account the fact that different types of restaurants serve different purposes. However, reading multiple reviews is time consuming. Sometimes I just want to be told where to go.

My capstone project will be the creation of a recommender system based on the ratings, cost and natural language processing of the reviews. My aim is to create a web app in which you can enter a restaurant that you like and 5 similar restaurants will be recommended to you with neighborhood, stars and possibly some key words that can help you make your decision. If possible I will exclude brunch options because I vehemently hate brunch (why would you leave your house to pay $20 for eggs and Andre mimosas?). Ideally, I want to harness the power of NLP to capture the essence of a restaurant and recommend other places with similar essences, whether that be the diviest of dives with an uneven pool table or a magnificent dinner that is actually worth the $1000 you might have spent at Persei.

# Data Collection

Webscraping of the Infatuation website:
1. Build a function that finds the slugs of ~900 restaurants from New York City.
2. Build a function that scrapes each review for each website.

# Natural Language processing

One of the challenges here is navigating similies and metaphors that are inevitably present in good restaurant reviews.

# Model Building

This will range from a logistic regression to something much more complex like the word2vec neural network.
