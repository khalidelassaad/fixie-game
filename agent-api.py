import requests
import dotenv
import os

FIXIE_API_KEY = dotenv.dotenv_values(
    ".env")["FIXIE_API_KEY"]
FIXIE_USERNAME = dotenv.dotenv_values(
    ".env")["FIXIE_USERNAME"]

HEADERS = {
    "Authorization": "Bearer ${}".format(FIXIE_API_KEY),
    "Content-Type": "application/json"
}


def talk_to_agent(agent_name, message):
    agent_url = "https://app.fixie.ai/api/agents/{}/{}".format(
        FIXIE_USERNAME, agent_name)
    response = requests.post(
        agent_url,
        data={"message": {"text": message}},
        headers=HEADERS
    )
    print(FIXIE_API_KEY)
    return response.text


if __name__ == "__main__":
    print(talk_to_agent("myagent", "Hello, what do you do?"))
