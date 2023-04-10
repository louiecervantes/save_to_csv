#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import numpy as np
import pandas as pd


# Define the Streamlit app
def app():
    
    # Create a sample dataframe
    data = {
        'Name': ['John', 'Mary', 'Mike', 'Linda'],
        'Age': [30, 25, 40, 35],
        'City': ['New York', 'London', 'Paris', 'Tokyo']
    }
    df = pd.DataFrame(data)

    # Create a button to save data to CSV file
    if st.button('Save data to CSV file'):
        # Prompt the user to enter a filename
        filename = st.text_input('Enter a filename:', 'data.csv')
        # Save the dataframe to a CSV file
        df.to_csv(filename, index=False)
        st.success(f'Data saved to {filename}!')         
             
# run the app
if __name__ == "__main__":
    app()
