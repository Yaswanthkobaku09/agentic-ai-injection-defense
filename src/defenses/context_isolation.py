"""Separates trusted instruction context from untrusted retrieved/log content.

TODO: implement channel tagging so downstream agents can distinguish
"instruction" tokens from "data" tokens, per the ACE (NDSS '26) architecture.
"""


def isolate(instructions: str, untrusted_content: str) -> dict:
    raise NotImplementedError
