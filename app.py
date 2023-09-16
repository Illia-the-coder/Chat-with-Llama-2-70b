import streamlit as st
from gradio_client import Client

# Constants
TITLE = "Llama2 70B Chatbot"
DESCRIPTION = """
This Space demonstrates model [Llama-2-70b-chat-hf](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) by Meta, 
a Llama 2 model with 70B parameters fine-tuned for chat instructions. 
"""

# Initialize client
client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")

# Prediction function
def predict(message, system_prompt="", temperature=0.9, max_new_tokens=4096):
    return client.predict(
			message,	# str in 'Message' Textbox component
            system_prompt,	# str in 'Optional system prompt' Textbox component
			temperature,	# int | float (numeric value between 0.0 and 1.0)
			max_new_tokens,	# int | float (numeric value between 0 and 4096)
			0.3,	# int | float (numeric value between 0.0 and 1)
			1,	# int | float (numeric value between 1.0 and 2.0)
			api_name="/chat"
    )

# Streamlit UI
st.title(TITLE)
st.write(DESCRIPTION)

# Input fields
message = st.text_area("Enter your message:", "")
system_prompt = st.text_area("Optional system prompt:", "")
temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.9, step=0.05)
max_new_tokens = st.slider("Max new tokens", min_value=0, max_value=4096, value=4096, step=64)

if st.button("Predict"):
    response = predict(message, system_prompt, temperature, max_new_tokens)
    st.write("Response:", response)

