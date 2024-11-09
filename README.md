# Sharpe Ratio Calculator

## Overview

Sharpe Ratio Calculator is a simple desktop application that helps you calculate the Sharpe Ratio for your investment portfolio. The Sharpe Ratio is a widely used metric to assess the performance of an investment by adjusting its risk.

This application is built using Python and the PySide6 library to provide a graphical user interface (GUI). It also fetches risk-free rates from Yahoo Finance using the yfinance library to help make the calculations accurate and up to date.

## Features

- **User-Friendly GUI**: An intuitive graphical interface to input financial data and get results.
- **Dynamic Risk-Free Rate**: Select from multiple available risk-free rate options, such as US Treasury Bonds, European Government Bonds, Corporate Bonds, Emerging Markets Bonds, and the S&P 500 average return.
- **Calculation for Custom Periods**: Input your investment's net profit, the number of months, and the initial capital to easily calculate the Sharpe Ratio.
- **Cross-Platform**: Works on macOS, Windows, and Linux.

## Installation

### Prerequisites

- **Python 3.7+**
- **Pip** (Python package installer)

### Installation Steps

1. **Clone the Repository**

   ```sh
   git clone <repository-url>
   cd sharpe_ratio_calculator
   ```

2. **Create a Virtual Environment**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```sh
   python sharpe_calculator.py
   ```
