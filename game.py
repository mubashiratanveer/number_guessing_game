import streamlit as st
import random
import time


st.set_page_config(page_title="Guessing Game", layout="wide", page_icon="🎯")

# Custom CSS 
st.markdown(
    """
    <style>
    .main {
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #008CBA; /* Updated color */
        color: white;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #005f73;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        text-align: center;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize Session Variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.message = ""
    

# UI Layout 
st.markdown("<div style='display: center; justify-content: center; text-align: center;'>", unsafe_allow_html=True)
st.title("🎯 Number Guessing Game")
st.subheader("Guess a number between 1 and 10")

# Input Number in the Middle
guess = st.number_input("Enter your guess", min_value=1, max_value=10, step=1)

# Function to Check the Guess
def check_guess():
    if st.session_state.game_over:
        return
    st.session_state.attempts -= 1
    if guess == st.session_state.secret_number:
        st.session_state.message = "🎉 Congratulations! You Win!"
        st.session_state.game_over = True 
        # 🎈 Balloon Animation
        time.sleep(0.3)  # Short delay for smooth effect
        st.balloons()
    elif st.session_state.attempts == 0:
        st.session_state.message = f"😢 Game Over! The correct number was {st.session_state.secret_number}."
        st.session_state.game_over = True
    else:
        st.session_state.message = f"❌ Wrong guess! You have {st.session_state.attempts} chances left."

# Reset Function
def reset_game():
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.message = ""

    
st.button("Check guess",on_click=check_guess)
st.write(f"{st.session_state.message}")
st.button("Reset game",on_click=reset_game)

st.markdown("</div>", unsafe_allow_html=True)