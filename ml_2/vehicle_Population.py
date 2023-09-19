import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the CSV data
data = pd.read_csv('vehicle_Population.csv')

while True:
    print("Select a graph to view:")
    print("1. Histogram")
    print("2. Scatter Plot")
    print("3. Line Graph")
    print("4. Pie Chart")
    print("0. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        # Create a histogram
        plt.figure(figsize=(10, 6))
        # Modify this part to create your specific histogram
        plt.hist(data['Electric Vehicle (EV) Total'], bins=20, color='g', alpha=0.7)
        plt.title('Histogram Example')
        plt.xlabel('EV Total')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    elif choice == "2":
        # Create a scatter plot
        plt.figure(figsize=(10, 6))
        # Modify this part to create your specific scatter plot
        plt.scatter(data['Battery Electric Vehicles (BEVs)'], data['Plug-In Hybrid Electric Vehicles (PHEVs)'], color='r')
        plt.title('Scatter Plot Example')
        plt.xlabel('BEVs Total')
        plt.ylabel('PHEVs Total')
        plt.tight_layout()
        plt.show()
    elif choice == "3":
        # Create a line graph
        plt.figure(figsize=(10, 6))
        # Modify this part to create your specific line graph
        plt.plot(data['Date'], data['Electric Vehicle (EV) Total'], marker='o', linestyle='-', color='b')
        plt.title('Line Graph Example')
        plt.xlabel('Date')
        plt.ylabel('EV Total')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    elif choice == "4":
        # Create a pie chart
        plt.figure(figsize=(8, 8))
        # Modify this part to create your specific pie chart
        vehicle_use = data.groupby('Vehicle Primary Use')['Percent Electric Vehicles'].mean()
        vehicle_use.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Pie Chart Example')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()
    elif choice == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
