# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Data
@st.cache_resource
def load_data():
    data = pd.read_csv("../dataset/hour.csv")
    return data

data = load_data()


# Set page title
st.title("Bike Share Dashboard")

# SIDEBAR
st.sidebar.title("Information:")
st.sidebar.markdown("**• Name: Alifya Zhafira Ananda**")
st.sidebar.markdown(
    "**• Email: [alifya.zhafira29@gmail.com](alifya.zhafira29@gmail.com)**")
st.sidebar.markdown(
    "**• LinkedIn: [Alifya Zhafira Ananda](https://www.linkedin.com/in/alifya-zhafira-ananda/)**")
st.sidebar.markdown(
    "**• Github: [alifyaza](https://github.com/alifyaza)**")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/code)")

# VISUALIZATION
# create a layout with two columns
col1, col2 = st.columns((7,3))

# Pie chart: Distribution of seasons
with col1:
    #st.markdown("### Distribution of Seasons (Pie Chart)")
    season_counts = data['season'].value_counts()
    fig_pie = px.pie(season_counts, values=season_counts.values, names=season_counts.index, title='Distribution of Seasons')
    st.plotly_chart(fig_pie)

# Heatmap: Correlation matrix
with col2:
    #st.markdown("### Correlation Heatmap")
    numerical_columns = data.select_dtypes(include=['number']).columns
    corr = data[numerical_columns].corr()
    fig_heatmap = px.imshow(corr, color_continuous_scale='RdBu', title='Correlation Heatmap')
    fig_heatmap.update_layout(width=600, height=400)
    st.plotly_chart(fig_heatmap)

# Bar chart: Distribution of bike rentals on weekdays vs holidays
#st.subheader("Bike Rentals Distribution on Weekdays vs Holidays")
rentals_by_day = data.groupby(['weekday', 'holiday'])['count'].sum().reset_index()
fig_bar = px.bar(rentals_by_day, x='weekday', y='count', color='holiday', title='Bike Rentals Distribution on Weekdays vs Holidays',
                 labels={'count': 'Total Bike Rentals', 'weekday': 'Weekday', 'holiday': 'Holiday'})
fig_bar.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']})
col1.plotly_chart(fig_bar, use_container_width=True)

# Humidity vs Bike Share Count
#st.subheader("Humidity vs Bike Share Count")
fig_humidity_chart = px.scatter(
    data, x="hum", y="count", title="Humidity vs Bike Share Count")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs Bike Share Count
#st.subheader("Wind Speed vs Bike Share Count")
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="count", title="Wind Speed vs Bike Share Count")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs Bike Share Count
#st.subheader("Temperature vs Bike Share Count")
fig_temp_chart = px.scatter(data, x="temp", y="count",
                            title="Temperature vs Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)
