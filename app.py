import streamlit as st
from datetime import datetime
import os
import json

class Blogs:
    def __init__(self, file_path = 'blog_entries.json'):
        self.file_path = file_path

    def get_blogs(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                return data
            except Exception as e:
                return f"Error reading file: {str(e)}"
        else:
            return "Blog file not found"



st.set_page_config(page_title="Kevin Otieno | Built from Scarcity", layout="wide")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Blog","Contact Me"])

if page == "Home":
    st.markdown("# 👋 Welcome")
    st.markdown("## Survival is Sacred. Systems are Sovereign.")
    st.image('new.jpg', width=650)
    st.write("""
    I'm **Kevin Otieno**, a behavioral architect based in Nairobi. I design dashboards, nudging engines, 
             and legacy system.

    I specialize in turning raw data into clarity, building systems that help SMEs, hospitals, and individuals make decisions with rhythm—not noise.

    This is a living archive of systems built from pain, designed for traction, and anchored in legacy.
             
    ###### *“Built from Nairobi, where survival isn’t theory—it’s daily practice.”*
    """)

    st.markdown("### 🔁 Latest Lever")
    st.write("Cold pitch sent to Nairobi SME. Proposed dashboard: KES 12,000/month. Waiting on reply.")

    st.markdown("### 💼 What I Offer")
    st.markdown("- SME Dashboards — modular, priced for reality, built for traction ")
    st.markdown("- Hospital Nudging Systems — daily loops, backend clarity, decision triggers ")
    st.markdown("- Behavioral Engines — systems that nudge action from minimal data ")

    st.markdown("### Why Me")
    st.markdown("I don’t design from theory. I design from survival. Every system I build is tested in scarcity, refined in rhythm, and anchored in legacy")
     


    st.markdown("## 🛠 Tools I Use")
    st.markdown("#### Python | Power BI | Behavioral Logic")

    st.markdown("##### 📬 Want to build systems that think like this?")
    st.markdown("[Let's talk](mailto:otienok@gmail.com)")

    st.markdown(" ###### *“As Naval Ravikant said: \
                  ‘The only real test of intelligence is if you get what you want out of life.’ I design systems that help people do exactly that.”*")
    

elif page == "Projects":
    st.header("Field Rythm")
    st.markdown("*Turning silent data into actionable insight through rhythm-based analysis*")
    st.write("We collect data through application—as is the norm for many. " \
    "But data only communicates when interrogated for meaning. " \
    "Most of the time, it sits silent. Yet this silence is what keeps the field in rhythm, built for clarity.")
    st.markdown("**Insights** — Data isn’t vocal but valuable — it becomes meaningful when interrogated.")
    st.markdown("**Systems** — Rhythm analysis designed to extract clarity from operational data.")
    st.markdown("**Outcome** Nudging in the right direction.")


    st.header("Backend Engagement")
    st.markdown("*Extracting decisions from minimal inputs using behavioral nudging and daily loops*")
    st.write("So much is stored in spreadsheets and databases. But what have we truly asked of them?")
    st.markdown("**Insight** - Even with just two features, data can communicate—if we script it with intention.")
    st.markdown("**System** - A backend nudging engine that sends daily email cues, helping teams make decisions from minimal inputs.")
    st.markdown("**Outcome** Making real time decisions")

    
    st.header("Buy Back Time")
    st.markdown("*Reclaiming hours through reporting systems that mirror reality, not bureaucracy*")
    st.write("How long does it take to send out that report? In the age of data, time is currency.")
    st.markdown("**Insight** — Reporting shouldn’t be a burden—it should be a mirror.")
    st.markdown("**System** — A reporting engine that reduced turnaround from 7 days to 1 hour " \
    "using simple charts and behavioral cues.")
    st.markdown("**Outcome** — Buy back time. Redeploy energy. Reclaim clarity.")

elif page == "Blog":
    blog_data = Blogs().get_blogs()
    if isinstance(blog_data, dict):
        for date, entries in blog_data.items():
            st.subheader(f"📅 {date}")
            for title, content in entries.items():
                st.markdown(f"### {title}")
                st.write(content)
                st.markdown("---")
    else:
        st.warning(blog_data)

elif page == 'Contact Me':
    st.header("📬 Let's Build from Reality")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("What do you want to build or solve?")
        submit_button = st.form_submit_button(label="Send Message")

        if submit_button:
            if name and email and message:
                st.success("Thanks for reaching out. I’ll get back to you soon.")
                # You can add logic here to send email or store data
            else:
                st.error("Please fill out all fields before submitting.")
    st.markdown("##### [📱 Message me on WhatsApp](https://wa.me/254712016435)")




