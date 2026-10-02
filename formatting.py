def clean_report(result):
    """
    Converts the CrewAI result into normal text
    that Streamlit can display.
    """

    if result is None:
        return "No report was generated."

    if hasattr(result, "raw"):
        return result.raw

    return str(result)
