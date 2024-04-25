import chainlit as cl

@cl.on_chat_start
def on_chat_start():
    cl.send_message("Hello! I'm Chainlit. I can help you with your daily tasks. What would you like me to do?")

@cl.on_message
def on_message(message):
    if message == "What can you do?":
        cl.send_message("I can help you with your daily tasks. Just tell me what you need help with.")
    else:
        cl.send_message("I'm sorry, I don't understand that command. Please try again.")