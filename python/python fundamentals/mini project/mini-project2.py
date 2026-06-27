def calculate_server_costs():
    cost_per_hour = 0.51
    cost_per_day = cost_per_hour * 24
    cost_per_week = cost_per_day * 7
    cost_per_month = cost_per_day * 30 # Assuming 30 days in a month for calculation
    
    budget = 918
    days_with_budget = budget / cost_per_day
    
    print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
    print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
    print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
    print(f"Days I can operate one server with ${budget}: {days_with_budget:.0f} days")

if __name__ == "__main__":
    calculate_server_costs()