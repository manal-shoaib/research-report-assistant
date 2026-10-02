from crewai import Crew, Process

from agents import (
    research_manager,
    researcher,
    analyst,
    report_writer,
)

from tasks import (
    planning_task,
    research_task,
    analysis_task,
    report_task,
)


def create_research_crew():

    """
    Creates the Research & Report Assistant.

    All tasks are executed sequentially.
    """

    research_crew = Crew(

        agents=[
            research_manager,
            researcher,
            analyst,
            report_writer,
        ],

        tasks=[
            planning_task,
            research_task,
            analysis_task,
            report_task,
        ],

        process=Process.sequential,

        verbose=True,
    )

    return research_crew
