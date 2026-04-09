# Report

## Business Use Case
This project focuses on converting unstructured meeting or operational notes into structured action items for healthcare workflows.

## Model Used
An OpenAI chat model was used through the API to generate action items from text input.

## Baseline vs Final Design
The initial prompt generated action items but lacked consistency and sometimes introduced details that were not present in the input. After revising the prompt to include structure and guardrails, the output became more consistent and more accurate.

## Limitations
The system still struggles with vague or incomplete notes and may fail to extract meaningful action items when context is limited.

## Recommendation
This workflow is useful as a draft assistant to save time, but it should not be fully automated without human review.