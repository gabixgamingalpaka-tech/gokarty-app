import streamlit as st
import requests
import datetime
import random

st.set_page_config(page_title="Gokarty?", page_icon="🏎️", layout="centered")

# TWÓJ ID Z FORMSPREE
FORMSPREE_ID = "xljelqql"

if "accepted" not in st.session_state:
    st.session_state.accepted = False

st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    div[data-testid="stElementToolbar"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# EKRAN 1: Pytanie wstępne
if not st.session_state.accepted:
    st.markdown("<h1 class='main-title'>🏎️ Idziemy na gokarty?</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("TAK! 🎉", use_container_width=True, type="primary"):
            st.session_state.accepted = True
            st.rerun()
            
    with col2:
        margin_top = random.randint(-50, 150)
        margin_left = random.randint(-80, 80)
        
        st.markdown(f"<div style='margin-top: {margin_top}px; margin-left: {margin_left}px;'>", unsafe_allow_html=True)
        if st.button("Nie 😜", key="no_btn", use_container_width=True):
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# EKRAN 2: Wybór terminu na S8Race
else:
    st.title("🏁 Wybierz termin jazdy")
    
    with st.form("karting_form"):
        name = st.text_input("Twoje Imię")
        
        track = st.selectbox(
            "Wybrany tor gokartowy",
            ["S8Race"]
        )
        
        selected_date = st.date_input("Wybierz dzień", min_value=datetime.date.today())
        selected_time = st.time_input("Wybierz godzinę", value=datetime.time(17, 0))
        
        message = st.text_area("Komentarz / Wiadomość (opcjonalnie)")
        
        submit_button = st.form_submit_button("Rezerwuj termin 🚀")

    if submit_button:
        if not name:
            st.error("Proszę podać imię!")
        else:
            data = {
                "Imię": name,
                "Wybrany Tor": track,
                "Data": str(selected_date),
                "Godzina": str(selected_time),
                "Wiadomość": message
            }
            
            url = f"https://formspree.io/f/{FORMSPREE_ID}"
            response = requests.post(url, data=data)
            
            if response.status_code == 200:
                st.balloons()
                st.success("zabierz mnie do gwiazd, ten kolejny raz ⭐🎵")
            else:
                st.error("Wystąpił błąd podczas wysyłania.")