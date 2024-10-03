#%%
import streamlit as st

st.title('With Love for Andrea')
st.write('This is a simple web app to show you how much I love you.')
st.write('I hope you like it.')
st.write('I love you so much.')
st.write('I miss you so much.')
st.write('I hope you are doing well.')

# Add an image to the web app
# from PIL import Image
# image = Image.open('heart.jpg')
# st.image(image, caption='I love you')

# Dispaly a video on the web app replaying from YouTube
video_file = open('hamster.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# host this web app on a url that I can share with my girlfriend
st.write('You can access this web app at the following URL:')
st.write('https://share.streamlit.io/andrea-rosa/with-love-for-andrea/main/streamlit.py')



# Display a text box to enter a custom message
user_input = st.text_input('How are you:')
# Display the customized message
st.write('Customized Message:', user_input)