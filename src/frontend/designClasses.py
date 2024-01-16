import streamlit as st


class WebComponents:

    @staticmethod
    def promptSummariseArea():
        st.write("# :rainbow[Learnify]")
        st.write("### Notes Summariser")
        text = st.text_area(label="label", label_visibility="hidden", height=350, max_chars=5000, placeholder="Paste your text here to summarise it!!")
        st.divider()

    @staticmethod
    def doubtSolver():
        st.write("### Doubts Solver")
        doubtText = st.text_area(label="Get your doubts solved instantly!", height=100, max_chars=250, placeholder="Paste or type your doubt here")
        highlights = st.multiselect(label="Topic related to", options=["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"], default=["Topic 1", "Topic 2"], placeholder="Click to select")
        st.divider()

    @staticmethod
    def quizSection():
        st.write("### Quiz Section")
        st.write("#### Question 1")
        st.radio(label="What came first Chicken or Egg?", options=["Idk", "Idc", "Doesn't matter", "Dinosaurs"])
        st.write("#### Question 2")
        st.radio(label="What is fullform of Idk", options=["Idk", "I don't no", "I do no", "I know I won't tell"])
        st.button(label="Submit")
        st.divider()


