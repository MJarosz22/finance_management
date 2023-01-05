# Personal Finances
This project is designed to help manage and track personal finances by taking in financial data from various sources and inserting it into a Google Sheets document.

### Prerequisites
In order to run this project, you will need to have the following libraries installed:

* requests
* csv
* gspread
* time

You will also need to have set up the Google Sheets API and have the necessary authentication credentials in order to access the Google Sheets document.

### Running the script
To run the script, first set the MONTH variable to the desired month. Make sure that the .csv files (mbankFile and abnFile) are in the correct location. Then, simply run the script using Python:

python main.py
The script will process the .csv files, convert any non-EUR currencies to EUR, categorize the transactions, and insert them into the specified Google Sheets document.

### Built With
* requests - Used to make HTTP requests to the currency conversion API
* csv - Used to read and parse the .csv files
* gspread - Used to access and update the Google Sheets document
* time - Used to introduce a delay between inserting rows into the Google Sheets document
### Author
Marcin Jarosz - Initial work

Project inspired by YouTube video made by Internet Made Coder
