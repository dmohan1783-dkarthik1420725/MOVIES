import streamlit as st
import time

# --- CONFIG & THEME ---
st.set_page_config(page_title="Pandaga Chesko - Full Movie", page_icon="🎬", layout="wide")

# Custom CSS for the Cinematic Experience
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stButton>button { 
        background-color: #ff4b4b; color: white; font-size: 24px; 
        height: 3em; width: 100%; border-radius: 10px; font-weight: bold;
    }
    .movie-title { text-align: center; color: #ffd700; font-family: 'Impact'; font-size: 60px; text-shadow: 2px 2px #ff0000; }
    .script-body { max-width: 800px; margin: auto; font-size: 18px; line-height: 1.6; }
    .hero { color: #00d4ff; font-weight: bold; }
    .villain { color: #ff4e4e; font-weight: bold; }
    .bgm { color: #ffd700; font-style: italic; font-size: 0.9em; display: block; margin: 10px 0; }
    .action { color: #aaaaaa; font-style: italic; }
    .footer { text-align: center; margin-top: 50px; padding: 20px; color: #555; font-size: 0.9em; border-top: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE FOR THE START BUTTON ---
if 'movie_started' not in st.session_state:
    st.session_state.movie_started = False

# --- FRONT PAGE (Before Start) ---
if not st.session_state.movie_started:
    st.markdown("<h1 class='movie-title'>PANDAGA CHESKO... PARIGETTAKU!</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_container_width=True)
    st.write("### 🍿 Ready for the Full 2.5 Hour Experience?")
    st.write("**Cast:** Prasad, Bujji, Bullet Babji, and Peddayya")
    st.write("**Director:** Gemini AI | **Production:** Mana Script Production")
    
    if st.button("🎬 START MOVIE DIRECTLY"):
        with st.spinner('Projector Starting... Loading Reels...'):
            time.sleep(2)
            st.session_state.movie_started = True
            st.rerun()

# --- THE WHOLE MOVIE (After Start) ---
else:
    st.markdown("<h1 class='movie-title'>NOW PLAYING</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='script-body'>", unsafe_allow_html=True)
        
        # ACT 1
        st.subheader("🏮 ACT 1: THE CHAOS BEGINS")
        st.markdown("<span class='bgm'>🎵 [Vibrant Village Music Starts] 🎵</span>", unsafe_allow_html=True)
        st.markdown("<p class='action'>The camera zooms into a busy wedding house. People are running around.</p>", unsafe_allow_html=True)
        st.write("**SREENU:** Prasad-u! Pellikoduku jump ra! Mana paruvu Bazaru palu avthundi!")
        st.markdown("<p class='hero'>PRASAD: Rey Sreenu, calm ga undu. Pellikoduku jump ithe substitute ni petteddam. Inthaki nenu unna ga! Makeup veyi, pelli kaniyi!</p>", unsafe_allow_html=True)
        st.write("**SREENU:** Arrey, idi emaina cricket match anukunnav-a? Substitute fielders undaniki?")
        st.markdown("<p class='hero'>PRASAD: Logic lu vaddu... Magic chudu! Ee pelli jaruguthundi, anthe!</p>", unsafe_allow_html=True)
        
        st.divider()

        # ACT 2
        st.subheader("🏠 ACT 2: THE ANCESTRAL TRAP")
        st.markdown("<span class='bgm'>🎵 [Emotional Veena BGM] 🎵</span>", unsafe_allow_html=True)
        st.write("**PEDDAYYA:** Ee illu ammi dobbutha. Evaru chuskunoru leru ikkada.")
        st.markdown("<p class='hero'>PRASAD: Thatha! Aguu! Mana chuttalalo okadu America lo Billionaire ayyadu. Aayana Sankranti ki vasthunnadu. Mana illu bangaram chesthadu!</p>", unsafe_allow_html=True)
        st.write("**PEDDAYYA:** Billionaire-a? Ma nannaki cycle koda lede?")
        st.markdown("<p class='hero'>PRASAD (Aside): Cycle lekapothe emi thatha, ippudu Boeing flight lo vasthunnadu! (To Sreenu) Rey, aa drama batch ki kotha battalu koni teeskura, Billionaires la kanipinchali!</p>", unsafe_allow_html=True)
        
        st.divider()

        # ACT 3 - INTERVAL BLOCK
        st.subheader("💥 ACT 3: THE INTERVAL BANG")
        st.markdown("<span class='bgm'>🎵 [Intense Bass & Electric Guitar] 🎵</span>", unsafe_allow_html=True)
        st.markdown("<p class='villain'>BULLET BABJI: Rey! Naa peru Bullet Babji! Ee land naa sontham. Ee fake billionaire evadu madhyalo?</p>", unsafe_allow_html=True)
        st.markdown("<p class='hero'>PRASAD: Babji! Trigger nokkithe sound vasthadi... kaani nenu scene loki vasthe 'Sound-u, Sandadi' rendu untayi!</p>", unsafe_allow_html=True)
        st.markdown("<p class='action'>Suddenly, a real Mafia SUV crashes the gate. The REAL DON steps out.</p>", unsafe_allow_html=True)
        st.markdown("<p class='villain'>REAL DON: Where is the money? Who is using my name?</p>", unsafe_allow_html=True)
        st.markdown("<p class='hero'>PRASAD: (Looking at camera) Thatha... veedu 'Special Guest'. Mana life lo Intermission icche guest! **INTERVAL!**</p>", unsafe_allow_html=True)
        
        st.divider()

        # ACT 4 - CLIMAX
        st.subheader("🪁 ACT 4: THE GRAND SANKRANTI CLIMAX")
        st.markdown("<span class='bgm'>🎵 [Heavy Folk Teenmaar Beat Begins] 🎵</span>", unsafe_allow_html=True)
        st.markdown("<p class='action'>Kites are flying everywhere. Prasad stands on the roof with a thread spool (Manja).</p>", unsafe_allow_html=True)
        st.markdown("<p class='hero'>PRASAD: Sankranti ante dummulu dhulapadam kaadu ra... mee lanti dhoola unna gallani dhulapadam! Peddayya illu joliki vasthe, narakam chustharu!</p>", unsafe_allow_html=True)
        st.markdown("<p class='villain'>BULLET BABJI: Baboi! Veedu hero laaga matladuthunnadu enti? Parigettandi!</p>", unsafe_allow_html=True)
        st.markdown("<p class='hero'>PRASAD: Parigettaku Babji... Pandaga chesko! (Hits Babji with a flying kite)</p>", unsafe_allow_html=True)
        st.write("**PEDDAYYA:** Prasad-u! Nuvvu ma vamsam ki nijamaina varasudu ra! Happy Sankranti!")
        
        st.markdown("<span class='bgm'>🎵 [All family members dance together - End Credits Roll] 🎵</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Celebration Effect
        st.balloons()
        
    # --- FOOTER ---
    st.markdown("<div class='footer'>(2026 Mana script production)</div>", unsafe_allow_html=True)

    if st.button("⏪ REWATCH FROM START"):
        st.session_state.movie_started = False
        st.rerun()
