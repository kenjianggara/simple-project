import requests
from bs4 import BeautifulSoup
import datetime
import os

# Clear the console screen
def clear_screen():
    if os.name == 'posix':
        # For Unix and Linux
        os.system('clear')
    elif os.name == 'nt':
        # For Windows
        os.system('cls')

# Dictionary mapping hotel names to their URL fragments
hotel_urls = {
    "Ranca Upas": "bobocabin-ranca-upas-1017",
    "Cikole": "bobocabin-cikole-1019",
    "Pangalengan": "bobocabin-pangalengan-1037",
}

# Function to scrape hotel prices
def scrape_hotel_prices(url):
    try:
        # Send a GET request to the hotel website
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract hotel price information
        price_element = soup.find('label', class_='md:heading-5 ml-1 text-imperialred-50')
        if price_element:
            price = price_element.text
            return price
        else:
            return "Price not found"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Function to validate dates
def validate_dates(checkin_date, checkout_date):
    try:
        today = datetime.date.today()
        checkin_date = datetime.datetime.strptime(checkin_date, "%Y-%m-%d").date()
        checkout_date = datetime.datetime.strptime(checkout_date, "%Y-%m-%d").date()
        
        if checkin_date < today:
            return "Check-in date cannot be earlier than today."
        if checkout_date > checkin_date:
            return "Checkout date must be after check-in date."
        else:
            return None
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
def logo():
    print("")
    print("                            .:^!7??JJJJJJJ??7~^:                           ")
    print("                         :~7?JYYYJJJJJJJJJJJJJJJ?7^.                       ")
    print("                      .~?JYYJJJ?JJJYJJJJJJJJJJJJJYYJ7^.                    ")
    print("                    .!JYYJ7~:.  ..:~?JJJJJJJJJJJJJJJJYJ~.                  ")
    print("                   ~JYJJ?:       ::  ^JJJJJJJJJJJJJJJJJY?^                 ")
    print("                 .7YJJJJ:         !:  ^YYJJJJJJJJJJJJJJJJY!                ")
    print("                .?YJJJJ?          ^. .^!7?JJYYJJJJJJJJJJJJY7               ")
    print("                7YJJJJJJ.                 .:~7JYJJJJJJJJJJJY!              ")
    print("               ^YJJJJJJJ?:  .:                .^?JJJYYYJJJJJJ:             ")
    print("               7YJJJJJJJJJ7!^.                   ^?7~~!7JJYJY!             ")
    print("              .JJJJJJJJJJJJ^    ^..               .^    .^7JJ?             ")
    print("              .JJJJJJJJJJY!     .^:  :!77.          ^^^^:  ~J?             ")
    print("               7JJJJJJJJJY^        .7JYJY^          .       77             ")
    print("               ^YJJJJJYYYY7        ~YYYY?  :.               !^             ")
    print("                ?YJYJ7!~^:^~.       :~!~.  .^:.   .        :!              ")
    print("                .J?^.       .    .:^^^^^^^^^^^:  ^~      .~7.              ")
    print("                 .!:           .~^^:.        .:~7J~:::^~7J?.               ")
    print("                  .!~.         ~7^:...:    .:^^^77?JJYYYJ~                 ")
    print("                    :!^.       !^  ~^:. .^^^:.     .:7J!.                  ")
    print("                      :~~:.    ^~:~7::^~^:        .:~~:                    ")
    print("                        .^~~^:. ... ...       .:^~~:.                      ")
    print("                            .:^^^^^::::::^^^^^^:.                          ")
    print("                                 ....:::....                               ")
    print("")
    print("!!                    ^7:                    !!                            ")
    print("Y?                    ~Y^                   .JJ                            ")
    print("J?:^~~^.     .^~~^.   ~Y~:~~^:      :~~~:   .J?:^~~^.     .^~~^.   :~:  .^~")
    print("JJ?!~!?J~  .7J7~~7J!. ~YJ7~~!J7.  ^??!~!??^ .JJ?!~!?J~  .7J7~~7J!. :!??7J7~")
    print("YJ.    !Y^ 7Y:    ^Y! ~Y~    :Y? :Y7     ?J..JJ.    !Y^ 7Y:    ^Y!    ?Y^  ")
    print("7J~. .:?J. ~Y!.  .7J^ :J?:  .~Y! .?J^. .^J7  7J~. .:?J. ~Y!.  :7J^  .^JY!. ")
    print(" ~?????!.   ^7????7:   :7?????^   .!?????~    ~?????!.   ^7????7:  ^??~^7??")
    print("")                                                                     

# Main function
if __name__ == "__main__":
        
    logo()
    # Display a menu of hotel choices to the user
    print("Choose a BoboCabin location:")
    for index, hotel_name in enumerate(hotel_urls.keys(), 1):
        print(f"{index}. {hotel_name}")
    
    # Prompt the user to select a hotel
    while True:
        try:
            choice = int(input("Enter the number of the Cabin you want to check: "))
            if 1 <= choice <= len(hotel_urls):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get user input for check-in date and continuously validate
    while True:
        checkin_date = input("Enter check-in date (YYYY-MM-DD): ")
        validation_result = validate_dates(checkin_date, datetime.date.today().strftime("%Y-%m-%d"))
        if validation_result is None:
            break
        else:
            print(validation_result)
    
    # Get user input for checkout date and continuously validate
    while True:
        checkout_date = input("Enter checkout date (YYYY-MM-DD): ")
        validation_result = validate_dates(checkout_date, checkin_date)
        if validation_result is None:
            clear_screen
            break
        else:
            print(validation_result)
    
    # Construct the URL with user inputs
    selected_hotel = list(hotel_urls.keys())[choice - 1]
    hotel_url_fragment = hotel_urls[selected_hotel]
    full_url = f"https://bobobox.com/bobocabin/jawa-barat/{hotel_url_fragment}/?checkin={checkin_date}&checkout={checkout_date}"
    
    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Scrape hotel prices
    hotel_price = scrape_hotel_prices(full_url)
    
    # Print the results
    logo()
    print(f"BoboCabin Starting Price for {selected_hotel} on {current_time} for {checkin_date} - {checkout_date} is: \nRp. {hotel_price}")
        
