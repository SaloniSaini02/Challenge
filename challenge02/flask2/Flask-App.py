
# coding: utf-8

# In[ ]:


from flask import Flask
from flask import *
import pandas as pd
import subprocess
#import Script1
app = Flask(__name__)


@app.route("/Titanic")
def function1():
    titanic_df = pd.read_csv('train.csv')
    first_df = titanic_df.iloc[:445,:]
    second_df = titanic_df.iloc[445:,::-1]
    first_df.to_csv('titanic_output1.csv')
    second_df.to_csv('titanic_output2.csv')
    subprocess.call(["ls", "-l", "./"])
    return render_template('view.html',tables=[first_df.head(15).to_html(classes='normal'), second_df.head(15).to_html(classes='reversed')],
    titles = ['na', 'Output1', 'Output2'])
    
@app.route("/API/<string:apikey>")
def function2(apikey):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey='+apikey+'&datatype=csv'
    time_series_df = pd.read_csv(url)
    time_series_df.head()
    time_series_df.to_excel("output.xlsx")
    subprocess.call(["ls", "-l", "./"])
    return render_template('view2.html',tables=[time_series_df.head(15).to_html(classes='time_series')],
    titles = ['na', 'Time_Series'])
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')