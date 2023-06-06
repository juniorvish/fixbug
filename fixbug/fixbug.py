import sys
import os
import subprocess
import json
import openai

def main():
    if len(sys.argv) < 2:
        print("Usage: fixbug <command> [args]")
        sys.exit(1)

    command = sys.argv[1:]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(e.output)
        user_message = str(e.output).strip()
        prompt = f"User: {user_message}\nAI Developer:"
        message = []
        message.append({"role": "system", "content": "You are a friendly AI Developer"})
        message.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=message,
                                                temperature=0.2,
                                                max_tokens=4000,
                                                frequency_penalty=0.9)
        gpt_message = response.choices[0].message.content
        print(gpt_message)

if __name__ == "__main__":
    main()