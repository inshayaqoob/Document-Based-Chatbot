import streamlit as st
import chat

# Creating the chatbot interface
st.title("LLM-Powered Chatbot for Intelligent Conversations")
st.subheader("AVA-Abonia Virtual Assistant")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Define a function to clear the input text
def clear_input_text():
    global input_text
    input_text = ""

# We will get the user's input by calling the get_text function
def get_text():
    global input_text
    input_text = st.text_input("Ask your Question", key="input", on_change=clear_input_text)
    return input_text

def main():
    user_input = get_text()

    if user_input:
        output = chat.answer(user_input)
        # store the output
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            st.write("Bot: ", st.session_state["generated"][i])  # Display the bot's response
            st.write("You: ", st.session_state['past'][i])  # Display the user's input

# Run the
if __name__ == "__main__":
    main()
