import tkinter as tk
from tkinter import scrolledtext
import requests
import json

class CatGPT:
    def __init__(self, root, api_key):
        self.root = root
        self.root.title("CatGPT 1.0X")
        self.root.geometry("800x600")
        self.root.config(bg="#2c3e50")

        self.intro_message = "Welcome to CatGPT 1.0X, your AI assistant."

        self.chat_window = scrolledtext.ScrolledText(self.root, width=100, height=20, bg="#ecf0f1")
        self.chat_window.pack(padx=10, pady=10)
        self.chat_window.insert(tk.END, "CatGPT: " + self.intro_message + "\n")
        self.chat_window.see(tk.END)

        self.input_field = tk.Text(self.root, width=90, height=2, bg="#ecf0f1")
        self.input_field.pack(padx=10, pady=10)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_command, bg="#1abc9c", fg="#ffffff")
        self.send_button.pack(pady=5)

        self.api_key = api_key
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"

    def send_request(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "meta-llama/llama-4-maverick",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return "Failed to retrieve response"

    def send_command(self):
        command = self.input_field.get("1.0", "end-1c")
        self.chat_window.insert(tk.END, "You: " + command + "\n")
        response = self.send_request(command)
        self.chat_window.insert(tk.END, "CatGPT: " + response + "\n")
        self.chat_window.see(tk.END)
        self.input_field.delete("1.0", tk.END)

if __name__ == "__main__":
    api_key = ""  # replace with your OpenRouter API key
    root = tk.Tk()
    catgpt = CatGPT(root, api_key)
    root.mainloop()
