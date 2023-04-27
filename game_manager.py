import agent_api
import sys


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
                "chat_prefix": "Red:",
            },
            "blue": {
                "session": self.blue_session,
                "chat_prefix": "Blue:",
            },
        }

    def chat_to_agent_and_get_response(self, agent_color, message):
        session = self.agent_dict[agent_color]["session"]
        return agent_api.say_to_session_and_get_text_response(session, message)

    def rolling_chat(self, agent_color):
        while True:
            try:
                print("Me: ", end="")
                message = input()
                if message == "exit":
                    return
                print(
                    self.agent_dict[agent_color]["chat_prefix"],
                    self.chat_to_agent_and_get_response(agent_color, message)
                )
            except KeyboardInterrupt:
                print("~~Thanks for playing~~")
                sys.exit()


if __name__ == "__main__":
    game = Game()
    game.rolling_chat("blue")
