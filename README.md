# UPC Datathon 2023
# Fashion Compatibility Challenge <img src="resources/icon.png" align="right" height=100/>

## Overview

<img src="resources/outfit.png">

This challenge aims to create a model capable of generating outfit recommendations based on a given initial product. Fashion matching is complex due to the nuanced patterns and visual details that dictate whether products pair well together, often going beyond mere product metadata. For instance, it's not straightforward to determine if a violet satin dress, white sandals, and a silver chic bag make a good outfit without seeing the items.
 
The essence of a good outfit often lies in the complementary nature of different products rather than their similarity. The task here is to extract and model these visual features to predict matching products effectively. One approach to address this is the "Fill in the Blank" task, where the goal is to predict a missing item in a given outfit from a list of candidate products. This task serves as a stepping stone towards generating complete outfits from a single product. However, participants are encouraged to explore other innovative solutions to this challenge as well.
 
Participants will have the opportunity to work with real outfits curated by stylists and fashion experts at MANGO and exhibit their proficiency in navigating a software development environment while adhering to strict deadlines and maintaining performance under a high-pressure scenario.


## Project
The Outfit Recommendation App is designed to help users discover new outfit combinations based on Mango's curated collection of stylish outfits. When a user selects a clothing item, the app generates and displays suitable outfits that complement the chosen piece, making it easier to put together fashionable looks.

## Code Structure
### /dataset
This directory contains the essential dataset required to run the code. To complete the setup, you need to add the images, which are available in a separate zip file.

### /src
Data_generator.ipynb: This Jupyter Notebook contains the code responsible for preprocessing the dataset. It prepares the data for subsequent steps in the project.

Main.ipynb: In this Jupyter Notebook, you'll find the code responsible for loading the processed data from pickles and generating outfit recommendations based on it.

generate_outfits.py: This script houses the functions responsible for creating new outfits and finding recommendations based on the outfit graph.

my_graph.pickle: This pickle file contains the serialized outfit graph, which is a crucial component for generating recommendations.

outfit_cleaning.py: This script includes preprocessing functions used to clean and format the outfit data.

show_images.py: Here, you'll find functions related to displaying individual clothing items or complete outfits.

outfit.csv: This CSV file contains the final outfit recommendations that have been created through the project's processes.

## Usage
Ensure you have the necessary dataset files and images in the /dataset directory.

Use Data_generator.ipynb to preprocess the dataset.

Run Main.ipynb to load the processed data and start generating outfit recommendations.

Explore the app by selecting clothing items, and the app will display matching outfit suggestions.

## App Demo
You can access the live demo of the Outfit Recommendation App here (https://mangodatathon2023.streamlit.app/).


