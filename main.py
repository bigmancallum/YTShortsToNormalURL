URL = '' #Sets URL blank to start so code runs

URL = input("Please enter a YouTube Shorts URl (i.e. https://www.youtube.com/shorts/jiiwJx2QW-E): ") #Asks user for Shorts URL

#Checks if the text entered is a YouTube Shorts URL, and asks the user to enter one again if not
while "/shorts" not in URL:
    URL = input("\nThat does not appear to be a YouTube Shorts URL.\n\nAn example of one is https://www.youtube.com/shorts/jiiwJx2QW-E\n\nPlease enter a YouTube Shorts URl: ")

print (f"\nYour YouTube Short URL as a regular YouTube video URL is: {URL.replace('/shorts/', '/watch?v=')}") #Displays the Shorts URL as a regular YouTube URL