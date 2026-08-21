"""Alert-triage agent: ingests raw log/ticket text and classifies severity.

TODO: implement the agent loop (tool calls into the mock ticket store),
wired through the defenses in src/defenses before any tool call executes.
"""


class TriageAgent:
    def __init__(self, model: str = "claude-sonnet-5"):
        self.model = model

    def triage(self, ticket: dict) -> dict:
        raise NotImplementedError
