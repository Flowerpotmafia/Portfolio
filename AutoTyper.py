import pyautogui, time, TextSorter

def main():

    #get the user input
    #textInput = input("Text: ")

    #run the text through the sorter class
    #text = TextSorter.Text_Sorter(textInput)
    #text.sortText(textInput)

    #time before destruction
    print("Working...")
    time.sleep(5)
    f = open("beemovie.txt", 'r')

    for line in f:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
  
    f.close()


main()