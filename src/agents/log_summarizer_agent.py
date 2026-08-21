"""Log-summarizer agent: reduces raw log dumps to a structured incident summary.

This is the primary indirect-injection surface — log content is untrusted
and must pass through src/defenses/context_isolation.py before reaching
the model's instruction context.
"""


class LogSummarizerAgent:
    def __init__(self, model: str = "claude-sonnet-5"):
        self.model = model

    def summarize(self, raw_logs: list[str]) -> dict:
        raise NotImplementedError
