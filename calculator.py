check_affordability(monthly_income, monthly_rent, agency_fee=0, service_charge=0):
recommended_max_housing = monthly_income * 0.30
security_deposit = monthly_rent
total_move_in_cost = monthly_rent + security_deposit + agency_fee
total_monthly_cost = monthly_rent + service_charge
    
    print("--- 🏠 RentWise Financial Analysis 📊 ---")
    print(f"Total Cash Needed to Move In: KES {total_move_in_cost:,}")
    print(f"Total True Cost per Month: KES {total_monthly_cost:,}")
    
    if total_monthly_cost > recommended_max_housing:
        print("\n⚠️ Financial Warning: This rent exceeds 30% of your income.")
        print(f"Based on your income, your recommended max monthly budget is KES {recommended_max_housing:,}.")
    else:
        print("\n✅ Financial Check: This rent looks affordable based on your income!")
      user_income = 80000
rent_price = 25000
agent_fee = 5000      
monthly_service = 2000
check_affordability(user_income, rent_price, agent_fee, monthly_service)
