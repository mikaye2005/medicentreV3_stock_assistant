def parse_assistant_answer(answer_text: str) -> dict:
    """
    Parse the assistant response into structured sections.

    Expected format:
    Direct Answer: ...
    Explanation: ...
    Relevant Table(s): ...

    If the format is imperfect, the function still tries to recover
    useful sections and falls back safely.
    """
    result = {
        "direct_answer": "",
        "explanation": "",
        "relevant_tables": "",
        "raw_answer": answer_text.strip(),
    }

    if not answer_text:
        return result

    lines = [line.strip() for line in answer_text.splitlines() if line.strip()]

    current_section = None

    for line in lines:
        lower = line.lower()

        if lower.startswith("direct answer:"):
            result["direct_answer"] = line.split(":", 1)[1].strip()
            current_section = "direct_answer"
            continue

        if lower.startswith("explanation:"):
            result["explanation"] = line.split(":", 1)[1].strip()
            current_section = "explanation"
            continue

        if lower.startswith("relevant table(s):"):
            result["relevant_tables"] = line.split(":", 1)[1].strip()
            current_section = "relevant_tables"
            continue

        # If the model puts extra text on the next lines,
        # keep attaching it to the last detected section.
        if current_section:
            if result[current_section]:
                result[current_section] += " " + line
            else:
                result[current_section] = line

    # Fallbacks if the model did not fully follow the format
    if not result["direct_answer"] and result["raw_answer"]:
        result["direct_answer"] = result["raw_answer"]

    return result