import streamlit as st

# Sample data for image titles and URLs
image_titles = ["Python Logo", "JavaScript Icon", "HTML Logo", "CSS Icon"]
image_urls = [
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",
    "https://www.w3.org/html/logo/downloads/HTML5_1Color_Black.png",
    "https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg"
]

# Function to filter images based on search query
def filter_images(search_query):
    return [url for title, url in zip(image_titles, image_urls) if search_query.lower() in title.lower()]

# Display search bar for filtering icons
selected = st.text_input("Search For Icon")

# Filter images and display in real-time
if selected:
    filtered_image_urls = filter_images(selected)
    number_of_results = len(filtered_image_urls)
    if number_of_results == 0:
        st.write(f'<span style="color:red;opacity:0.9;font-size:smaller"> No Result Found  </span>', unsafe_allow_html=True)
    else:
        st.write(f'<span style="color:green;opacity:0.9;font-size:smaller">Total Result : {number_of_results}</span>', unsafe_allow_html=True)
    for url in filtered_image_urls:
        st.image(url, caption='Filtered Image')

# The rest of your code...

# Display the footer
st.divider()
st.markdown("<h6 class='footer'>All Rights Reserved</h6>", unsafe_allow_html=True)
