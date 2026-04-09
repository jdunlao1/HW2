# Prompt Iteration

## Initial Version
Convert notes into action items.

## Revision 1
Convert notes into structured action items. Include the task, owner if available, and a priority level (High, Medium, Low).

### What changed and why
I added structure so the output is consistent and easier to evaluate.

### What improved or stayed the same
The output became more organized, but still sometimes guessed details.

## Revision 2
Convert notes into structured action items. Include the task, owner if available, and a priority level (High, Medium, Low). If the input is unclear or does not contain real follow ups, say "No action items found." Do not invent names or details.

### What changed and why
I added rules to prevent hallucination and improve reliability.

### What improved or stayed the same
The model became more cautious and avoided making things up.