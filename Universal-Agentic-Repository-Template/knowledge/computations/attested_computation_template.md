---
type: Attested Computation
uid: comp-example-v1
title: Standard Discounted Cashflow Formula
runtime: python
parameters:
  - { name: cash_flows, type: array_float, required: true }
  - { name: rate, type: float, required: true }
computation: /src/core/math/dcf.py
attester: /tools/attesters/check_dcf.py
status: stable
verified: { by: human:lead-quant, at: 2026-10-01 }
---

# Computation Summary
Computes the present value of expected cash flows discounted at a constant rate.
