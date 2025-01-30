#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:08:20 2025

@author: ndumiso
"""

import streamlit as st
import pandas as pd

st.title("Valentines is coming where is your boyfriend?")
st.write("A perfect love story")

st.image("5d46c3fb-8bb0-4058-bd63-f554ec5e6950.JPG")

st.write("Roses are red violets are blue, life is sweet when you're around,  you're my wifey and I'm your hubby, will you be my sweet valentine?")

st.subheader("A testiment of my love")
st.write("My love for you, my darling, is a river that never runs dry, flowing endlessly through the valleys of time. You are the moon that pulls my tides, the sun that warms my soul, the whispered breeze that stirs my heart. In your laughter, I find my melody; in your embrace, my home. Every heartbeat echoes your name, every breath is a vow renewed. If love were a language, my every word would be a verse written for you. With you, forever is not long enough, for even eternity could never hold the depth of what I feel.")


choice = st.selectbox(
    "Will you be my Valentine?", 
    ["No", "Yes"]
    )

if choice == "Yes":
    st.write("Its a Date! Friday the 14th, 7pm")
else:
    st.write("I guess i have to try again next year :(")
    
    