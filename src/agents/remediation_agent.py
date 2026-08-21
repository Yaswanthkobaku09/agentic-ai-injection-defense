"""Remediation agent: the highest-privilege agent in the pipeline.

Has tool access to (mock) remediation actions. Every call must pass through
src/defenses/tool_scoping.py — this is the agent an injected instruction is
trying to reach.
"""


class RemediationAgent:
    def __init__(self, model: str = "claude-sonnet-5"):
        self.model = model

    def propose_action(self, incident_summary: dict) -> dict:
        raise NotImplementedError
