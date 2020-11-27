#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image


# In[ ]:


st.write("""
# Optimal Asset Allocation
@E E Ajaegbu -- 27th of November, 2020


Optimal asset allocation also known as Portfolio optimization or the modern portfolio theory, is the acts of creating/building a desired portfolio which maximizes the expected return for a given risk or minimizes the risk for a given level of return.
""")
st.subheader("Goal of this Research:")

st.write("""  
i) To determine the Risk associated with  Amazon, Facebook, Google and Microsoft stock. 
""")
st.write("""
ii)To create a portfolio that comprises of  Amazon,Facebook, Google and Microsoft 
""")
st.write("""
iii) To determine the weight that will minimizes the risk and maximizes the expected returns
""")

st.header("United State Stock Market in 2020")
st.write("Historical Data: 1st of  January, 2020 - 26th of  November, 2020")

RUA = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/RUA.jpg")
RUA_vol = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/RUA_vol.jpg")

st.image(RUA,caption="Daily Stock Price of Russell 300",use_column_width=True)
st.image(RUA_vol,caption="Volatility Clustering of the Daily Returns", use_column_width=True)

st.write(
"""
         Between mid-February and End of March 2020, the Crux of corona pandemic and period of news and rumors of the potential lockdown of cities and states in the United States, the US stock Market experienced sharp decline in value of stocks and extreme market Volatility, this is due to the facts that Investors were afraid because of uncertainty caused by the pandemic which led them to reduce their position or even sold their entire Position in share of stock in the Capital Market.
""")
st.write(
"""
From April, the volatility of US stock market have continue to reduce and is fairly stable for the past four month, and the Value of Stocks have also continue to rally upward.
""")

st.header("Volatility,Beta, and Value at Risk ")
## Volatility, Bets and VaR
Metric =pd.DataFrame({"Benchmark (Russell 3000)":[2.319396,1,7.371953],"Amazon":[2.515215,0.6559319,5.424391],\
                      "Facebook":[2.999992,0.9626674,7.779814],"Google":[2.518143,0.9266877,5.985034],\
                     "Microsoft":[2.888342,1.092308,6.970678]},index=["Volatility(%)","Beta","VaR (%)"])
st.dataframe(Metric)

st.subheader("Volatility")
st.write("""
Amazon, Facebook, Google and Microsoft are more volatile compared to the market benchmark index (Russel 3000). Facebook is the riskiest stock, it has the highest Volatility Value, Next is  Microsoft, then Google. Amazon is the least risky stock since it has the least volatility. The stocks considered in the portfolio are  high risk stock.
""")
st.subheader("Beta")
st.write("""
Microsoft has the Highest Beta with value of 1.092308. The stock of Microsoft moves in greater amount to the general direction of the stock markets, it is highly sensitive to the movement in the market as a whole, For instance, if he market increase by 10%, it is expected that the stock of amazon increase by 10.9%, 

The Amazon, Facebook and Google stocks are less sensitive to the movement in the market as a whole but it is positively correlated to the market. they have beta value ranging in between 0 and 1.
""")

AMZN_vol = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/AMZN_vol.jpg")
FB_vol = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/FB_vol.jpg")
GOOGL_vol = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/GOOGL_vol.jpg")
MSFT_vol = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/MSFT_vol.jpg")

ticker = st.selectbox('Select Ticker',['AMZN','FB','GOOGL','MSFT'])
if ticker == "AMZN":
    st.image(AMZN_vol,caption="Volatility Clustering of the Daily Returns of Amazon Stocks.",use_column_width=True)
elif ticker == "FB":
    st.image(FB_vol,caption="Volatility Clustering of the Daily Returns of Facebook Stocks.",use_column_width=True)
elif ticker =="GOOGL":
    st.image(GOOGL_vol,caption="Volatility Clustering of the Daily Returns of Google Stocks.",use_column_width=True)
else:
    st.image(MSFT_vol,caption="Volatility Clustering of the Daily Returns of Microsoft Stocks.",use_column_width=True)
    
st.subheader("Value at Risk, VaR")
st.write("""
The 99% VaR for Amazon is 5.424391, it implies that there is a 1% chance that the Amazon stock will lose 5.42% of it's value in a single day. The 99% VaR for Facebook is 7.779814,it implies that there is a 1% chance that the Facebook stock will lose 7.78% of it's value in a single.The 99% VaR for Google is 5.985034,it implies that there is a 1% chance that the Google stock will lose 5.99% of it's value in a single.The 99% VaR for Microsoft is 6.970678],it implies that there is a 1% chance that the Microsoft stock will lose 6.97% of it's value in a single.
""")

st.header("The Global Minimum Variance Portfolio")
st.write("The GVMP approach will be used in selecting the optimal weights for the four assets. MV portfolio is a non-constraint mean variance optimization strategy which is on the left most tip of the mean variance efficient frontier, the global minimum variance portfolio is the assets portfolio with lowest risk or variance on the minimum variance frontier.")

st.subheader("The Regression Approach")
reg = Image.open("C:/Users/hp/Desktop/Streamlit App Documentation/Portfolio Optimazation/reg.jpg")
st.image(reg,caption="Regression Summary",use_column_width=True)

st.write("""
a) The Global Mininum varaince portfolio Weight is the Coefficent of the Regression Model
""")
st.write("""
b) The Intercept is the Expected Return of the Portfolio
""")
st.write("""
c) The standard deviation of the Error Term is the Volatility of the Portfolio
""")

st.subheader("Portfolio Weight")
gmvp = pd.DataFrame({"Amazon": 0.5962531,"Facebook":-0.006531495,"Google":0.7441513,"Microsoft":-0.2750895},index=["Weight"])
st.dataframe(gmvp)
st.write("""
A negative portfolio weight indicate you should short sell. Short selling implies to borrow the stock now and Sell it later. You must then purchase the stock at a later date to repay the borrowed stock.
         """)

st.write("The expected Return of Portfolio is 0.002094")
st.write("Volatility of the Portfolio is 2.27% ")
st.write("""


""")
st.subheader("Thank You")