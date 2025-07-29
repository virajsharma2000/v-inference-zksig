# llm-zk-demo

This repository demonstrates how to use `ezkl` (Halo2-based zk-SNARKs) in Python to prove that:
- A model produced a given output for a private input,  
- Without revealing the input or model internals.

It parallels how one might **prove that an LLM generated a response**, without revealing the prompt or weights.

## Prerequisites

- Python 3.9+
- `pip install ezkl`

## Files

- `train_and_export.py`: trains a small classifier and exports to ONNX.
- `input.json`: a sample private input.
- `demo.py`: runs the full `ezkl` flow: setup, witness, proof, verify.

## Usage

```bash
python train_and_export.py
python demo.py
