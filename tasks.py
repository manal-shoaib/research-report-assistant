from crewai import Task

from agents import (
    research_manager,
    researcher,
    analyst,
    report_writer,
)


# =========================================================
# TASK 1 — RESEARCH PLANNING
# =========================================================

planning_task = Task(

    description="""

    The user wants a research report about:

    {topic}

    Create a research plan.

    The plan should include:

    1. Main research questions
    2. Important areas to investigate
    3. Important information that should be collected
    4. Possible limitations
    5. Important perspectives that should be considered

    Do NOT write the final report.

    Only create the research plan.

    """,

    expected_output="""

    A clear research plan containing:

    - Research questions
    - Investigation areas
    - Information requirements
    - Potential limitations
    - Important perspectives

    """,

    agent=research_manager,
)


# =========================================================
# TASK 2 — RESEARCH
# =========================================================

research_task = Task(

    description="""

    Conduct research about:

    {topic}

    Use the research plan created by the Research Manager.

    Produce detailed research notes.

    Focus on:

    - Important facts
    - Key findings
    - Evidence
    - Important examples
    - Different perspectives
    - Statistics when available
    - Limitations
    - Potential sources

    Do NOT write the final report.

    """,

    expected_output="""

    Detailed research notes containing:

    - Key findings
    - Important evidence
    - Examples
    - Statistics when available
    - Different perspectives
    - Limitations
    - Source information

    """,

    agent=researcher,
)


# =========================================================
# TASK 3 — ANALYSIS
# =========================================================

analysis_task = Task(

    description="""

    Analyze the research collected about:

    {topic}

    Your responsibilities are:

    1. Identify the most important findings.
    2. Organize the evidence.
    3. Identify strong and weak claims.
    4. Identify contradictions.
    5. Identify limitations.
    6. Remove unnecessary repetition.
    7. Decide which findings are important for the final report.

    Do NOT write the final report.

    Create a structured analysis for the Report Writer.

    """,

    expected_output="""

    A structured research analysis containing:

    - Key findings
    - Supporting evidence
    - Important claims
    - Contradictions
    - Limitations
    - Recommendations for the final report

    """,

    agent=analyst,
)


# =========================================================
# TASK 4 — FINAL REPORT
# =========================================================

report_task = Task(

    description="""

    Write a professional research report about:

    {topic}

    Use the research analysis produced by the previous agent.

    The report must contain:

    # Research Report

    ## Executive Summary

    ## Introduction

    ## Key Findings

    ## Detailed Analysis

    ## Benefits / Opportunities

    ## Challenges / Limitations

    ## Future Outlook

    ## Conclusion

    ## Sources

    Requirements:

    - Use clear language.
    - Do not invent facts.
    - Do not invent sources.
    - Do not make unsupported claims.
    - Clearly separate evidence from opinions.
    - Use Markdown formatting.
    - Make the report useful for a student or general reader.

    """,

    expected_output="""

    A complete professional research report in Markdown
    format containing:

    - Executive Summary
    - Introduction
    - Key Findings
    - Detailed Analysis
    - Benefits / Opportunities
    - Challenges / Limitations
    - Future Outlook
    - Conclusion
    - Sources

    """,

    agent=report_writer,
)
