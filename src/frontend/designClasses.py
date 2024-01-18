import random
import streamlit as st
import streamlit_scrollable_textbox as sst
# from src.backend import brain


class WebComponents:

    @staticmethod
    def promptSummariseArea():
        st.write("# :rainbow[Learnify]")
        st.write("### Notes Summariser")
        text = st.text_area(label="label", label_visibility="hidden", height=350, max_chars=2500,
                            placeholder="Paste your text here to summarise it!!")
        st.button(label="Summarise")
        st.divider()
        return text

    @staticmethod
    def summaryProvider(summary="This is summary body"):
        st.write("#### Notes Summary")
        st.text(summary)
        sst.scrollableTextbox(summary, height=250, border=False)

        st.divider()

    @staticmethod
    def doubtSolver():
        st.write("### Doubts Solver")
        doubtText = st.text_area(label="Get your doubts solved instantly!", height=100, max_chars=250,
                                 placeholder="Paste or type your doubt here")
        highlights = st.multiselect(label="Topic related to",
                                    options=["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
                                    default=["Topic 1", "Topic 2"], placeholder="Click to select")
        st.button(label="Solve my doubts")
        st.divider()

    @staticmethod
    def quizSection():
        st.write("### Quiz Section")
        st.write("#### Question 1")
        st.radio(label="What came first Chicken or Egg?", options=["Idk", "Idc", "Doesn't matter", "Dinosaurs"])
        st.write("#### Question 2")
        st.radio(label="What is the full form of Idk",
                 options=["Idk", "I don't know", "I do not know", "I know I won't tell"])
        st.button(label="Submit")
        st.divider()


# Define a dictionary of languages for translation
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
}

# Define a dictionary of note levels
note_levels = {
    "Beginner": "beginner",
    "Advanced": "advanced",
}

# Define a dictionary of note categories
note_categories = {
    "Music": "music",
    "Education": "education",
}


def note_input_form():
    st.subheader("Create Summarized Notes")
    note_title = st.text_input("Enter Title")
    note_category = st.selectbox("Enter Category", list(note_categories.keys()))
    note_content = st.text_area("Enter Note Content Details")
    translation_language = st.selectbox("Select Language", list(languages.keys()),
                                        index=list(languages.keys()).index("English"))
    note_level = st.selectbox("Note Level", list(note_levels.keys()))
    stay_motivated = st.checkbox("Stay Motivated!")

    if stay_motivated:
        # Generate an automated motivational message
        motivational_messages = [
            "You're doing great! Keep it up!",
            "Every small step leads to a big achievement.",
            "Believe in yourself, you can do it!",
            # Add more motivational messages as needed
        ]
        motivational_message = random.choice(motivational_messages)

        # Display the generated motivational message
        st.write(f"{motivational_message}")

    # Button to generate notes
    st.button(label="Generate Notes")


# Define the Streamlit app
def main():
    st.title("SummNote")

    # Call the WebComponents functions
    notes = WebComponents.promptSummariseArea()
    WebComponents.summaryProvider(notes)
    WebComponents.doubtSolver()
    WebComponents.quizSection()

    # Call the note_input_form function
    note_input_form()


if __name__ == "__main__":
    main()