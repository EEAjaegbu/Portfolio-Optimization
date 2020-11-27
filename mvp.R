
### Global Minimum variance portfolio for four Techn Stock.
# 25/11/2020
# Ajaegbu Ebuka Emmanuel

library(quantmod)
library(TTR)
library(PerformanceAnalytics)
library(tseries)
library(corrplot)
library(ggplot2)


# Period Covered
startdate="2020-01-01"
enddate="2020-11-26"


### BETA, VOLATILITY AND VALUE AT RISK OF THE FOUR STOCK AND THE BENCHMARK

## BENCHMARK STOCK- Rusell 3000
getSymbols("^RUA",from=startdate ,to=enddate, src="yahoo")
chartSeries(RUA)

# Get daily return 
russell3000Returns<- dailyReturn(RUA)
russell3000Returns

# Volatility and Volatility Clustering
chartSeries(russell3000Returns)
volrussel <- sqrt(var(as.vector(russell3000Returns)))
volrussel

# VaR
russellvar<-VaR(russell3000Returns,p=0.99,method = "historical")
russellvar


### Tech Stock- Amazan,facebook, Google, and Microsoft

## a) AMAZON
getSymbols("AMZN",from=startdate ,to=enddate, src="yahoo")
chartSeries(AMZN)
summary(AMZN)

#Get monthly return for QCOM
amznReturns<- dailyReturn(AMZN)
amznReturns

#Volatility and Volatility clustering
chartSeries(amznReturns)
amznvol<-sqrt(var(as.vector(amznReturns)))
amznvol

# Beta
amznBeta<- CAPM.beta(amznReturns,russell3000Returns)
amznBeta

# Value at Risk
amznvar<-VaR(amznReturns,p=0.99,method = "historical")
amznvar


## b) Facebook inc
getSymbols("FB",from=startdate ,to=enddate, src="yahoo")
chartSeries(FB)
summary(FB)

# Get monthly return for FB
fbReturns<- dailyReturn(FB)
fbReturns

# Volatility and Volatility clustering
chartSeries(fbReturns)
fbvol=sqrt(var(as.vector(fbReturns)))
fbvol

# Beta
fbBeta<- CAPM.beta(fbReturns,russell3000Returns)
fbBeta

# Value at Risk
fbvar<-VaR(fbReturns,p=0.99,method = "historical")
fbvar


## c) GOOGLE 
getSymbols("GOOGL",from=startdate ,to=enddate, src="yahoo")
chartSeries(GOOGL)
summary(GOOGL)

# Get monthly return for FB
googleReturns<- dailyReturn(GOOGL)
googleReturns

# Volatility clustering
chartSeries(googleReturns)
googlevol=sqrt(var(as.vector(googleReturns)))
googlevol

# Beta
googleBeta<- CAPM.beta(googleReturns,russell3000Returns)
googleBeta

# Value at Risk
googlevar<-VaR(googleReturns,p=0.99,method = "historical")
googlevar


## d) MICROSOFT 
getSymbols("MSFT",from=startdate ,to=enddate, src="yahoo")

# Get monthly return for FB
msftReturns<- dailyReturn(MSFT)
chartSeries(MSFT)
summary(MSFT)

#Volatility and Volatility clustering
chartSeries(msftReturns)
msftvol=sqrt(var(as.vector(msftReturns)))
msftvol

# Beta
msftBeta<- CAPM.beta(msftReturns,russell3000Returns)
msftBeta

# Value at Risk
msftvar<-VaR(msftReturns,p=0.99,method = "historical")
msftvar


#### GLOBAL MINIMUM VARIANCE PORTFOLIO
# Dataframe of Stocks
PortfolioReturns<-cbind(amznReturns,fbReturns,googleReturns,msftReturns)

# Create Vector of ticker
ticker <-c("AMZN","FB","GOOGL","MSFT")

#Assign ticker to the dataframe
colnames(PortfolioReturns)<-ticker

# Correlation
cor(PortfolioReturns)


# Convert to a Matrix
PortfReturns<- as.matrix(PortfolioReturns)

#Calculating Portfolio Weight Using Regression method

y<-PortfReturns[,1]
x<-PortfReturns[,1]-PortfReturns[,2:4]

# linear Model
reg<- lm(y~x)
summary(reg)

# GMVP weights
gmvpweights<- as.vector(c(1-sum(coef(reg)[-1L]),coef(reg)[-1L]))
gmvpweights<- matrix(gmvpweights,nrow=1,ncol=4)
colnames(gmvpweights)<-ticker
gmvpweights *100

# Expected return of the GMVP portfolio
reg$coefficients[1]

# Varince of the GMVP portfolio
sqrt(var(reg$residuals))


### Mean Varince portfolio
MvP <-portfolio.optim(PortfolioReturns)

#Mean Variance Weights 
MvPweights <- MvP$pw
MvPweights

#Expected return of the portfolio
MvP$pm

# Varince of the portfolio
MvP$ps


sqrt(var(MvP$px))

#### Result
#
vol= data.frame(RUSSEL=volrussel,AMZN=amznvol,FB= fbvol,GOOGL=googlevol,
                MSFT=msftvol,GMVP= sqrt(var(reg$residuals)))
vol *100
