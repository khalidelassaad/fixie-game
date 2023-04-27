import requests
import dotenv
import json
import os
import fixieai

FIXIE_API_KEY = dotenv.dotenv_values(
    ".env")["FIXIE_API_KEY"]
FIXIE_USERNAME = dotenv.dotenv_values(
    ".env")["FIXIE_USERNAME"]

HEADERS = {
    "Authorization": "Bearer {}".format(FIXIE_API_KEY),
    "Content-Type": "application/json"
}


def talk_to_agent(agent_name, message):
    agent_url = "https://app.fixie.ai/api/agents/{}/{}".format(
        FIXIE_USERNAME, agent_name)
    response = requests.post(
        agent_url,
        data=json.dumps({"message": {"text": message}}),
        headers=HEADERS
    )
    return json.loads(response.text)["message"]["text"]


client = fixieai.FixieClient(FIXIE_API_KEY)

if __name__ == "__main__":
    # print(talk_to_agent("myagent", "Generate a random number between 4 and 34"))
    # print(client.get_agent('khalidelassaad/myagent'))
    session = client.create_session('khalidelassaad/myagent')
    # session.add_message("Generate a random number between 16 and 65")
    print(session.get_messages()[-1])
