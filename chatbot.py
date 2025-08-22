import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDPlyW78iu7DYEtWgKBpwcmOV-oK6vxVxs")

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Function to handle the chatbot logic
def chatbot_response(user_input):
    if user_input.lower() == "quit":
        return "Exiting chatbot. Goodbye!"
    parameters = {"generation_config": {"temperature": 0.7}}
    response = model.generate_content(user_input, **parameters)
    return response.text.replace('', '').replace('*', '')

# Function to send and display chat messages
def send_message():
    user_input = user_entry.get()
    if user_input.strip():  # Check if user input is not empty
        chat_history.insert(tk.END, f"You: {user_input}\n")
        response = chatbot_response(user_input)
        chat_history.insert(tk.END, f"Bot: {response}\n\n")
        user_entry.delete(0, tk.END)  # Clear the input box

        if user_input.lower() == "quit":  # Close the chatbot if user types "quit"
            messagebox.showinfo("Chatbot", "Exiting chatbot. Goodbye!")
            root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Chatbot with Pop-up Window")
root.geometry("500x600")  # Size of the pop-up window

# Chat History Display
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, font=("Arial", 12))
chat_history.pack(padx=10, pady=10)

# User Input
user_entry = tk.Entry(root, width=45, font=("Arial", 12))
user_entry.pack(pady=5, side=tk.LEFT, padx=(10, 0))

# Send Button
send_button = tk.Button(root, text="Send", width=10, font=("Arial", 12), command=send_message)

send_button.pack(pady=5, side=tk.RIGHT, padx=(0, 10))

# Start the GUI Event Loop
root.mainloop()