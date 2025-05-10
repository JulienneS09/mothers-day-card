import streamlit as st

# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="For Mama 💌", layout="centered")

# # ---- PASSWORD PROTECTION ----
# if "access_granted" not in st.session_state:
#     st.session_state.access_granted = False

# if not st.session_state.access_granted:
#     st.title("🌸 Mother's Day Surprise 🌸")
#     pw = st.text_input("Enter the secret password:", type="password")
#     if pw == "christine":
#         st.session_state.access_granted = True
#         st.experimental_rerun()  # Safe to rerun AFTER setting session state
#     else:
#         st.stop()  # Halt the app if password is incorrect

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
    "To CC",
    "Just a little more...",
    "Here's a flower, and something written just for you",
    "From your eldest badlongon XD",
    "From your eldest badlongon part 2",
    "From not-so-pretty daughter nyehe",
    "From you prettiest daughter!",
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

# Track current step
if "step" not in st.session_state:
    st.session_state.step = 0

current = st.session_state.step
st.image(image_urls[current], use_column_width=True, caption=captions[current])

# Advance button
if current < len(image_urls) - 1:
    if st.button("👉 Tap to read your letter"):
        st.session_state.step += 1
        st.experimental_rerun()
else:
    st.success("🎉 That's the end! Happy Mother's Day, Ma! 🌼")
