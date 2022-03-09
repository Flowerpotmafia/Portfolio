class Text_Sorter:
    def __init__(self, textInput):
        self.__textInput = textInput
        
    def sortText(self, textInput):
        f = open("typer.txt", 'w')   
        f.seek(0)   #so the next time it runs it will replace    

        for char in self.__textInput:
            if char != " ":
                f.write(char)
            else:
                f.write("\n")


        f.close()


          
                



