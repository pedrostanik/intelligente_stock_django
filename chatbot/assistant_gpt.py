from openai import OpenAI
class AssistantGPT():
    def __init__(self):
        self.client = OpenAI()

    def execute(self, question):
        system_instruction = {
            "role": "system",
            "content": "Você é um chatbot especializado para petshop. Qualquer pergunta que fuja à esse tema, avise que foge ao tema principal"
        }
        completion = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            system_instruction,
                {"role": "user", "content": question}
            ]
        )
        message = completion.choices[0].message
        answer = message.content
        print(f'answer: {answer}')
        return answer

if (__name__=='__main__'):
    assistant_gpt = AssistantGPT()
    assistant_gpt.execute()