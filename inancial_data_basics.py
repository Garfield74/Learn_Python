# financial_data_basics.py
# A beginner-friendly Python file for learning basic data handling with financial context
# Perfect first file for someone interested in Agentic AI in FP&A

# 1. HELLO WORLD - Starting simple
print("Hello World!")
print("Welcome to Financial Data Analysis with Python!")
print("-" * 50)

# 2. BASIC VARIABLES - Store financial data
company_name = "TechCorp Inc."
current_year = 2024
revenue_target = 1000000  # $1M target

print(f"Company: {company_name}")
print(f"Year: {current_year}")
print(f"Revenue Target: ${revenue_target:,}")
print()

# 3. WORKING WITH LISTS - Monthly revenue data
monthly_revenue = [85000, 92000, 88000, 95000, 103000, 97000, 
                  110000, 105000, 115000, 120000, 108000, 125000]

print("Monthly Revenue Data:")
for i, revenue in enumerate(monthly_revenue, 1):
    print(f"Month {i}: ${revenue:,}")
print()

# 4. BASIC CALCULATIONS - Key financial metrics
total_revenue = sum(monthly_revenue)
average_monthly = total_revenue / len(monthly_revenue)
max_month = max(monthly_revenue)
min_month = min(monthly_revenue)

print("FINANCIAL ANALYSIS:")
print(f"Total Annual Revenue: ${total_revenue:,}")
print(f"Average Monthly Revenue: ${average_monthly:,.2f}")
print(f"Best Month: ${max_month:,}")
print(f"Worst Month: ${min_month:,}")
print(f"Target Achievement: {(total_revenue/revenue_target)*100:.1f}%")
print()

# 5. DICTIONARIES - Organizing financial data
financial_metrics = {
    "revenue": total_revenue,
    "expenses": 850000,
    "profit": total_revenue - 850000,
    "profit_margin": ((total_revenue - 850000) / total_revenue) * 100
}

print("KEY METRICS:")
for metric, value in financial_metrics.items():
    if metric == "profit_margin":
        print(f"{metric.title()}: {value:.2f}%")
    else:
        print(f"{metric.title()}: ${value:,}")
print()

# 6. AUTOMATION - Growth rate calculations
print("MONTH-OVER-MONTH GROWTH RATES:")
for i in range(1, len(monthly_revenue)):
    previous_month = monthly_revenue[i-1]
    current_month = monthly_revenue[i]
    growth_rate = ((current_month - previous_month) / previous_month) * 100
    print(f"Month {i+1}: {growth_rate:+.1f}%")
print()

# 7. CONDITIONAL LOGIC - Performance alerts
print("PERFORMANCE ALERTS:")
target_monthly = revenue_target / 12

for i, revenue in enumerate(monthly_revenue, 1):
    if revenue > target_monthly:
        status = "✅ Above Target"
    elif revenue > target_monthly * 0.9:
        status = "⚠️  Close to Target"
    else:
        status = "❌ Below Target"
    
    print(f"Month {i}: {status} (${revenue:,})")
print()

# 8. SIMPLE FORECASTING - Next month prediction
# Basic trend analysis using last 3 months
recent_months = monthly_revenue[-3:]
trend = sum(recent_months) / len(recent_months)
predicted_next_month = trend * 1.02  # Assume 2% growth

print("SIMPLE FORECAST:")
print(f"Average of last 3 months: ${trend:,.2f}")
print(f"Predicted next month: ${predicted_next_month:,.2f}")
print()

# 9. DATA SUMMARY FUNCTION - Building reusable code
def analyze_financial_data(data, description):
    """A simple function to analyze any financial data list"""
    return {
        "description": description,
        "total": sum(data),
        "average": sum(data) / len(data),
        "maximum": max(data),
        "minimum": min(data),
        "count": len(data)
    }

# Test the function with quarterly data
quarterly_data = [270000, 285000, 320000, 358000]  # Q1, Q2, Q3, Q4
quarterly_analysis = analyze_financial_data(quarterly_data, "Quarterly Revenue")

print("QUARTERLY ANALYSIS:")
for key, value in quarterly_analysis.items():
    if key == "description":
        print(f"{key.title()}: {value}")
    elif key == "count":
        print(f"{key.title()}: {value} quarters")
    else:
        print(f"{key.title()}: ${value:,.2f}")

print("\n" + "="*50)
print("🎉 Congratulations! You've completed your first Python financial analysis!")
print("Next steps: Learn about pandas, APIs, and machine learning for FP&A!")
print("="*50)
