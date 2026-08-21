"""Runs the poisoned-log/ticket fixtures through the pipeline N times and
records whether each injected instruction successfully altered agent behavior.

TODO: implement single-shot, 10x, and 100x repeated-attempt conditions,
with and without each defense in src/defenses enabled.
"""


def run_attack_suite(fixtures_path: str, defenses_enabled: list[str], attempts: int) -> dict:
    raise NotImplementedError
