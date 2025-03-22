import re
import argparse
from marketplace_service import MarketplaceService
from repository import MarketplaceRepository

class CLIHandler:
    def __init__(self, service: MarketplaceService):
        self.service = service

    def execute_command(self, command: str):
        tokens = command.split(" ", 1)
        action = tokens[0]

        if action == "REGISTER":
            username = tokens[1].strip()
            print(self.service.register_user(username))

        elif action == "CREATE_LISTING":
            match = re.match(r"CREATE_LISTING (\S+) '([^']+)' '([^']+)' (\d+) '([^']+)'", command)
            if match:
                username = match.group(1)
                title = match.group(2)
                description = match.group(3)
                price = int(match.group(4))
                category = match.group(5)
                print(self.service.create_listing(username, title, description, price, category))
            else:
                print("Error - Invalid CREATE_LISTING format")

        elif action == "DELETE_LISTING":
            parts = tokens[1].split()
            if len(parts) == 2:
                username = parts[0]
                listing_id = int(parts[1])
                print(self.service.delete_listing(username, listing_id))
            else:
                print("Error - Invalid DELETE_LISTING format")

        elif action == "GET_LISTING":
            parts = tokens[1].split()
            if len(parts) == 2:
                username = parts[0]
                listing_id = int(parts[1])
                print(self.service.get_listing(username, listing_id))
            else:
                print("Error - Invalid GET_LISTING format")

        elif action == "GET_CATEGORY":
            parts = tokens[1].split()
            if len(parts) == 2:
                username = parts[0]
                category = re.search("[^']+", parts[1]).group()
                print(self.service.get_category(username, category))
            else:
                print("Error - Invalid GET_CATEGORY format")

        elif action == "GET_TOP_CATEGORY":
            username = tokens[1].strip()
            print(self.service.get_top_category(username))

        else:
            print("Error - Unknown command")

if __name__ == "__main__":
    repo = MarketplaceRepository()
    service = MarketplaceService(repo)
    cli = CLIHandler(service)
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    args = parser.parse_args()
    
    if args.file:
        input_file = args.file
        try:
            with open(input_file, "r") as file:
                for line in file:
                    command = line.strip()
                    if command:
                        cli.execute_command(command)
        except FileNotFoundError:
            print(f"Error - File {input_file} not found")
    else:
        while True:
            try:
                command = input("# ").strip()
                if command:
                    cli.execute_command(command)
            except EOFError:
                print("Finished!")
                break
