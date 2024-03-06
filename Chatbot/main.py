import tkinter as tk
from tkinter import PhotoImage
from chatbot import ChatBot


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        self.master.geometry("1152x648")

        self.myChatBot = ChatBot()

        #self.myChatBot.loadModel()

        #criar o modelo
        self.myChatBot.createModel()


        self.background_image = PhotoImage(file='img.gif')

        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.chat_history = tk.Text(self.master, wrap=tk.WORD, width=50, height=20,borderwidth=0,bg='#FFFFFF')
        self.chat_history.place(x=65, y=80)

        self.input_entry = tk.Text(self.master, width=42, height=2,borderwidth=0,)
        self.input_entry.place(x=65, y=487)

        self.send_button = tk.Button(self.master, text="Enviar",height=3, command=self.send_message)
        self.send_button.place(x=455, y=480)
        self.display_message("como posso te ajudar?")

    def send_message(self):
        user_input = self.input_entry.get("1.0", tk.END)
        self.display_message(f"Você: {user_input}")

        resposta, intencao = self.myChatBot.chatbot_response(user_input)
        bot_response = resposta
        self.display_message(f"Bot: {bot_response}")

        

    def display_message(self, message):
        self.chat_history.insert(tk.END, f"{message}\n")
        self.input_entry.delete("1.0", tk.END)


def main():
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()

main()