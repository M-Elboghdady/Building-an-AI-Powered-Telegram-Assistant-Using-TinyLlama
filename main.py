import torch
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the TinyLlama model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Hello! I am your AI assistant powered by TinyLlama. Ask me anything!"
    )
# Function to handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    print(f"Received message: {user_message}")

    # Encode the user input and generate a response from the LLM
    input_ids = tokenizer.encode(user_message, return_tensors="pt").to(device)
    output_ids = model.generate(input_ids, max_length=200, num_return_sequences=1)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print(f"Response generated: {response}")
    await update.message.reply_text(response)
# Main function to run the bot
def main():
    # Replace with your actual bot token
    bot_token = "7924120373:AAGI-0x7qxy00cBocCifibfMVOtAmJGkqIY"
    # Initialize the application
    application = ApplicationBuilder().token(bot_token).build()
    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    # Start the bot
    print("MyAssistentBot is running... Press Ctrl+C to stop.")
    application.run_polling()
if __name__ == "__main__":
    main()
