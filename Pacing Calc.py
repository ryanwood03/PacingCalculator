# Heading
   
print("This program allows you to calculate the optimal and current pacing percentages, along with a projection of where things will be on day 28 based on recent days of CustomerSpend.")

print("\n")

# Input the number of days completed in the month so far and define the number of days left

prompt1=number_of_days = eval(input("Enter the amount of days that have elapsed so far this month? For example, if today is March 23rd, enter: 22\n"))

print("\n")

days_left = (28-number_of_days)

# Input the CustomerSpend budgetary cap and MTD CustomerSpend

prompt2=budget = eval(input("Enter the CustomerSpend budgetary cap\n"))

print("\n")

prompt3=mtd_customerspend = eval(input("Enter the campaign's MTD CustomerSpend?\n"))

print("\n")


# Compute CustomerSpend average over last three days or input CustomerSpend for yesterday

prompt4=input("Has the CustomerSpend been relatively consistent over the last three days? Within $50 or so? Enter Y or N\n")

if prompt4 == 'y':
        prompt4=customerspend_1, customerspend_2, customerspend_3 = [int(x) for x in input("Enter CustomerSpend for each of the last three days, seperated by spaced. For example: 27 28 21\n").split()]                                                                       
    
        customer_average = (customerspend_1+customerspend_2+customerspend_3)/3
         
else:
        prompt5=customer_average = eval(input("Enter the CustomerSpend for yesterday\n"))

print("\n")


# Calculate optimal pacing, optimal pacing difference, and projection

projection = (days_left*customer_average)+mtd_customerspend

current_pace = mtd_customerspend / budget * 100

optimal_pace = number_of_days / 28 * 100

# Display the optimal pacing difference (also optimal pacing and current pacing) and projection

print("Find the requested data below")


print("CustomerSpend Projection by day 28: $" , round(projection))


print("Optimal Pace:" , round(optimal_pace, 2) , "%") 


print("Current Pace:" , round(current_pace, 2) , "%")









