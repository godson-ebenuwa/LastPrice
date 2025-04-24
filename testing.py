from mistral import query
from template import NEGOTIATION_TEMPLATE


def clean_response(text):
    clean_text = text.split('[/INST]')[-1]
    clean_text = clean_text.split('[INST]')[0]
    clean_text = clean_text.strip()
    return clean_text


def interactive_test():
    print("LastPrice AI Negotiation Simulator")
    chat_history = []

    while True:
        host_msg = input("\nHost's message (type 'exit' to quit): ")
        if host_msg.lower() == 'exit':
            break

        history_str = "\n".join([
            f"{msg}"
            for msg in chat_history[-5:]
        ])

        prompt = NEGOTIATION_TEMPLATE.format(
            budget=100,
            max_budget=120,
            dates="Dec 1-5, 2025",
            amenities="WiFi, kitchen",
            host_message=host_msg,
            target_price=110,
            chat_history=history_str
        )

        response = query(prompt)

        if response and isinstance(response, list):
            raw_text = response[0].get('generated_text', '')
            ai_response = clean_response(raw_text)
            print("\nLastPrice AI:", ai_response)

            chat_history.append(f"Host: {host_msg}")
            chat_history.append(f"AI: {ai_response}")
        else:
            print("\nError generating response")

if __name__ == "__main__":
    interactive_test()