import streamlit as st
from PIL import Image
from io import BytesIO
from rembg import remove

st.set_page_config(page_title='Image background eraser')

def erase(original):      
    # st.write('Background removed')
    image = remove(original)
    col2.image(image,caption="Edited Image")
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()

    col2.download_button(
        label="Download Image",
        data=image_bytes,
        file_name="edited_image.png",
        use_container_width=True,
        mime="image/png"
    )

###LAYOUT###
st.markdown(
    f"""
    <h1 style='text-align: center'>Image Background Remover</h1>
    """,
    unsafe_allow_html=True
)
st.title('')
st.title('')
st.title('')

st.sidebar.write("### Erase the background of any image. \n\n"
                 "### ✔️ *Easy* \n\n"
                 "### ✔️ *Free*\n\n"
                 "### ✔️ *No registration*\n\n"
                 "### ✔️ *Any resolution*\n\n"
                 "### Just... ")
# file upload and action button
my_upload = st.sidebar.file_uploader("upload file", 
                            type=["png", "jpg", "jpeg"],
                            help="Just upload an image and click 'Remove'.",
                            label_visibility='collapsed')

st.sidebar.title('')
credits = st.sidebar.checkbox('Credits & Info')
if credits:
    sm1 = "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shopovgeorgi/)"
    sm2 = "[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/shopovgeorgii)"

    st.sidebar.write('# **Georgi Shopov**\n\n',sm1,sm2)
    st.sidebar.image('default.png')
    sm3 = "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/datascigonewild)"
    sm4 = "[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/datascigonewild)"
    st.sidebar.write(sm3,sm4)

if my_upload is None:
    st.write("#### What if I told you it takes a *click*?")

col1,col2= st.columns(2)
with col1:
    if my_upload is not None:
        # st.write('Original image')
        original = Image.open(my_upload)
        st.image(original, caption='Original image')
        action_button = st.button('Remove', 
                        type='primary',
                        use_container_width=True,)

        if action_button:
            erase(original)
    else:
        col1.image(Image.open("whatifitoldyou.jpg"), caption='Original image')
        
        erase(Image.open("whatifitoldyou.jpg"))
