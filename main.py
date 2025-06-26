import streamlit as st #importing the required lib
import textdistance
import os
from st_clickable_images import clickable_images
from st_keyup import st_keyup

#---------------------------Config page----------------------------------#
st.set_page_config(
    page_title="ICODEV | Get Most of the programming Icons",
    page_icon="https://d17azs2fqvxy2n.cloudfront.net/icon2.0/icodev.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)
#--------------------------------------------------------------------#



#-------------CSS---------------------#


css_para = """
<style>
    .styled-paragraph {
        font-family: Arial, sans-serif;
        font-size: medium;
        line-height: 1.5;
        color: #333;
        padding: 20px;
        background-color: #f7f7f7;
        border-radius: 25px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>
"""

st.markdown(css_para, unsafe_allow_html=True)


css_footer = """
<style>
    .st-emotion-cache-1racx89 h6 {
        padding: 0.5rem !important;
    }

    .footer {
        text-align: center;
        font-size: 12px;
        color: black !important;
        padding: 10px;
        background-color: #f9f9f9;
        border-top: 0.5px solid #ddd;
        bottom: 0;
        width: 100%;
    }
</style>
"""

st.markdown(css_footer, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Custom CSS styles for the search input */
    #label {
        content=''
        font-size: larger; /* Set font size */
        color: grey; /* Set text color */
        position: absolute; 
        top: 35%;
        z-index:12;
        font-weight: bold;
        opacity:0.7;
    }
</style>

""", unsafe_allow_html=True)
#----------------------------------------------------------------




#---------------------------Hide Header & Footer----------------------------#
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
#--------------------------------------------------------------------#




#---------------------------Solution------------------------#


#Tile of the webpage
st.caption("<h1 style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -120%) ;'><img src='https://d17azs2fqvxy2n.cloudfront.net/icon2.0/icodev.svg' alt='ICODEV' style='height: 40px;'> ICODEV</h1>", unsafe_allow_html=True)


# Define the folder path
folder_path = "icon2.0"


#caching the data to get it asap
@st.cache_data
def fetch_image_data(folder_path):
    # Initialize empty lists to store image URLs and titles
    image_urls = []
    image_titles = []
    
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is an SVG file
            if filename.endswith(".svg"):
                # Extract the file name without extension
                file_name = os.path.splitext(filename)[0]
                # Construct the URL using the file name
                url = f"https://d17azs2fqvxy2n.cloudfront.net/icon2.0/{file_name}.svg"
                # Append the URL to the list of image URLs
                image_urls.append(url)
                # Append the file name (without extension and '-original') to the list of titles
                image_titles.append(file_name.replace("-original", "").upper())
    else:
        st.error(f"The folder '{folder_path}' does not exist or is not accessible.")
    
    # Sort the image titles
    image_titles.sort()
    image_urls.sort()
    
    return image_urls, image_titles

# Fetch image URLs and titles
image_urls, image_titles = fetch_image_data(folder_path)

# Function to perform auto-correction
def auto_correct(input_text):
    # Calculate Levenshtein distance between input text and image titles
    distances = [(title, textdistance.levenshtein.normalized_distance(input_text.lower(), title.lower())) for title in image_titles]
    # Sort by distance and get the closest title
    closest_title = min(distances, key=lambda x: x[1])[0]
    return closest_title





# selected = st.text_input("Search For Icon", key="my_input", placeholder="Python", autocomplete="on", help="Enter the name of the icon you're looking for.",args=None)

# Search bar with custom title
st.markdown('<label id="label" for="text_input">Search For Icon</label>', unsafe_allow_html=True)
selected = st_keyup("", key="0",placeholder="Python") #this will help us to filter in real time 

# Filter images based on search query
filtered_image_urls = [url for title, url in zip(image_titles, image_urls) if selected.lower() in title.lower()]
filtered_image_titles = [title for title in image_titles if selected.lower() in title.lower()]


# Display total results with some custom css
number_of_results = len(filtered_image_titles)
if number_of_results == 0:
    st.write(f'<span style="color:red;opacity:0.9;font-size:smaller"> No Result Found  </span>', unsafe_allow_html=True) #none will be shown in red 
else:
    st.write(f'<span style="color:green;opacity:0.9;font-size:smaller">Total Result : {number_of_results}</span>', unsafe_allow_html=True) #result will be shown in green



#suggestion based on the file name will be given 
if selected:
    corrected_text = auto_correct(selected)
    if corrected_text.lower() != selected.lower():
        # Add event handler to the suggested correction
        st.caption(f"Do you mean: {corrected_text} ?")



# Display clickable images
clicked_image_index = clickable_images(
    filtered_image_urls,
    titles=filtered_image_titles,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "50px", "height": "200px"},
)

#Footer for the main page 
st.divider()
st.markdown("<h6  class='footer'>All Right Reserved</h6>", unsafe_allow_html=True)
        

# Map the index to the filtered list
if clicked_image_index > -1:
    original_index = [i for i, url in enumerate(image_urls) if url == filtered_image_urls[clicked_image_index]][0]
    selected_image_url = image_urls[original_index]
    selected_image_title = image_titles[original_index]


    # Sidebar for additional information
    with st.sidebar:
        st.markdown("<h1 style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -110%); font-size: medium ;'>Development Icon</h1>", unsafe_allow_html=True)

        st.markdown("<p class='styled-paragraph'>IcoDev is a small project but yet very useful project which will help us to get the set of icons representing programming languages, designing, and development tools. You can directly add the icons to your project without any delay.</p>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='position: absolute; top: 50%; left: 50%; transform: translate(-192%, 40%); font-size: smaller ;'>SVG versions</h5>", unsafe_allow_html=True)
        
        st.divider()
        
        # Display clicked image and its title
        st.markdown(f"<div style='position: relative; display: flex; flex-direction: column; justify-content: center; align-items: center;'> <img src='{selected_image_url}' width='150'> <br> <br>  <h6 style='text-align: center; color: grey; font-size: smaller;'>{selected_image_title}</h6> </div>", unsafe_allow_html=True)
        
        # Display the HTML string
        check = st.code(f" '{selected_image_url}' ", language='python')
         # Show toast message
         

        st.divider()
        
        st.markdown("<p class='styled-paragraph' style='text-align:center'>Originally created by Firoz  <br> Copyright © 2024 Firoz</p>", unsafe_allow_html=True)
        
        
        
        
#Project Created by Firoz Shaikh
#Date : 2024-04-28
#Hours Spent on Project : 3 Hours

#Project Motive Description
# - > IcoDev is simple project but yet very much useful project in this we have store the images cdn so in that way anyone 
# without downloading can easily get the icons we have more then 400+ icons with us 


#Front-end 
# Streamlit , Html , css , aws

#Back-End
# Python , Streamlit 