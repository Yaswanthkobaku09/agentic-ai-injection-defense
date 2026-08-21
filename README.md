# Agentic AI Injection Defense

PhD portfolio project — Tier I. Build and break an LLM-driven SOC triage pipeline to
measure whether current prompt-injection defenses actually hold under repeated-attempt
and multi-agent conditions.

## The gap

Prompt injection is still an unsolved architectural problem: LLMs process system
instructions, user input, and retrieved content as one undifferentiated token stream, so
there is no reliable privilege boundary between them. Once an agent has tools — ticket
systems, log stores, remediation scripts — an injected instruction stops being a nuisance
and becomes an action. Reported attack success rates climb sharply with repeated attempts
even against hardened frontier models, so single-shot evaluation understates real risk.

## The project

A minimal multi-agent SOC pipeline (alert-triage agent → log-summarizer agent →
remediation agent) fed intentionally poisoned logs and tickets, with layered defenses
implemented and measured independently and in combination:

- **Context isolation** between instruction and data channels
- **Output filtering** modeled on MELON-style detection
- **Tool scoping** enforcing least privilege per agent

The deliverable is a small, reproducible benchmark: attack success rate before/after each
defense, under single-shot and repeated-attempt (10x, 100x) conditions.

## Status

Scaffold stage — architecture and interfaces defined, implementations pending.

## Repository layout

```
src/
  agents/       triage, summarizer, and remediation agent stubs
  defenses/     context isolation, output filter, tool scoping
  eval/         attack harness and metrics
data/           poisoned log/ticket fixtures (not committed)
```

## Roadmap

1. Implement the three agents against a mock ticket/log store
2. Implement a baseline (undefended) attack harness and measure ASR
3. Add defenses one at a time, re-measure ASR after each
4. Write up results as a short technical report / arXiv-style preprint

## Related work

- USENIX Security '26 — "SoK: Attack and Defense Landscape of Agentic AI Systems"
- NDSS '26 — "ACE: A Security Architecture for LLM-Integrated App Systems"
- MELON — Provable Defense Against Indirect Prompt Injection Attacks in AI Agents
- AgentDyn — dynamic open-ended benchmark for prompt injection evaluation

## License

MIT
