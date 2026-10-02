import streamlit as st

from crew import create_research_crew
from formatting import clean_report


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Research & Report Assistant",
    page_icon="🔎",
    layout="wide",
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🔎 Research & Report Assistant")

st.write(
    "A multi-agent AI system that researches a topic, "
    "analyzes information, and creates a structured report."
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("🤖 AI Agents")

    st.write(
        """
        This application uses four sequential agents:

        1. 📋 Research Manager
        2. 🔎 Researcher
        3. 📊 Fact & Source Analyst
        4. ✍️ Report Writer
        """
    )

    st.divider()

    st.write(
        "The agents work one after another."
    )


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

topic = st.text_area(
    "Enter your research topic",
    placeholder=(
        "Example: The impact of artificial intelligence "
        "on education"
    ),
    height=150,
)


# ---------------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------------

generate = st.button(
    "🚀 Generate Research Report",
    type="primary",
)


# ---------------------------------------------------------
# RUN THE MULTI-AGENT SYSTEM
# ---------------------------------------------------------

if generate:

    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

    else:

        st.info(
            "The agents are working sequentially. "
            "Please wait..."
        )

        try:

            with st.spinner(
                "🤖 Research team is working..."
            ):

                # Create our CrewAI system
                research_crew = create_research_crew()

                # Start the crew
                result = research_crew.kickoff(
                    inputs={
                        "topic": topic
                    }
                )

            # Convert result into clean text
            report = clean_report(result)

            st.success(
                "✅ Research report generated!"
            )

            st.divider()

            # Display report
            st.markdown(report)

            st.divider()

            # Download report
            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="research_report.md",
                mime="text/markdown",
            )

        except Exception as error:

            st.error(
                "❌ Something went wrong."
            )

            st.exception(error)
