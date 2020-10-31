# Import libraries and dependencies
import numpy as np
import pandas as pd
import os
from datetime import datetime,timedelta
import requests
from dotenv import load_dotenv




# Load .env enviroment variables
load_dotenv()

#storing API key for FMPCloud
appkey = os.getenv("FMP_KEY")

#Prelim Dictionary
mapkey={"Date":"date","Net Income Loss":"netincomeloss"}

#"""-----------------           MACC TOOLS !!!!           ---------------"""
#"""  Listed below are the functions that we will use to make the code more condense and clean"""

#Computing Rolling Beta Averages
 #def BETA(df1,df2,WIN):
 #   """Computes rolling beta averages
 #   df1=first DataFrame
 #   df2=second DataFrame (reference DataFrame)
 #   W=specified window for computations"""
    
 #   rolling_covariance = df1.rolling(window=WIN).cov(df2) #gets rolling covariance between DataFrames
 #   rolling_variance = df.rolling(window=WIN).var() # gets rolling variance of DataFrame
  #  rolling_beta = rolling_covariance / rolling_variance #compute rolling beta
  #  return(rollinb_beta)




#Computing Bollinger Bands
# def BBands(df,WIN,S):
 #   """ Computes the Bollinger Bands for given data over specific rolling window
 #   df=DataFrame containing data
  #  WIN=specified window for computations
  #  S=multiple of standard deviations to use for Bollinger Bands; must specify positive or
  #  negative"""
  #  BB = df.rolling(window=WIN).mean() +( S * df.rolling(window=W).std()) #gets Bollinger Bands

    #upper_band.plot(ax=ax)
    #lower_band.plot(ax=ax)
  #  return(BB)




# Data Cleaning (Receives the Data for Cleaning)
# def data_clean(df):
#"""Cleans data: removes null/NA values and converts data to required forms, if necessary"""
    #checks if there are any NAs in the data
    #Removes NA
    # converts data into correct types


    
    
# Horizontal Analysis
 #def HA(df):
 #   """Performs horizontal analysis on data frame"""
    #computes percent changes for horizontal analysis
    #return(df_HA)
    
    
    
# Altman Z-Score
# def AltZ(ratios):
 #   """ Computes Altman's Bankruptcy Z-score to see if company is in danger of 
 #   going bankrupt"""
 #   weights=[1,2,3,4,5,6] #gets the weights that are assigned to Altman Z-score
 #   Z=0.0; #computing the Altman Z-score
 #   return(Z)
    
        
    
    
    
  #########          DEFINING THE CLASS USED IN FINANCIAL ANALYSIS.       ###############

class AccountScrub:
    """ This class is for pulling financial records for a specified company and specified time range
        
     Attributes
        
        
        
        
        
    """
        
        
        
    def __init__(self, ticker="AAPL",
                 start=(datetime.now()-timedelta(days=1095)).strftime("%Y-%m-%d"),end=datetime.now().strftime("%Y-%m-%d")):
#Setting class attributes
        self.ticker=ticker
        self.fin_stat_items=["Date","Symbol","Net Income Loss"]
        self.balance_sheet_items=["Date","Symbol","Net Income Loss"]
        self.fin_ratios_items=["Date","Symbol","Net Income Loss"]
        self.cash_flow_items=["Date","Symbol","Net Income Loss"]
        self.start=start
        self.end=end
        
        
        
    def fin_stat(self):
        tags=self.fin_stat_items #stores the items to collect from API data
        stock_list=pd.DataFrame() #initialize list for stocks
        for tick in self.ticker:
            query=f"https://fmpcloud.io/api/v3/cash-flow-statement-as-reported/{tick}?from={self.start}&to={self.end}&period=quarter&apikey={appkey}"
            response=requests.get(query)   #Making the API query
            data=response.json()          #converting data in json object
            D={}                          #initialize dictionary 
            #Collecting data from json object and putting it into a DataFrame
            for tag in tags:
                if(tag=="Date"):
                    D[tag]=[datetime.strptime(item[mapkey[tag]],"%Y-%m-%d") for item in data] #list comprehension to collect dates
                    D[tag].reverse()
                elif(tag=="Symbol"):
                    D[tag]=[tick for item in data]
                else:
                    D[tag]=[round(float(item[mapkey[tag]]),2) for item in data]
                    D[tag].reverse()
            D=pd.DataFrame(D) #creating DataFrame and specifying the idex
            D.set_index("Date",inplace=True)
        #D.set_index("Date",inplace=True)   #set the index to the "Date" column
        #D.sort_index(ascending=True,inplace=True) #sorting the index
        #D=D[self.start:self.end]                    #refining to selection
            #stock_list.append(D)               #adds stock information to stock list
            stock_list=pd.concat([stock_list,D],axis=0,join='outer') #joins the data Frames
        #stock_list.reset_index(drop=True,inplace=True)
        #stock_list.set_index(keys=["Symbol","Date"],inplace=True)
        #for tick in self.ticker:
            #stock_list.loc[tick].sort_values(by="Date",inplace=True)
        return(stock_list)                          #returning the DataFrame
            



        
        
        
        
        

#    class MCSimulation:
#    """
#    A Python class for runnning Monte Carlo simulation on portfolio price data. 
    

    
#    Attributes
#    ----------
 #   portfolio_data : pandas.DataFrame
 #       portfolio dataframe
 #   weights: list(float)
#        portfolio investment breakdown
#    nSim: int
#        number of samples in simulation
#    nTrading: int
#        number of trading days to simulate
#    simulated_return : pandas.DataFrame
#        Simulated data from Monte Carlo
#    confidence_interval : pandas.Series
#        the 95% confidence intervals for simulated final cumulative returns
        
#    """
    
 #   def __init__(self, portfolio_data, weights="", num_simulation=1000, num_trading_days=252):
#        """
#        Constructs all the necessary attributes for the MCSimulation object.
#
#        Parameters
#        ----------
#        portfolio_data: pandas.DataFrame
#            DataFrame containing stock price information from Alpaca API
#        weights: list(float)
#            A list fractions representing percentage of total investment per stock. DEFAULT: Equal distribution
#        num_simulation: int
#            Number of simulation samples. DEFAULT: 1000 simulation samples
#        num_trading_days: int
#            Number of trading days to simulate. DEFAULT: 252 days (1 year of business days)
#        """
        
        # Check to make sure that all attributes are set
 #       if not isinstance(portfolio_data, pd.DataFrame):
 #           raise TypeError("portfolio_data must be a Pandas DataFrame")
            
        # Set weights if empty, otherwise make sure sum of weights equals one.
 #       if weights == "":
 #           num_stocks = len(portfolio_data.columns.get_level_values(0).unique())
 #           weights = [1.0/num_stocks for s in range(0,num_stocks)]
 #       else:
 #           if round(sum(weights),2) < .99:
 #               raise AttributeError("Sum of portfolio weights must equal one.")
        
        # Calculate daily return if not within dataframe
 #       if not "daily_return" in portfolio_data.columns.get_level_values(1).unique():
 #           close_df = portfolio_data.xs('close',level=1,axis=1).pct_change()
 #           tickers = portfolio_data.columns.get_level_values(0).unique()
 #           column_names = [(x,"daily_return") for x in tickers]
 #           close_df.columns = pd.MultiIndex.from_tuples(column_names)
 #           portfolio_data = portfolio_data.merge(close_df,left_index=True,right_index=True).reindex(columns=tickers,level=0)    
        
        # Set class attributes
#        self.portfolio_data = portfolio_data
#        self.weights = weights
#        self.nSim = num_simulation
#        self.nTrading = num_trading_days
#        self.simulated_return = ""
        
#    def calc_cumulative_return(self):
#        """
#        Calculates the cumulative return of a stock over time using a Monte Carlo simulation (Brownian motion with drift).

 #       """
        
        # Get closing prices of each stock
#        last_prices = self.portfolio_data.xs('close',level=1,axis=1)[-1:].values.tolist()[0]
        
        # Calculate the mean and standard deviation of daily returns for each stock
#        daily_returns = self.portfolio_data.xs('daily_return',level=1,axis=1)
#        mean_returns = daily_returns.mean().tolist()
#        std_returns = daily_returns.std().tolist()
        
        # Initialize empty Dataframe to hold simulated prices
#        portfolio_cumulative_returns = pd.DataFrame()
        
        # Run the simulation of projecting stock prices 'nSim' number of times
#        for n in range(self.nSim):
        
#            if n % 10 == 0:
#                print(f"Running Monte Carlo simulation number {n}.")
        
            # Create a list of lists to contain the simulated values for each stock
#            simvals = [[p] for p in last_prices]
    
            # For each stock in our data:
#            for s in range(len(last_prices)):

                # Simulate the returns for each trading day
#                for i in range(self.nTrading):
        
                    # Calculate the simulated price using the last price within the list
#                    simvals[s].append(simvals[s][-1] * (1 + np.random.normal(mean_returns[s], std_returns[s])))
    
            # Calculate the daily returns of simulated prices
#            sim_df = pd.DataFrame(simvals).T.pct_change()
    
            # Use the `dot` function with the weights to multiply weights with each column's simulated daily returns
#            sim_df = sim_df.dot(self.weights)
    
            # Calculate the normalized, cumulative return series
#            portfolio_cumulative_returns[n] = (1 + sim_df.fillna(0)).cumprod()
        
        # Set attribute to use in plotting
#        self.simulated_return = portfolio_cumulative_returns
        
        # Calculate 95% confidence intervals for final cumulative returns
#        self.confidence_interval = portfolio_cumulative_returns.iloc[-1, :].quantile(q=[0.025, 0.975])
        
#        return portfolio_cumulative_returns
    
#    def plot_simulation(self):
#        """
#        Visualizes the simulated stock trajectories using calc_cumulative_return method.

#        """ 
        
        # Check to make sure that simulation has run previously. 
#        if not isinstance(self.simulated_return,pd.DataFrame):
#            self.calc_cumulative_return()
            
        # Use Pandas plot function to plot the return data
#        plot_title = f"{self.nSim} Simulations of Cumulative Portfolio Return Trajectories Over the Next        {self.nTrading} Trading Days."
#        return self.simulated_return.plot(legend=None,title=plot_title)
    
#    def plot_distribution(self):
#        """
#        Visualizes the distribution of cumulative returns simulated using calc_cumulative_return method.

#        """
        
        # Check to make sure that simulation has run previously. 
#        if not isinstance(self.simulated_return,pd.DataFrame):
#            self.calc_cumulative_return()
        
        # Use the `plot` function to create a probability distribution histogram of simulated ending prices
        # with markings for a 95% confidence interval
#        plot_title = f"Distribution of Final Cumuluative Returns Across All {self.nSim} Simulations"
#        plt = self.simulated_return.iloc[-1, :].plot(kind='hist', bins=10,density=True,title=plot_title)
#        plt.axvline(self.confidence_interval.iloc[0], color='r')
#        plt.axvline(self.confidence_interval.iloc[1], color='r')
#        return plt
    
#    def summarize_cumulative_return(self):
#        """
#        Calculate final summary statistics for Monte Carlo simulated stock data.
        
#        """
        
        # Check to make sure that simulation has run previously. 
#        if not isinstance(self.simulated_return,pd.DataFrame):
#            self.calc_cumulative_return()
            
#        metrics = self.simulated_return.iloc[-1].describe()
#        ci_series = self.confidence_interval
#        ci_series.index = ["95% CI Lower","95% CI Upper"]
#        return metrics.append(ci_series)