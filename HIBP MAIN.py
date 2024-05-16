
import time
import pyhibp
from pyhibp import pwnedpasswords as pw


def main():

    infile = open("Test_Email.txt", "r")
    outfile = open("Output.txt", "w")
    YOUR_API_KEY = "*Insert API Key Here"
    
    

    def rate_limit():
        # Make a function to avoid hitting the HIBP API rate limit
        time.sleep(15)

    #Key is authenticated to the HIBP API to verify subscription
    if YOUR_API_KEY is not None:
        pyhibp.set_api_key(key=YOUR_API_KEY)

    

    pyhibp.set_user_agent(ua="Kawasaki app 1.0 : I just wanna see emails")


    for line in infile:

        y = 0

        if YOUR_API_KEY is not None:
            # API Key Required. Get breaches that affect a given account, truncate the response to the breach names
            #   and include unverified breaches
            
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

        rate_limit()   

    outfile.close()
    infile.close()    

main()
