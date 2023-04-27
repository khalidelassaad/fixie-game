import agent_api
import sys
from termcolor import colored


class Game:
    def __init__(self, skip_init=False):
        if skip_init:
            return
        self.red_session = agent_api.create_session("red-agent")
        self.blue_session = agent_api.create_session("blue-agent")
        self.red_session_handle = agent_api.get_session_handle(
            self.red_session)
        self.blue_session_handle = agent_api.get_session_handle(
            self.blue_session)
        self.agent_dict = {
            "red": {
                "session": self.red_session,
                "colored_name": colored("Red", "red"),
            },
            "blue": {
                "session": self.blue_session,
                "colored_name": colored("Blue", "blue"),
            },
            None: {
                "session": None,
                "colored_name": "nobody"
            }
        }
        self.current_agent_color = None

    def chat_to_agent_and_get_response(self, agent_color, message):
        session = self.agent_dict[agent_color]["session"]
        return agent_api.say_to_session_and_get_text_response(session, message)

    def run_command(self, command):
        match command:
            case "exit":
                print("~~Thanks for playing~~")
                sys.exit()
            case "red":
                self.current_agent_color = "red"
            case "blue":
                self.current_agent_color = "blue"
            case "inv":
                print("You have nothing in your inventory.")

    def rolling_chat(self):
        conversation_partner_name = self.agent_dict[self.current_agent_color]["colored_name"]
        while True:
            print("You (to {}): ".format(conversation_partner_name), end="")
            message = input()

            if message[0] == "!":
                self.run_command(message[1:])
                continue

            if self.current_agent_color is not None:
                print(
                    conversation_partner_name + ":",
                    self.chat_to_agent_and_get_response(
                        self.current_agent_color, message)
                )

    def print_intro_text(self):
        intro_text = [
            "  Welcome to Conflict Resolution Class!  ",
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
            "  Your goal is to resolve a conflict     ",
            "  between " +
            colored("Red", "red", "on_white", attrs=['bold']) +
            colored(" and ", "dark_grey", "on_white") +
            colored("Blue", "blue", "on_white", attrs=['bold']) +
            colored(".                  ", "dark_grey", "on_white"),
            "                                         ",
            "  Chat with them, ask them questions     ",
            "  understand their differences, earn     ",
            "  their trust, and settle their beef.    ",
            "                                         ",
            "  Useful Commands:                       ",
            "      !exit - Exits the game.            ",
            "      !red  - Talk to " +
            colored("Red", "red", "on_white", attrs=['bold']) +
            colored(".               ", "dark_grey", "on_white"),
            "      !blue  - Talk to " +
            colored("Blue", "blue", "on_white", attrs=['bold']) +
            colored(".             ", "dark_grey", "on_white"),
            "      !inv - Check your inventory.       ",
            "                                         ",
            colored("             🍀 Good Luck! 🍀            ",
                    "green", "on_white", attrs=["bold"]),
            "                                         ",


        ]
        for line in intro_text:
            print(colored(line, "dark_grey", "on_white"))

    def start_game(self):
        self.print_intro_text()
        self.rolling_chat(None)


if __name__ == "__main__":
    game = Game()
    game.start_game()
