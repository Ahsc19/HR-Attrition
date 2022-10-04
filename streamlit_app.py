import streamlit as st
import streamlit.components.v1 as components
import pydeck as pdk

import numpy as np
import pandas as pd 
import math
import altair as alt



@st.experimental_singleton
def setup():
  st.set_page_config(page_title='Streamlit - Dashboard 🤯',
                    page_icon="🚀",
                    layout='wide')

