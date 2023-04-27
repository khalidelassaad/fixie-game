import agent_api
import sys
from termcolor import colored


class Game:
    def __init__(self):
        self.red_session = agent_api.create_session("red-agent")
        self.blue_session = agent_api.create_session("blue-agent")
        self.red_session_handle = agent_api.get_session_handle(
            self.red_session)
        self.blue_session_handle = agent_api.get_session_handle(
            self.blue_session)
        self.agent_dict = {
            "red": {
                "session": self.red_session,
                "chat_prefix": colored("Red:", "red"),
            },
            "blue": {
                "session": self.blue_session,
                "chat_prefix": colored("Blue:", "blue"),
            },
        }

    def chat_to_agent_and_get_response(self, agent_color, message):
        session = self.agent_dict[agent_color]["session"]
        return agent_api.say_to_session_and_get_text_response(session, message)

    def rolling_chat(self, agent_color):
        while True:
            print("You: ", end="")
            message = input()
            if message == "exit":
                print("~~Thanks for playing~~")
                sys.exit()
            print(
                self.agent_dict[agent_color]["chat_prefix"],
                self.chat_to_agent_and_get_response(agent_color, message)
            )


if __name__ == "__main__":
    game = Game()
    game.rolling_chat("blue")
