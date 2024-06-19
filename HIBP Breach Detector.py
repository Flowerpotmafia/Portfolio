
import os
import time
import pyhibp
from datetime import datetime
from dotenv import load_dotenv


#this opens the .env file that holds the environmental variables for security
load_dotenv('TestVariables.env')

def main(): 

    #gets the date and time right now to pass along to the output file name
    now = datetime.now() 
    formatted_now = now.strftime("%m-%d-%Y_%Hh-%Mm")

    file_name = f"Results_{formatted_now}.txt"

    YOUR_API_KEY = os.getenv('API_KEY')

    #File opening
    infile = open("Test_Email.txt", "r")
    outfile = open(file_name, "w")    
    
    
    
    def rate_limit():        
        time.sleep(15)
        # Make a function to avoid hitting the HIBP API rate limit

    
    if YOUR_API_KEY is not None:
        pyhibp.set_api_key(key=YOUR_API_KEY)
        #Key is authenticated to the HIBP API to verify subscription

    

    pyhibp.set_user_agent(ua="Kawasaki app 1.0 : I just wanna see emails")


    for line in infile:

        y = 0

        if YOUR_API_KEY is not None:
            # Checking if there is a valid API Key and if there is, it will run this part of the script 
            
            resp = pyhibp.get_account_breaches(account=line.strip(), include_unverified=True)

            if resp:
                
                print(line.strip() + ",")

                output = line.strip() + ","
                outfile.write(output)

                for x in resp:
              

                    whatdict = dict(resp[y])
                    print ("Name: " + whatdict["Name"])
                    print ("Date of Breach: " + whatdict["BreachDate"])

                    y = y + 1

                    output = " Name: " + whatdict["Name"] + " Date of Breach: " + whatdict["BreachDate"] + ","
                    outfile.write(output)
                          

                outfile.write("\n")

            else:
                print(line.strip() + "|CLEAN|")  

        #Calls rate limit so it doesn't go too quickly for the API
        rate_limit() 
        
    #File closing
    outfile.close()
    infile.close()

#Calls main to begin the script
main()