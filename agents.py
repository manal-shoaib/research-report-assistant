from crewai import Agent, LLM

from config import MODEL_NAME


# =========================================================
# GROQ LLM
# =========================================================

llm = LLM(
    model=f"groq/{MODEL_NAME}",
    temperature=0.2,
)


# =========================================================
# AGENT 1 — RESEARCH MANAGER
# =========================================================

research_manager = Agent(

    role="Research Manager",

    goal=(
        "Create a clear and logical research plan "
        "for the user's topic."
    ),

    backstory=(
        "You are an experienced research manager. "
        "You break complex topics into smaller research "
        "questions and organize the research process."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# =========================================================
# AGENT 2 — RESEARCHER
# =========================================================

researcher = Agent(

    role="Research Specialist",

    goal=(
        "Investigate the research topic and produce "
        "detailed and useful research notes."
    ),

    backstory=(
        "You are a professional research specialist. "
        "You investigate topics carefully, identify "
        "important information, and organize findings "
        "for further analysis."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# =========================================================
# AGENT 3 — FACT & SOURCE ANALYST
# =========================================================

analyst = Agent(

    role="Fact and Source Analyst",

    goal=(
        "Analyze research findings, identify important "
        "claims, organize evidence, and identify "
        "limitations or contradictions."
    ),

    backstory=(
        "You are a critical research analyst. "
        "You examine research information carefully "
        "and organize the strongest useful findings "
        "for the report writer."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# =========================================================
# AGENT 4 — REPORT WRITER
# =========================================================

report_writer = Agent(

    role="Professional Report Writer",

    goal=(
        "Create a clear, professional and well-structured "
        "research report using the research analysis."
    ),

    backstory=(
        "You are an experienced professional report writer. "
        "You transform research findings into clear, "
        "organized and easy-to-understand reports."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)
