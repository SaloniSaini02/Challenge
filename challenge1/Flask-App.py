#import packages 
from flask import Flask
from flask import *
import pandas as pd

# Create Flask App
app = Flask(__name__)

# Create url routes
@app.route("/Titanic")
def function1():
    """ Method reads the titanic dataset to a dataframe.The first half is stored in the first output(csv) file. The columns in the second half are reversed and stored in the second output file.
    
    Returns: 
    
    Template to be displayed in user's browser. 
    
    
    """
    titanic_df = pd.read_csv('train.csv')
    first_df = titanic_df.iloc[:445,:]
    # Reverse the second half of the dataset
    second_df = titanic_df.iloc[445:,::-1]
    # Store the data in two files
    first_df.to_csv('titanic_output1.csv')
    second_df.to_csv('titanic_output2.csv')
    return render_template('view.html',tables=[first_df.head(15).to_html(classes='normal'), second_df.head(15).to_html(classes='reversed')],
    titles = ['na', 'Output1', 'Output2'])
    
@app.route("/API/<string:apikey>")
def function2(apikey):
    """ Method reads in data using an API call. The dataframe is stored in an excel file as output.
    
    Parameters:
    
    arg1(int): Takes the api key as an argument.
    
    Returns:
    
    Template to be displayed in user's browser. 
    
    
    """
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey='+apikey+'&datatype=csv'
    time_series_df = pd.read_csv(url)
    time_series_df.head()
    time_series_df.to_excel("output.xlsx")
    return render_template('view2.html',tables=[time_series_df.head(15).to_html(classes='time_series')],
    titles = ['na', 'Time_Series'])
    
if __name__ == "__main__":
    app.run(debug=True)
