# **MyAssistentBot: An AI-Powered Telegram Assistant**

## **Overview**
MyAssistentBot is an AI-powered chatbot built using the Telegram Bot API and the TinyLlama-1.1B-Chat-v1.0 language model. This bot processes user messages, generates intelligent responses, and provides real-time conversational interaction.

## **Features**
- Natural language understanding powered by the TinyLlama LLM.
- Handles conversational tasks and user queries through Telegram.
- Lightweight and efficient model suitable for local CPU-based inference (with optional GPU optimization).

---

## **Project Workflow**

### **Step 1: Bot Setup**
1. Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather).
2. Configure the bot token and set up message handling using Python's `python-telegram-bot` library.

### **Step 2: Model Integration**
1. Load the **TinyLlama-1.1B-Chat-v1.0** model from [Hugging Face](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0).
2. Use the model to process incoming messages from the bot and generate responses.

### **Step 3: Interaction Flow**
1. A user sends a message (e.g., "Tell me about dogs") to the bot.
2. The bot forwards the message to the locally hosted TinyLlama model for processing.
3. TinyLlama generates a response based on the input.
4. The bot sends the response back to the user in the Telegram chat.

---

## **Tools and Technologies**
- **Programming Language**: Python
- **Libraries**: 
  - `python-telegram-bot` for bot handling
  - `transformers` for LLM integration
  - `torch` for inference backend
- **Model**: [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- **Platform**: Telegram Messenger

