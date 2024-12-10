from tkinter import *
import google.generativeai as gemini

gemini.configure(api_key="API KEY")
model = gemini.GenerativeModel("gemini-1.5-flash")

root = Tk()
root.title = "Password Generator"

label1 = Label(root, text="Let's make you a password")
label1.grid(column=0, row=0)

label2 = Label(root, text="What is something unique or special to you? This can be anything.")
label2.grid(column=0, row=2)
txt1 = Entry(root)
txt1.grid(column=1, row=2)

def generate_words():
    global combinedWords
    combinedWords = ""

    user_input = txt1.get()
    gemini_response = model.generate_content(f"Generate three popular words that are 7+ letters long. The words should aim to use as many common letters in English as possible while minimizing overlap between the three. Customize the words to be related to the theme \"{user_input}\" Return the list of words in the format [word1, word2, word3] and nothing else. Do not include any explanations or additional text.")
    word_list = gemini_response.text.strip('[]').split(',')

    combinedWords = ''.join(word_list)
    label2.config(text=f"Your words are: {combinedWords}")

def generate_password():
    global password
    password = ""

    website_name = txt2.get()

    for char in website_name:
        if char in combinedWords:
            index = combinedWords.index(char)
            next_char = combinedWords[index + 1]
            password += next_char
        else:
            password += "X"

    character_substitutions = {
        "e": "3",
        "o": "0",
        "g": "9",
        "i": "!",
        "a": "@",
        "s": "$",
    }
    new_password = ""
    for char in password:
        new_password += character_substitutions.get(char, char)

    label3.config(text=f"Here is your new password: {new_password}")

btn1 = Button(root, text="Generate Words", command=generate_words)
btn1.grid(column=2, row=2)

label3 = Label(root, text="What is the name of the website you need a password for?")
label3.grid(column=0, row=4)

txt2 = Entry(root)
txt2.grid(column=1, row=4)

btn2 = Button(root, text="Generate Password", command=generate_password)
btn2.grid(column=3, row=4)

root.mainloop()