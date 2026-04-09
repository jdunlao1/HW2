import os
import json
import anthropic

# Initialize client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# System prompt (final improved version)
SYSTEM_PROMPT = """
Convert notes into structured action items.

Each action item must include:
- task
- owner (if available)
- priority (High, Medium, Low)

If the input is unclear or does not contain real follow ups, say:
No action items found.

Do not invent names or details.
"""

def generate(note):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": note}
        ]
    )

    return response.content[0].text


def run_eval():
    with open("eval_set.json") as f:
        data = json.load(f)

    print("\nEVALUATION RESULTS")

    for case in data:
        print("\n" + "=" * 60)
        print(f"Input: {case['input']}")
        print(f"Expected: {case['expected_behavior']}")

        output = generate(case["input"])

        print("\nModel Output:")
        print(output)
        print()


if __name__ == "__main__":
    run_eval()