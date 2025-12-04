import streamlit as st
import pandas as pd

def render_income_classification_dialog():
    """Render the Income Type Classification project dialog content"""
    
    st.header("📊 Dataset")
    st.write("""
    The data was fetched from World Bank by using APIs. It includes economy indices such as GDP or GNI, 
    year of record, colony, and excludes name of country. The time range is from 2012 to 2022. There are 
    4 income types: high, higher middle, lower middle, and low.
    """)
    st.markdown("[📁 Link to dataset](https://drive.google.com/file/d/11xWZgK4ZhLko7d0fUDc82FHW3i1m1yBu/view?usp=sharing)")

    st.header("🧹 Cleaning and Preprocessing")
    st.write("""
    As the data was fetched through APIs, it have already been cleaned. On the other hand, I applied 
    Ordinal Encoding for categorical features, and standardize for numerical features.
    """)

    st.header("🤖 Models and Evaluation")
    st.write("""
    There were two models that were trained: KNN and Random Forest. The data was splitted into train 
    set and test set with ratio is 4:1
    """)

    # Create results table
    results_data = {
        'Model': ['KNN', 'Random Forest'],
        'Test Accuracy': [0.05, 0.00],
        'Train Accuracy': [0.63, 0.98]
    }
    df = pd.DataFrame(results_data)

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )

    st.write("""
    As the table shows, models cannot predict well. The accuracy of KNN is 0.05, and Random Forest is 0. 
    The reason may be the data is not enough, or it needs more powerful models.
    """)

    st.header("🚀 Future Work")
    st.write("""
    For future work, I will try to apply more models such as SVM, Logistic Regression, or Neural Network 
    to see if the accuracy can be improved. Also, the data will be collected for diversity.
    """)
    
    if st.button("Close", key="close_income"):
        st.session_state.show_income_class = False
        st.rerun()
