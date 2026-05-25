# DTTS v0.3.0 Synthesis Report

Status: PASS-DTTS-V030-SYNTHESIS-LOCKED

## Scope

This report synthesizes DTTS v0.2.0--v0.2.8 toy-model audits for sleep-like recovery transitions in finite adaptive networks. It is not a clinical, biological, EEG, wearable-device, diagnostic, or therapeutic claim.

## Locked claim

Within the implemented finite adaptive-network toy-model sequence, DTTS-like sleep-gate onset, hysteresis-like persistence, structurally aligned selective protection, perturbation-recovery response, and topology/noise robustness were observed within tested regimes. Expanded audits identified failure boundaries, and frozen minimal rescue policies generalized across holdout seeds, simplified topologies, and noise levels for most rescue-sensitive regimes, while weak-protection conditions remained unstable under harsher holdout. This is a claim-bounded network-dynamical toy-model result, not a biological or clinical sleep claim.

## Phase ledger

| Phase | Status | Role | Key result |
|---|---|---|---|
| v0.2.0 | PASS-DTTS-V020-RUN-COMPLETE | Threshold, hysteresis preflight, protection, and negative controls | Within the implemented finite adaptive-network toy model, load accumulation and coherence loss can produce threshold-like sleep-propensit... |
| v0.2.1 | PASS-DTTS-V021-RUN-COMPLETE | Closed-loop hysteresis and protection holdout | Within the implemented finite adaptive-network toy model, continuous load ramps produce threshold-like sleep-gate activation with hystere... |
| v0.2.2 | PASS-DTTS-V022-RUN-COMPLETE | Circadian-gate and multi-cycle audit | Within the implemented finite adaptive-network toy model, circadian-like permissive gating modulates threshold-like sleep-gate timing, an... |
| v0.2.3 | PASS-DTTS-V023-RUN-COMPLETE | Perturbation-recovery audit, numpy trapezoid hotfix preferred | Within the implemented finite adaptive-network toy model, acute load pulses evoke a sleep-like recovery-gate response, and structurally a... |
| v0.2.4 | PASS-DTTS-V024-RUN-COMPLETE | Topology and noise robustness audit | Within the implemented finite adaptive-network toy model, the sleep-like recovery-gate response and structurally aligned selective-protec... |
| v0.2.5 | PASS-DTTS-V025-RUN-COMPLETE | Parameter-envelope and conservative boundary audit | Within the implemented finite adaptive-network toy model, the sleep-like recovery gate and structurally aligned selective-protection effe... |
| v0.2.6 | PASS-DTTS-V026-RUN-COMPLETE | Expanded failure-boundary and holdout audit | failure cases=69; holdout pass=3 |
| v0.2.7 | PASS-DTTS-V027-RUN-COMPLETE | Mechanism-rescue and regime classification audit | Within the implemented finite adaptive-network toy model, DTTS-like behavior separates into native-pass, rescue-sensitive, and persistent... |
| v0.2.8 | PASS-DTTS-V028-RUN-COMPLETE | Frozen-rescue holdout audit | frozen mean pass rate=0.7729166666666667; unstable rescue boundaries=1 |

## Interpretation

The strongest synthesis is not that DTTS is a general theory of biological sleep. The supported interpretation is narrower: the implemented toy model exhibits a sleep-like recovery-gate transition, hysteresis-like persistence, and selective protection under tested regimes, with explicit failure boundaries and rescue-sensitive regimes.

## Holdout result from v0.2.8

Frozen policy mean pass rate: 0.7729166666666667
Native pass count: 1
Rescue holdout pass count: 4
Unstable rescue boundary count: 1
Persistent failure boundary count: 0

## Forbidden claims

- clinical sleep diagnosis
- medical advice or treatment guidance
- human or animal sleep-data validation
- EEG or wearable-device prediction
- complete biological theory of sleep
