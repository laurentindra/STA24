import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data
scores = [1, 2, 3, 4, 5]
frequencies = [24, 33, 42, 30, 21]

# Calculate probabilities
total = sum(frequencies)
probabilities = [f / total for f in frequencies]

# Create a DataFrame
data = pd.DataFrame({'Score (x)': scores, 'Frequency (f)': frequencies, 'Probability P(x)': probabilities})

# Streamlit App
st.title('Probability Distribution of Sentiment Scores')

# Show the table
st.write("### Probability Distribution Table")
st.dataframe(data)

# Plotting the histogram
fig, ax = plt.subplots()
ax.bar(scores, probabilities, color='skyblue')
ax.set_xlabel('Score (x)')
ax.set_ylabel('Probability P(x)')
ax.set_title('Probability Distribution of Sentiment Scores')
ax.grid(True)

# Show the plot in Streamlit
st.pyplot(fig)
