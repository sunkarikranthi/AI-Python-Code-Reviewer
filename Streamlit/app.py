import streamlit as st
from openai import OpenAI


# Setting up OpenAI and key
f = open('.openai_api_key.txt')
OPENAI_KEY = f.read()
client = OpenAI(api_key=OPENAI_KEY)

# title for the app
st.header("An :blue[AI] Python Code Reviewer ⌨️")
# Defining User and System Prompt
user_prompt = st.text_area('Enter your python code here :')
system_prompt = '''
                    you are an intelligent python code reviewer.
                    you must verify the code and if it incorrect show the errors in the code to the user and provide the correct code.
                   '''

# Generating response on button click

if st.button("Review") == True:
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role':'system', 'content': system_prompt,
                'role':'user', 'content':user_prompt
            }
        ],
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    st.write(response.choices[0].message.content)