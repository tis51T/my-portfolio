import streamlit as st
import os

def render_house_price_dialog():
    """Render the House Price Prediction project dialog content"""

    # Use primary color from the app theme if available
    primary = st.session_state.get('primary', '#FFCC66')

    st.markdown(f"<h2 style='color: {primary};'>📊 Dataset</h2>", unsafe_allow_html=True)
    st.write("""
    The data was crawled from [batdongsan.com.vn](https://batdongsan.com.vn/ban-nha/) website. 
    The dataset includes more than 10,000 samples that are only about houses in Ho Chi Minh city.
    """)

    st.markdown(f"<h2 style='color: {primary};'>🧹 Cleaning and Preprocessing</h2>", unsafe_allow_html=True)
    st.write("""
    In this project, the cleaning phase is the hardest part to me as the price of house is wrong due 
    to typo error, for example the true price is 3.9 billions VND but the post shows 3,900,000 billions VND. 
    To cope with this problem, I decided to divide the price by 10 or 100 or 1000 to get to true price. 
    Some other features like number of bedrooms, bathrooms, squares, etc. also have this problem. I have 
    to extract the price from the content and title (the structure of a post include: given information, 
    title, content) and then vote the final information.
    """)

    st.write("""
    With Preprocessing phase, I applied imputing NaN data using KNN, target encoding, and normalization.
    """)

    st.markdown(f"<h2 style='color: {primary};'>🤖 Models and Evaluation</h2>", unsafe_allow_html=True)
    st.write("""
    I totally used 5 models: Dummy Regression (for baseline model), Polynomial Linear Regression, 
    Random Forest, Support Vector Machine, and Decision Tree. Moreover, to find out which model is 
    the best, I also used GridSearchCV to tune hyperparameters. The evaluation metrics are RMSE, MSE, 
    MAE, run time, memory usage, and CPU usage.
    """)

    # Display metrics images
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("images/house_price_prediction/metric1.png"):
            st.image("images/house_price_prediction/metric1.png", caption="Model Metrics 1")
    with col2:
        if os.path.exists("images/house_price_prediction/metric2.png"):
            st.image("images/house_price_prediction/metric2.png", caption="Model Metrics 2")

    st.markdown(f"<h2 style='color: {primary};'>⚠️ Challenges</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: {primary};'>1. Data Accuracy</h3>", unsafe_allow_html=True)
    st.markdown("""
    - The data from the website is full of noise as some posts sell furniture, buildings, electronic 
      items, etc., instead of selling houses. I tried to filter by length of content and title of the 
      post, but there still have outliers.
    - As I mentioned before, information in the post is not consistent.
    """)

    st.markdown(f"<h3 style='color: {primary};'>2. Data Completeness</h3>", unsafe_allow_html=True)
    st.write("""
    In this dataset, "Cần Giờ" District is not included, so I decided to encode it as 0. This is risky 
    as the absence doesn't mean it is absolutely zero.
    """)
    
    if st.button("Close", key="close_house"):
        st.session_state.open_dialog = None
        st.rerun()
