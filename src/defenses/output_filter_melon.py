"""MELON-style output filter: detects whether an agent's next action was
influenced by injected instructions rather than the legitimate task.

TODO: implement the re-execution / consistency check described in MELON
(arXiv 2025) — run the agent's action twice under masked vs. unmasked
untrusted content and compare outputs.
"""


def check_action(action: dict, masked_action: dict) -> bool:
    """Return True if the action appears injection-influenced."""
    raise NotImplementedError
