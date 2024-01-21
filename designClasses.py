import random
import streamlit as st
import streamlit_scrollable_textbox as sst
import brain


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
    "None": "none",
    "Beginner": "beginner",
    "Intermediate": "intermediate",
    "Advanced": "advanced",
    "Professional": "professional"
}

# Define a dictionary of note categories
note_categories = {
    "None": "none",
    "Music": "music",
    "Education": "education",
    "Travel": "travel",
    "Literature": "literature",
    "Employment": "employment",
    "Architecture": "architecture",
    "Industry & Automation": "industry",
    "Automobile": "automobile"
}


class WebComponents:

    @staticmethod
    def promptSummariseArea() -> str:
        st.write("# :rainbow[Learnify]")
        st.write("### Notes Summariser")
        text = st.text_area(label="label", label_visibility="hidden", height=350, max_chars=2500,
                            placeholder="Paste your text here to summarise it!!")

        if st.button("Summarise"):
            summarisedText = brain.openAISummariser(text)
            return sst.scrollableTextbox(summarisedText, height=200)
        else:
            return None

    @staticmethod
    def doubtSolver():
        st.write("### Doubts Solver")
        doubtText = st.text_area(label="Get your doubts solved instantly!", height=100, max_chars=250,
                                 placeholder="Paste or type your doubt here")
        if st.button(label="Solve my doubts"):
            doubtSolution = brain.openAIDoubtSolver(doubtText)
            return sst.scrollableTextbox(doubtSolution, height=200)
        else:
            return None

    @staticmethod
    def quizSection():
        st.divider()
        st.write("### Quiz Section")
        st.write("#### Question 1")
        st.radio(label="What came first Chicken or Egg?", options=["Idk", "Idc", "Doesn't matter", "Dinosaurs"])
        st.write("#### Question 2")
        st.radio(label="What is the full form of Idk",
                 options=["Idk", "I don't know", "I do not know", "I know I won't tell"])
        st.button(label="Submit")
        st.divider()

    @staticmethod
    def generateNotes():
        st.subheader("Notes Generator")
        note_title = st.text_input("Enter Title")
        note_category = st.selectbox("Enter Category", list(note_categories.keys()))
        note_content = st.text_area("Enter Note Content Details", max_chars=250)
        translation_language = st.selectbox("Select Language", list(languages.keys()))
        note_level = st.selectbox("Note Level", list(note_levels.keys()))

        if st.button("Generate Notes"):
            generatedContent = brain.openAINotesProvider(note_title, note_category, note_content, translation_language, note_level)
            return sst.scrollableTextbox(generatedContent, height=200)
        else:
            return None

    @staticmethod
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
            error_label = ""
            # Display error label
            st.write(error_label)
            # Display the generated motivational message
            st.write(f"{motivational_message}")

        return [note_title, note_category, note_content, translation_language, note_level]


# Define the Streamlit app
def main():
    st.title("SummNote")

    # Call the WebComponents functions
    notes = WebComponents.promptSummariseArea()
    WebComponents.summaryProvider(notes)

    doubtSolverValue = WebComponents.doubtSolver()
    WebComponents.doubtSolutionArea()

    WebComponents.quizSection()

    note_input_form()


if __name__ == "__main__":
    main()
