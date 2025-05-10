import streamlit as st

# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="For Mama 💌", layout="centered")

# ---- IMAGE SEQUENCE ----
st.title("💌 For You, Mama")

image_urls = [
    "https://i.imgur.com/MTZv4pb.png",      # Closed envelope
    "https://i.imgur.com/Wyxtjp1.png",      # Opening envelope
    "https://i.imgur.com/dOFkFmB.png",      # Blank paper + flower
    "https://i.imgur.com/vpFoaoj.png",      # Gerard
    "https://i.imgur.com/iRH8yI4.png",      # Raymund
    "https://i.imgur.com/nsZwFKZ.png",      # Johanna
    "https://i.imgur.com/z4vkfSp.png",      # Julienne
    "https://i.imgur.com/g65uWTh.png",      # Ge-an
    "https://i.imgur.com/Hg67jyR.png",      # Yohann
    "https://i.imgur.com/ozTiqe3.png",      # Trixia
    "https://i.imgur.com/NyaaJl0.png",      # Rafael
    "https://i.imgur.com/L2q9iu6.png",      # Elyana
    "https://i.imgur.com/s9ZwdsN.png",      # Kane
    "https://i.imgur.com/3Coqw0N.png",      # Kyros
    "https://i.imgur.com/z9hulyU.png",      # Karen
    "https://i.imgur.com/MI0vD2Q.png"       # Final
]

captions = [
    "Just a little more...",
    "Here's a flower, and something written just for you",
    "From your eldest badlongon XD",
    "From your eldest badlongon part 2",
    "From not-so-pretty daughter nyehe",
    "From your prettiest daughter!",
    "Eldest Sopiya",
    "Kuya Yohann",
    "Ate Trixia",
    "Pael",
    "Yanabanana",
    "Kuya Kane",
    "Kyros",
    "Karen",
    "We love you, Mama and Lola!!! 🌺"
]

# ---- STEP TRACKER ----
if "step" not in st.session_state:
    st.session_state.step = 0

current = st.session_state.step

# ---- DISPLAY IMAGE AS A CLICKABLE ELEMENT ----
st.markdown(
    f"""
    <a href="?step={current + 1}">
        <img src="{image_urls[current]}" style="width:100%; border-radius:15px;" alt="letter image"/>
    </a>
    <p style="text-align:center;"><em>{captions[current]}</em></p>
    """,
    unsafe_allow_html=True
)

# ---- HANDLE STEP INCREMENT FROM URL PARAM ----
query_params = st.experimental_get_query_params()
if "step" in query_params:
    next_step = int(query_params["step"][0])
    if next_step < len(image_urls):
        st.session_state.step = next_step
        st.experimental_set_query_params()  # clear URL
        st.experimental_rerun()

# ---- FINAL MESSAGE ----
if current == len(image_urls) - 1:
    st.success("🎉 That's the end! Happy Mother's Day, Ma! 🌼")
