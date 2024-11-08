from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QComboBox
import numpy as np
import sys
from finance_data import get_risk_free_rate

# Define function to update the risk-free rate when the dropdown selection changes
def update_risk_free_rate():
    risk_free_rate_selection = dropdown_risk_free.currentText()
    risk_free_rate = get_risk_free_rate(risk_free_rate_selection)

    if risk_free_rate is not None:
        risk_free_rate_label.setText(f"Risk-Free Rate: {risk_free_rate:.2%}")
    else:
        risk_free_rate_label.setText("Risk-Free Rate: not available")

def calculate_sharpe_ratio():
    try:
        # Get values from input fields
        net_profit_text = entry_net_profit.text()
        months_text = entry_months.text()
        initial_capital_text = entry_initial_capital.text()

        net_profit = float(net_profit_text)
        months = int(months_text)
        initial_capital = float(initial_capital_text)

        if initial_capital <= 0 or months <= 0:
            QMessageBox.critical(window, "Error", "Initial capital and number of months must be greater than zero.")
            return

        avg_monthly_return = (net_profit / initial_capital) / months

        # Get the risk-free rate and convert it to a monthly rate
        risk_free_rate_selection = dropdown_risk_free.currentText()
        risk_free_rate = get_risk_free_rate(risk_free_rate_selection)

        if risk_free_rate is None:
            QMessageBox.critical(window, "Error", "Failed to retrieve the risk-free rate. Please check your internet connection or the selected data.")
            return

        monthly_risk_free_rate = risk_free_rate / 12

        # Display the risk-free rate in the interface
        risk_free_rate_label.setText(f"Risk-Free Rate: {risk_free_rate:.2%}")

        # Calculate standard deviation (assuming constant monthly profit for simplicity)
        std_dev = avg_monthly_return / 10  # Assumed standard deviation for example purposes

        if std_dev == 0:
            QMessageBox.warning(window, "Warning", "Standard deviation is zero, Sharpe Ratio cannot be calculated.")
            return

        # Calculate Sharpe Ratio
        sharpe_ratio = (avg_monthly_return - monthly_risk_free_rate) / std_dev

        if np.isinf(sharpe_ratio):
            QMessageBox.warning(window, "Warning", "Sharpe Ratio is infinite (inf), possibly due to division by a very small standard deviation.")
            return

        # Display the result
        QMessageBox.information(window, "Sharpe Ratio", f"Sharpe Ratio: {sharpe_ratio:.2f}")
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Error during calculation: {e}")

# Create the graphical interface
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Sharpe Ratio Calculator")

# Create layout
layout = QVBoxLayout()

# Label and input field for net profit
label_net_profit = QLabel("Net Profit:")
layout.addWidget(label_net_profit)
entry_net_profit = QLineEdit()
layout.addWidget(entry_net_profit)

# Label and input field for number of months
label_months = QLabel("Number of Months:")
layout.addWidget(label_months)
entry_months = QLineEdit()
layout.addWidget(entry_months)

# Label and input field for initial capital
label_initial_capital = QLabel("Initial Capital:")
layout.addWidget(label_initial_capital)
entry_initial_capital = QLineEdit()
layout.addWidget(entry_initial_capital)

# Label and dropdown for risk-free rate
label_risk_free = QLabel("Select Risk-Free Rate (1-Year Data):")
layout.addWidget(label_risk_free)
dropdown_risk_free = QComboBox()
dropdown_risk_free.addItems(["S&P 500 (1-Year Average Return)", "US (1-Year Treasury Bond)", "EU (1-Year European Government Bonds)", "Emerging Markets (1-Year Government Bonds)", "Corporate Bonds (1-Year Low Risk)"])
dropdown_risk_free.currentIndexChanged.connect(update_risk_free_rate)  # Connect selection change to update function
layout.addWidget(dropdown_risk_free)

# Get the default risk-free rate at program startup
initial_risk_free_rate = get_risk_free_rate("S&P 500 (1-Year Average Return)")
if initial_risk_free_rate is not None:
    initial_risk_free_rate_text = f"Risk-Free Rate: {initial_risk_free_rate:.2%}"
else:
    initial_risk_free_rate_text = "Risk-Free Rate: not available"

# Label to display the risk-free rate
risk_free_rate_label = QLabel(initial_risk_free_rate_text)
layout.addWidget(risk_free_rate_label)

# Button to calculate Sharpe Ratio
button_calculate = QPushButton("Calculate Sharpe Ratio")
button_calculate.clicked.connect(calculate_sharpe_ratio)
layout.addWidget(button_calculate)

# Set layout for the window
window.setLayout(layout)

# Show the window
window.show()

# Run the GUI
sys.exit(app.exec())
