# Football Data API Test Framework#

## Overview

This project is a football data APA Test framework written in Python showing how to get information from a secured web server using an API key. 

Every part of this project is a sample code that gets information about matches, teams, players, and competitions. It utilizes the [Football API](https://example.com/football-api) to fetch and display data related to football events.

## Features

- Retrieve match data for all or specific competitions
- Retrieve match data for all or specific area(s)
- View information about persons (Players)
- View details of ongoing and upcoming matches


## Installation

1. Clone the repository:

   ```bash
   git clone:  https:https://github.com/guruasap/FootballDataAPI.git
   Install dependencies:
   cd FootballDataApi 
   pip install -r requirements.txt
   

## Usage
1. Obtain API key:
To use the Football API, you need to obtain an API key from [Football Data Org](https://www.football-data.org) and update the config.py file with your key.

2. Run the application:

## Configuration
Update the config.py file with your API key and other configuration settings.

### config.py

BASE_URL = "https://www.football-data.org"
HEADER = {'X-Auth-Token': 'your-api-key'}

## Contributing or Found a bug?

if you found an issue or would like to submit an improvement  please submit an issue using the issues tab above. If you would like to submit a PR with a fix, making reference to teh issue you created.
