import pyttsx3
import datetime
import speech_recognition as sr   
import smtplib 
from sceret import senderemail , epwd 
from email.message import EmailMessage
import pyautogui
import webbrowser as web
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes



engine = pyttsx3.init()
selected_voice = 0  # Default male (Raiden)

def speak(audio):
    """Speak the given text using the selected voice."""
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    """Change the assistant's voice."""
    global selected_voice
    voices = engine.getProperty('voices')
    
    if voice == 1:
        selected_voice = 1  # Male
        engine.setProperty('voice', voices[0].id)
        speak("Hello, this is Raiden.")
    elif voice == 2:
        selected_voice = 2  # Female
        engine.setProperty('voice', voices[1].id)
        speak("Hello, this is Robin.")

def time():
    """Tell the current time."""
    Time = datetime.datetime.now().strftime("%I:%M %p")  
    speak(f"The current time is {Time}")

def date():
    """Tell the current date."""
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(f"Today's date is {day} {month} {year}")

def greeting():
    """Greet based on the time of day."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon sir !")
    elif 18 <= hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir !")

def wishme():
    """Welcome message when assistant starts."""
    speak("Welcome back  sir.")
    time()
    date()
    greeting()
    speak("Raiden at your service. How can I help you?")

def takecommandmic():
    """Take voice input from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak("Can you please say that again?")
        return "None"
    return query.lower()


# email
def sendEmail(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email ['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


 def sendwhatsmsg(phone_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
   




def searchgoogle():
    speak("what should i search for ?")
    search = takecommandmic()
    web.open("https://www.google.com/search?q="+search)




def news():
    try:
        newsapi = NewsApiClient(api_key=' Use your valid API key')  # Use your valid API key
        speak("What topic do you want the news about?")
        topic = takecommandmic().lower()  # Convert input to lowercase
        
        # ✅ Fetch news using `everything()` for keyword-based searches
        data = newsapi.get_everything(q=topic, language='en', sort_by='relevancy', page_size=5)

        # ✅ Check if API response is successful
        if data.get('status') != 'ok':
            speak(f"Sorry, I couldn't fetch news. API error: {data.get('message', 'Unknown error')}")
            return

        newsdata = data.get('articles', [])

        # ✅ If no articles are found
        if not newsdata:
            speak(f"Sorry, I couldn't find any news about {topic}. Try another topic.")
            return

        # ✅ Loop through articles
        for i, article in enumerate(newsdata):
            title = article.get('title', 'No title available')
            description = article.get('description', 'No description available')
            print(f"{i+1}. {title} - {description}")
            speak(f"News {i+1}: {title}. {description}")

        speak("That's all for now. I'll update you later.")

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, there was an error while fetching the news.")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)





def screenshot():
    # Generate a valid filename with timestamp
    name_img = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the directory where the screenshot will be saved
    save_dir = "ur path"
    
    # Check if the directory exists, if not, create it
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # Create the missing directory
    
    # Create the full file path
    img_path = os.path.join(save_dir, f"{name_img}.png")
    
    # Take and save the screenshot
    img = pyautogui.screenshot()
    img.save(img_path)  # Save the screenshot to the correct path
    
    # Open the screenshot
    img.show()
    
    speak("took screenshot successfully")

if __name__ == "__main__":
    getvoices(1)  # Start with male voice
    wishme()
    voice_names = ["jarvis", "raiden",'ryden','rider']
    bye = ['offline','bye','catch you later']
    tq = ['thank','okay','ok']
    while True:
        query = takecommandmic()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        
        elif any(name in query for name in voice_names):
            getvoices(1)  # Change to male voice
        elif 'robin' in query:
            getvoices(2)  # Change to female voice

        elif 'mail' in query:
            email_list = {
               # Add more contacts here
            }
            try:
                speak("To Whom you want to send mail?")
                name = takecommandmic().lower()
                receiver = email_list[name]
                speak("what is the subject ...!")
                subject = takecommandmic()

                speak("what should i say")
                content = takecommandmic()
                sendEmail(receiver,subject,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak(f"unable to send mail:{e}")
        # elif 'message' in query:
        #     user_name = {
        #         # Add more contacts here
        #     }

        #     try:
        #         speak("To whom do you want to send a WhatsApp message?")
        #         name = takecommandmic().lower()

        #         if name in user_name:
        #             phone_no = user_name[name]
        #             message = ""

        #             while True:
        #                 speak("What message do you want to send?")
        #                 new_msg = takecommandmic()
        #                 message += " " + new_msg

        #                 speak(f"Current message: {message}. Do you want to add more text or send it?")
        #                 speak("Say 'add' to continue adding text, 'send' to send the message, or 'cancel' to discard.")

        #                 confirmation = takecommandmic().lower()

        #                 if 'send' in confirmation:
        #                     speak("Alright, sending the message now.")
        #                     sendwhatsmsg(phone_no, message.strip())
        #                     speak("Message has been sent successfully.")
        #                     break
        #                 elif 'cancel' in confirmation:
        #                     speak("Message sending cancelled.")
        #                     break
        #                 elif 'add' in confirmation:
        #                     speak("Alright, continue adding your message.")
        #                 else:
        #                     speak("I didn't understand that. Please say 'add', 'send', or 'cancel'.")

        #         else:
        #             speak("I couldn't find that contact. Please add them first.")

        #     except Exception as e:
        #         print(e)
        #         speak(f"Unable to send the message: {e}")
       
        elif 'wikipedia' in query:
            try:
                speak("Searching on Wikipedia...!")
                query = query.replace("wikipedia", "").strip()
                
                if query:  # Ensure the query is not empty
                    result = wikipedia.summary(query, sentences=2)
                    print(result)
                    speak(result)
                else:
                    speak("Sorry, I didn't understand what to search on Wikipedia.")

            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for this topic. Please be more specific.")
                print(e.options[:5])  # Show some possible options

            except wikipedia.exceptions.PageError:
                speak("Sorry, no results found on Wikipedia for that query.")

            except wikipedia.exceptions.WikipediaException as e:
                speak("An error occurred while searching Wikipedia.")
                print(f"Wikipedia error: {e}")


        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak("what should i search for on youtube.?")
            topic = takecommandmic()
            pywhatkit.playonyt(topic)

        

        elif 'weather' in query:

            api_key = "Replace with your API key"  # Replace with your API key
            # city = "hyderabad"  # You can modify this or allow user input for different cities
            speak("Which city's weather would you like to know?")
            city = takecommandmic()  # Get city name from voice input
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"

            try:
                res = requests.get(url)
                data = res.json()

                if res.status_code == 200:  # Check if API request was successful
                    weather = data['weather'][0]['main']  # Main weather category (e.g., "Cloudy")
                    desc = data['weather'][0]['description']  # Detailed weather description
                    temp = data['main']['temp']  # Temperature in Fahrenheit
                    temp_c = round((temp - 32) * 5/9, 1)
                    print(f"Weather: {weather}, Temperature: {temp_c}°C, Description: {desc}")
                    speak(f"The weather in {city} is {weather}. The temperature is {temp_c} degrees Celsius. It's {desc}.")
                else:
                    speak("Sorry, I couldn't fetch the weather data.")
                    print(f"Error: {data}")  # Print API response for debugging

            except Exception as e:
                speak("An error occurred while fetching the weather.")
                print(f"Weather API Error: {e}")

        elif 'news' in query:
            news()

        elif 'read' in query:
            text2speech()

        
        elif 'open code' in query:
            os.system("code")
        elif 'instagram' in query:
            os.startfile('https://www.instagram.com/')
        elif 'git' in query:
            path = r"C:\Users\SAGAR\Desktop\git\GitAutoCommit\commit.bat"
            os.startfile(path)
            speak('git contrubution done master...!')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'screenshot' in query:
            screenshot()


        elif 'remember that' in query:
            speak("what should i remeber..?")
            data = takecommandmic()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you told me to rember that"+remember.read())
            
        elif any(name in query for name in tq):
            speak("thank you sir ")
        elif any(name in query for name in bye):
            speak("Raiden logging off. Call me when you need me.")
            quit()
            
