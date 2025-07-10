#Author: S.A.Y.R. Samaraweera
#Date: 24/12/2024
#Student ID: 20231515 / w2120238

# Import Modules
import csv
import tkinter as tk

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    
    while True:
        # Use try and except to handle any errors
        try:
            # Get user input for the day in the format dd
            day = int(input("\nPlease enter the day of the survey in the format dd: "))

            # Check if the date is within the range
            if not(1 <= day <=31):  
                print("Out of range - Value must be in the range 1 to 31")
                continue

        # Handle the error where the input is not an integer
        except ValueError:
            print("Integer Required")
            continue
        
        # Nested while loop to get user input of the month and handle errors same as day
        while True:
            try:
                month = int(input("Please enter the month of the survey in the format mm: "))
                if not(1 <= month <= 12):
                    print("Out of range - Value must be in the range 1 to 12\n")
                    continue
                elif (month in (4,6,9,11) and day > 30) or (month == 2 and day > 29):
                    print(f"The month you entered does not include {day}")
                    continue
                    
            except ValueError:
                print("Integer Required")
                continue

            # Nested while loop to get the user input for the year and handle errors same as day and month
            while True:
                try:
                    year = int(input("Please enter the year of the survey in the format yyyy: "))
                    if not(2000 <= year <= 2024):
                        print("Out of range - Value must be in the range 2000 to 2024\n")
                        continue
                    elif day == 29 and month == 2 and year % 4 != 0:
                        print("The year you entered is not a leap year.\n")
                        continue

                except ValueError:
                    print("Integer Required")
                    continue

                # Return the date in DD MM YYYY format
                return(day,month,year)


def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """

    # while loop to validate user choice
    while True:
        # Get user input for choice
        choice = input("Do you want to select another data file for a different date? Y/N: ")

        # Validate the user input and return the choice if the input is valid
        if choice == "Y" or choice == "y" or choice == "N" or choice == "n":
            return choice

        else:
            print("Please enter 'Y' or 'N'")

    
# Task B: Processed Outcomes    
def process_csv_data(day, month, year):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """

    # Create date string
    date = f"{day:02}/{month:02}/{year}"
    # Get the file name from the user input date
    csv_file_name = (f"traffic_data{day:02}{month:02}{year}.csv")

    # Initialize variables
    total_vehicles = 0
    total_trucks = 0
    total_electrics = 0
    two_wheeled = 0
    busses_elm_north = 0
    no_turning_total = 0
    trucks_percentage = 0
    total_bicycles = 0
    bicycles_average = 0
    over_speed_total = 0
    elm_total = 0
    hanley_total = 0
    total_scooters_elm = 0
    elm_scooter_percentage = 0
    hanley_peak_total = 0
    hanley_peak_hours = [] # List to append peak hours if there are multiple hours
    hourly_vehicle_count_hanley = [0] * 24 # List of hourly vehicle count in Hanley Highway/Westway with index for each hour
    starting_peak = 0
    ending_peak = 0
    rain_hours_list = [] # List of hours that rained to calculate the rain hours
    rain_hours = 0
    hourly_vehicle_count_elm = [0] * 24 # # List of hourly vehicle count in Elm Avenue/Rabbit Road with index for each hour 

    # Open the csv file using the csv module
    with open(csv_file_name, 'r') as file:
        traffic_data = csv.reader(file)
        # Use next() to skip the header row
        next(traffic_data)

        # Process dara in the csv file using for loops and conditions
        for row in traffic_data:
            # Calculate total vehicles passed through all junctions
            total_vehicles += 1
            # Calculate total trucks
            if row[8] == "Truck":
                total_trucks += 1
            # Calculate total electric vehicles
            if row[9] == "True":
                total_electrics += 1
            # Calculate all the two wheeled vehicles
            if row[8] in ["Bicycle", "Motorcycle", "Scooter"]:
                two_wheeled += 1
            # Calculate the busses leaving elm street heading north
            if row[0] == "Elm Avenue/Rabbit Road" and row[4] == "N" and row[8] == "Buss":
                busses_elm_north += 1
            # Calculate vehicles that went though both junctions without turning
            if row[3] == row[4]:
                no_turning_total += 1
            # Calculate the total bicycles to get the average
            if row[8] == "Bicycle":
                total_bicycles += 1
            # Compare the speed limit and vehicle's speed to get the over speed vehicles
            if int(row[6]) < int(row[7]):
                over_speed_total += 1
            # Calculate total vehicles only went through Elm Avenue/Rabbit Road
            if row[0] == "Elm Avenue/Rabbit Road":
                elm_total += 1
            # Calculate total vehicles only went through Hanley Highway/Westway  
            if row[0] == "Hanley Highway/Westway":
                hanley_total += 1
            # Calculate total scooters only went through Elm Avenue/Rabbit Road to get the percentage
            if row[0] == "Elm Avenue/Rabbit Road" and row[8] == "Scooter":
                total_scooters_elm += 1
            # Get the hour by splitting the hour from ":"
            hour = int(row[2].split(":")[0])
            # Calculate the total vehicles on each hour of Hanley Highway/Westway
            if row[0] == "Hanley Highway/Westway":
                hourly_vehicle_count_hanley[hour] += 1
            # Calculate the total vahicles on each hour of Elm Avenue/Rabbit Road
            if row[0] == "Elm Avenue/Rabbit Road":
                hourly_vehicle_count_elm[hour] += 1
            # Get the hours that rained in the selected day
            if row[5] == "Light Rain" or row[5] == "Heavy Rain":
                # If the hour is not in the rain_hours_list append it to the list
                if hour not in (rain_hours_list):
                    rain_hours_list.append(hour)
        # Calculate the rain_hour by getting the length of the list  
        rain_hours = len(rain_hours_list)

        # Get the percentages and averages as integers using the round() function        
        trucks_percentage = round((total_trucks/total_vehicles)*100)
        bicycles_average = round(total_bicycles/24)
        elm_scooter_percentage = round((total_scooters_elm/elm_total)*100)
        # Get total vehicles in the peak hour with max() function
        hanley_peak_total = max(hourly_vehicle_count_hanley)
        # Get the peak hour range with a for loop and if conditions
        for index in range(24):
            if hourly_vehicle_count_hanley[index] == hanley_peak_total:
                # Get the index of the peak hour
                starting_peak = (f"{index}:00")
                # If the starting_peak hour is 23:00 the ending_peak will be 00:00 of next day
                if index == 23:
                    ending_peak = ("00:00")
                # Otherwise increament starting_peak by 1
                else:
                    ending_peak = (f"{index+1}:00")
                # Append the peak hour ranges to hanley_peak_hours list
                hanley_peak_hours.append(f"between {starting_peak} and {ending_peak}")
                
        # Save the results in a dictionary
        outcomes = {"date": date,
                    "csv_file_name": csv_file_name,
                    "total_vehicles": total_vehicles,
                    "total_trucks": total_trucks,
                    "total_electrics": total_electrics,
                    "two_wheeled": two_wheeled,
                    "busses_elm_north": busses_elm_north,
                    "no_turning_total": no_turning_total,
                    "trucks_percentage": trucks_percentage,
                    "bicycles_average": bicycles_average,
                    "over_speed_total": over_speed_total,
                    "elm_total": elm_total,
                    "hanley_total": hanley_total,
                    "elm_scooter_percentage": elm_scooter_percentage,
                    "hanley_peak_total": hanley_peak_total,
                    "hanley_peak_hours": hanley_peak_hours,
                    "rain_hours": rain_hours,
                    "hourly_vehicle_count_hanley": hourly_vehicle_count_hanley,
                    "hourly_vehicle_count_elm": hourly_vehicle_count_elm}
        # Return the outcomes dictionary
        return outcomes
    
def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """

    # Initialize variables
    peak_hours = ''
    
    # for loop to display the peak_hours in hanley_peak_hours
    for i in (outcomes['hanley_peak_hours']):
        peak_hours += (i)
    
        # Display the output using a print statement
    results = (f"\n{'*'*50} \ndata file selected is {outcomes['csv_file_name']} \n{'*'*50}\n"
               f"\nThe total number of vehicles recorded for this date is {outcomes['total_vehicles']}\n"
               f"The total number of trucks recorded for this data is {outcomes['total_trucks']}\n"
               f"The total number of electric vehicles for this date is {outcomes['total_electrics']}\n"
               f"The total number of two wheeled vehicles for this data is {outcomes['two_wheeled']}\n"
               f"The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes['busses_elm_north']}\n"
               f"The total number of vehicles through both junctions not turning left or right is {outcomes['no_turning_total']}\n"
               f"The percentage of total vehicles recorded that are trucks for this data is {outcomes['trucks_percentage']}%\n"
               f"The average number of bicycles per hour for this date is {outcomes['bicycles_average']}\n"
               f"\nThe total number of vehicles recorded as over the speed limit for this date is {outcomes['over_speed_total']}\n"
               f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['elm_total']}\n"
               f"The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['hanley_total']}\n"
               f"{outcomes['elm_scooter_percentage']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n"
               f"\nThe highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes['hanley_peak_total']}\n"
               f"The most vehicles through Hanley Highway/Westway were recorded {peak_hours}\n"
               f"The number of hours of rain for this date is {outcomes['rain_hours']}\n")

    return results
              
# Task C: Save Results to Text File
def save_results_to_file(results, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    # create and open the text file
    with open(file_name, 'a') as text_file:
        text_file.write(results)
        print("**Text file is ready**")
        
# if you have been contracted to do this assignment please do not remove this line

# Task D: Histogram Display

class HistogramApp:
    def __init__(self, traffic_data_elm, traffic_data_hanley, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        # Set the variables
        self.traffic_data_elm = traffic_data_elm
        self.traffic_data_hanley = traffic_data_hanley
        self.date = date
        self.bar_width = 20
        self.bar_spacing = 50
        self.bar_height = 350
        # Get the maximum vehicle count of both roads
        self.max_veh_count = max(max(self.traffic_data_elm), max(self.traffic_data_hanley))

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        # Create the tkinter window and give a title
        self.root = tk.Tk()
        self.root.title("Histogram")
        # Create the canvas 
        self.canvas = tk.Canvas(self.root, width=1250, height=600)
        # Set the canvas title
        self.canvas.create_text(275, 25, text=f"Histogram of Vehicle Frequency per Hour ({self.date})", font=16)
        # Add the canvas to the window
        self.canvas.pack()

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        # Create the x-axis
        self.canvas.create_line(30, 550, 1220, 550)
        for hour in range(24):
            # Add labels to the x-axis 
            x = self.bar_spacing + hour * self.bar_spacing
            self.canvas.create_text(x, 560, text=f"{hour:02}", font=("Arial", 7, "bold"))
            # Draw bars for Elm Avenue/Rabbit Road
            vehicle_count_elm = self.traffic_data_elm[hour]
            x1 = 30 + hour * self.bar_spacing
            y1 = 530 - (vehicle_count_elm / self.max_veh_count) * self.bar_height 
            x2 = x1 + self.bar_width
            y2 = 550
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            # Add the elm vehicle count
            self.canvas.create_text(x1 + 10, y1 - 10, text=vehicle_count_elm, fill="blue")
            # Draw bars for Hanley Highway/Westway
            vehicle_count_hanley = self.traffic_data_hanley[hour]
            x1 = 50 + hour * self.bar_spacing
            y1 = 530 - (vehicle_count_hanley / self.max_veh_count) * self.bar_height 
            x2 = x1 + self.bar_width
            y2 = 550
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="light green")
            # Add the hanley vehicle count
            self.canvas.create_text(x1 + 10, y1 - 10, text=vehicle_count_hanley, fill="green")

        # Name the x-axis
        self.canvas.create_text(605, 580, text="Hours 00:00 to 23:00", font=("Arial", 10))

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        self.canvas.create_rectangle(50, 60, 70, 80, fill="blue")
        self.canvas.create_text(160, 70, text="Elm Avenue/Rabbit Road", font=("Arial", 10))
        self.canvas.create_rectangle(50, 90, 70, 110, fill="light green")
        self.canvas.create_text(160, 100, text="Hanley Highway/Westway", font=("Arial", 10))

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        # Loop to display the window
        self.root.mainloop()


# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None

    def load_csv_file(self, day, month, year):
        """
        Loads a CSV file and processes its data.
        """
        try:
            outcomes = process_csv_data(day, month, year)
            results = (display_outcomes(outcomes))
            print(results)
            save_results_to_file(results, file_name="results.txt")

            # Draw the histogram
            traffic_data_elm = outcomes['hourly_vehicle_count_elm']
            traffic_data_hanley = outcomes['hourly_vehicle_count_hanley']
            date = outcomes['date']
            histogram = HistogramApp(traffic_data_elm, traffic_data_hanley, date)
            histogram.run()

        # If the file is empty, handle the error
        except ZeroDivisionError:
            print("\n**The file is empty**")
        # If the csv file doesn't exist, handle the error
        except FileNotFoundError:
            print("\n**The file does not exist**")

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        self.current_data = None

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        while True:
            try:
                # Call the functions to run the program
                (day, month, year) = validate_date_input()

                # Process the csv file
                self.load_csv_file(day, month, year)

                # Ask the user if they want to process another file
                choice = validate_continue_input()

                # if the user input no break the loop and end the program.
                if choice == "N" or choice == "n":
                    print("\nEnd of the program!")
                    break
            except Exception as e:
                print(f"{e}. Please try agin")
            

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        self.handle_user_interaction()

# Creating main() function 
def main():
    program = MultiCSVProcessor()
    program.process_files()

# Call the main() function to run the program if __name__ == "__main__"
if __name__ == "__main__":
    main()
