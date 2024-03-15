
# Stock Data Visualization App


This Python script creates an interactive web application for comparing stock data using Bokeh in Python. The application allows users to input two stock tickers, start and end dates, and select indicators to plot the data.

### How to Use:
1. Enter the stock tickers for comparison in the 'Stock1' and 'Stock2' input fields.
2. Select the start and end dates using the date pickers.
3. Choose indicators to plot from the available options: '100 Day SMA', '30 Day SMA', and 'Linear Regression Line'.
4. Click the 'Load Data' button to load and plot the selected stock data with the chosen indicators.

### Code Explanation:
- The code uses the 'yfinance' library to download stock data based on the input tickers and date range.
- The 'plot_data' function creates a Bokeh figure for visualizing the stock data with customizable indicators.
- The 'on_button_click' function handles the data loading and plotting process based on user inputs.
- The script constructs the layout of the web application using input fields, date pickers, a multi-choice selector for indicators, and a button for loading data.

### Instructions:
- Ensure you have the necessary Python libraries installed, such as 'yfinance' and 'Bokeh'.
- Run the script and access the interactive web application in your web browser to visualize stock data comparisons effectively.

 Happy coding!
