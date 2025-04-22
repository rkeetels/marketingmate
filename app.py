import openai
import streamlit as st

# Zet hier je OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else ""

st.title("\ud83c\udf1f MarketingMate - Jouw AI Marketing Assistent")

# Vraag input van gebruiker
st.header("Geef MarketingMate een opdracht")
user_goal = st.text_area("Wat wil je dat MarketingMate voor je uitwerkt?", placeholder="Bijvoorbeeld: Maak een gratis weggever over belastingtips voor ondernemers.")

# Extra parameters
tone = st.selectbox("Welke schrijfstijl wil je?", ["Professioneel", "Creatief", "Persoonlijk", "Direct"])
output_type = st.selectbox("Wat wil je ontvangen?", ["Gratis weggever", "E-mailreeks", "Podcast onderwerpen", "Social media posts"])

if st.button("Start Genereren"):
    if not user_goal.strip():
        st.error("Voer eerst een opdracht in!")
    else:
        with st.spinner("MarketingMate is bezig..."):
            prompt = f"""
Je bent een creatieve maar feitelijke marketingstrateeg gespecialiseerd in financieel advies.

Doel: {user_goal}

Output type: {output_type}
Schrijfstijl: {tone}

Werk zelfstandig een compleet concept uit, inclusief suggesties voor inhoud en structuur. Denk stap voor stap en reflecteer kort waarom je keuzes maakt.
"""
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Je bent MarketingMate, een expert in marketingcreatie voor financiële diensten."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                
                output = response['choices'][0]['message']['content']
                st.success("Hier is jouw uitgewerkte concept!")
                st.write(output)
                
            except Exception as e:
                st.error(f"Er ging iets mis: {e}")

# Tip voor gebruik
st.sidebar.header("Tips:")
st.sidebar.markdown("- Wees specifiek in je opdracht\n- Vraag eventueel om meerdere varianten\n- Combineer opdrachten voor nog betere concepten!")
