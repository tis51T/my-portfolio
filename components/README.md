# Portfolio Components Structure

This folder contains the modular dialog components for the portfolio app.

## Files:

- `__init__.py` - Package initialization and exports
- `house_price_prediction.py` - House Price Prediction dialog content
- `income_type_classification.py` - Income Type Classification dialog content

## How to Add New Project Dialogs:

1. Create a new file in this folder (e.g., `my_new_project.py`)
2. Define a render function:
```python
import streamlit as st

def render_my_new_project_dialog():
    """Render the My New Project dialog content"""
    st.header("📊 Project Title")
    st.write("Your content here...")
    
    # Add close button
    if st.button("Close", key="close_my_project"):
        st.session_state.show_my_project = False
        st.rerun()
```

3. Export it in `__init__.py`:
```python
from .my_new_project import render_my_new_project_dialog
```

4. Import and use it in `app.py`:
```python
from components import render_my_new_project_dialog

# Create dialog
@st.dialog("My New Project", width="large")
def show_my_project_dialog():
    render_my_new_project_dialog()
```

## Benefits:

✅ **Separation of concerns** - Dialog content is separate from main app logic  
✅ **Easy to maintain** - Each project has its own file  
✅ **Reusable** - Components can be imported anywhere  
✅ **Clean structure** - Main app.py stays concise  
