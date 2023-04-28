import agent_api
import sys
from termcolor import colored


class Game:
    intro_text_list = [
        "                                         ",
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
    ]
    help_text_list = [
        "                                         ",
        "  Useful Commands:                       ",
        "      !exit - Exits the game.            ",
        "      !red  - Talk to " +
        colored("Red", "red", "on_white", attrs=['bold']) +
        colored(".               ", "dark_grey", "on_white"),
        "      !blue - Talk to " +
        colored("Blue", "blue", "on_white", attrs=['bold']) +
        colored(".              ", "dark_grey", "on_white"),
        "      !meet - Make the agents chat with  ",
        "              each other.                ",
        "      !help - See this command list.     ",
        "                                         ",
    ]
    good_luck_text_list = [
        colored("             🍀 Good Luck! 🍀            ",
                "green", "on_white", attrs=["bold"]),
        "                                         ",
    ]
    game_over_text_list = [
        "        ~~ Thanks for playing ~~         "
    ]

    red_name = colored("Red", "red")
    blue_name = colored("Blue", "blue")

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
                "colored_name": Game.red_name,
            },
            "blue": {
                "session": self.blue_session,
                "colored_name": Game.blue_name,
            },
            None: {
                "session": None,
                "colored_name": "nobody"
            }
        }
        self.current_agent_color = None
        self.last_agent_color = None

    def chat_to_agent_and_get_response(self, agent_color, message):
        session = self.agent_dict[agent_color]["session"]
        return agent_api.say_to_session_and_get_text_response(session, message)

    def run_command(self, command):
        match command:
            case "exit":
                print()
                self.print_game_text(Game.game_over_text_list)
                print()
                sys.exit()
            case "red":
                self.current_agent_color = "red"
            case "blue":
                self.current_agent_color = "blue"
            case "meet":
                self.last_agent_color = self.current_agent_color
                self.current_agent_color = "both"
            case "help":
                self.print_game_text(Game.help_text_list)
            case _:
                print("> Unrecognized command, say '!help' to see the command list.")

    def determine_first_speaker(self):
        choice = None
        while True:
            print("Who should speak first, {} or {}? ".format(
                Game.red_name, Game.blue_name), end="")
            choice = input().lower()
            if choice not in ['red', 'blue']:
                print("> Invalid choice.")
                continue
            break
        return choice

    def handle_meet(self):
        first_speaker_color = self.determine_first_speaker()
        second_speaker_color = {'red': 'blue',
                                'blue': 'red'}[first_speaker_color]

        speaker = first_speaker_color
        listener = second_speaker_color

        message = self.chat_to_agent_and_get_response(
            speaker, "{}: Hello, {}.".format(listener.capitalize(), speaker.capitalize()))
        print()
        print("> Press enter in between messages to continue. Type any letter and press enter to end the conversation between the two agents.")
        print()
        print("{} to {}: {}".format(
            self.agent_dict[speaker]["colored_name"],
            self.agent_dict[listener]["colored_name"],
            message,
        ))
        while True:
            if input("> ") != '':
                self.current_agent_color = self.last_agent_color
                return
            prefix = speaker.capitalize() + ": "
            personified_message = prefix + message
            response = self.chat_to_agent_and_get_response(
                listener, personified_message)
            speaker, listener = listener, speaker
            print("{} to {}: {}".format(
                self.agent_dict[speaker]["colored_name"],
                self.agent_dict[listener]["colored_name"],
                response,
            ))
            message = response

    def rolling_chat(self):
        while True:
            if self.current_agent_color == "both":
                self.handle_meet()
                continue

            conversation_partner_name = self.agent_dict[self.current_agent_color]["colored_name"]
            print()
            print("You (to {}): ".format(conversation_partner_name), end="")
            message = input()

            if not message:
                continue

            if len(message) > 2 and message[0] == "!":
                self.run_command(message[1:])
                continue

            if self.current_agent_color is None:
                continue

            print(
                conversation_partner_name + ":",
                self.chat_to_agent_and_get_response(
                    self.current_agent_color, "Player: " + message)
            )

    def print_game_text(self, text_list):
        for line in text_list:
            print(colored(line, "dark_grey", "on_white"))

    def start_game(self):
        self.print_game_text(Game.intro_text_list)
        self.print_game_text(Game.help_text_list)
        self.print_game_text(Game.good_luck_text_list)
        self.rolling_chat()


if __name__ == "__main__":
    game = Game()
    game.start_game()
