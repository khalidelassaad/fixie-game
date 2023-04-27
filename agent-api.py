import dotenv
import json
import fixieai

FIXIE_API_KEY = dotenv.dotenv_values(
    ".env")["FIXIE_API_KEY"]
FIXIE_USERNAME = dotenv.dotenv_values(
    ".env")["FIXIE_USERNAME"]

CLIENT = fixieai.FixieClient(FIXIE_API_KEY)


def create_session(agent_name):
    # Creates a session with the provided agent_name and returns the Session object
    session = CLIENT.create_session("{}/{}".format(FIXIE_USERNAME, agent_name))
    return session


def get_session_handle(session):
    return session.get_metadata()['handle']


def say_to_session(session, message):
    session.add_message(message)
    return session.get_messages()[-1]


if __name__ == "__main__":
    print(get_session_handle(create_session("myagent")))
