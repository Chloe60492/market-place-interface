from repository import MarketplaceRepository
import re
import argparse


class CLIHandler:
    def __init__(self):
        self.repo = MarketplaceRepository()
        

    def execute_command(self, command: str):
        tokens = command.split(" ", 1)
        action = tokens[0]

        if action == "REGISTER":
            username = tokens[1].strip()
            print(self.repo.add_user(username))

        elif action == "CREATE_LISTING":
            # Use regular expression to extract username and quoted fields (title, description, price, category)
            match = re.match(r"CREATE_LISTING (\S+) '([^']+)' '([^']+)' (\d+) '([^']+)'", command)
            
            if match:
                username = match.group(1)  # The username
                title = match.group(2)     # The title (in quotes)
                description = match.group(3)  # The description (in quotes)
                price = int(match.group(4))  # The price
                category = match.group(5)  # The category (in quotes)
                
                # Now we can use these variables to call the repository method
                print(self.repo.add_listing(username, title, description, price, category))
            else:
                print("Error - Invalid CREATE_LISTING format")

        elif action == "DELETE_LISTING":
            # DELETE_LISTING command expects: DELETE_LISTING <username> <listing_id>
            parts = tokens[1].split()
            if len(parts) == 2:
                username = parts[0]
                listing_id = int(parts[1])
                print(self.repo.delete_listing(username, listing_id))
            else:
                print("Error - Invalid DELETE_LISTING format")

        elif action == "GET_LISTING":
            # GET_LISTING command expects: GET_LISTING <username> <listing_id>
            parts = tokens[1].split()
            if len(parts) == 2:
                username = parts[0]
                listing_id = int(parts[1])
                print(self.repo.get_listing(username, listing_id))
            else:
                print("Error - Invalid GET_LISTING format")

        elif action == "GET_CATEGORY":
            # GET_CATEGORY command expects: GET_CATEGORY <username> <category>
            parts = tokens[1].split()
            if len(parts) == 2:
                username = parts[0]
                category = re.search("[^']+",parts[1]).group()
    
                print(self.repo.get_listings_by_category(username, category))
            else:
                print("Error - Invalid GET_CATEGORY format")

        elif action == "GET_TOP_CATEGORY":
            # GET_TOP_CATEGORY command expects: GET_TOP_CATEGORY <username>
            username = tokens[1].strip()
            print(self.repo.get_top_category(username))

        else:
            print("Error - Unknown command")

if __name__ == "__main__":
    cli = CLIHandler()
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    args = parser.parse_args()
    if args.file:
        input_file = args.file
        try:
            with open(input_file, "r") as file:
                for line in file:
                    command = line.strip()
                    if command:  # Only execute non-empty commands
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

