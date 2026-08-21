"""Least-privilege tool scoping for the remediation agent.

TODO: define a per-agent allowlist of tool calls and argument ranges;
reject anything outside scope before execution.
"""

ALLOWED_TOOLS: dict[str, list[str]] = {
    "triage_agent": [],
    "log_summarizer_agent": [],
    "remediation_agent": [],
}


def is_allowed(agent_name: str, tool_name: str) -> bool:
    raise NotImplementedError
