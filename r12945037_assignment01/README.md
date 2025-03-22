# Marketplace CLI Application

This project provides a **Command-Line Interface (CLI)** application to simulate the functionality of a marketplace platform. It allows users to register, create listings, retrieve listings, and interact with the marketplace via commands.

## Features

- **REGISTER**: Allows a user to register on the marketplace.
- **CREATE_LISTING**: Allows a registered user to create a listing for an item.
- **GET_LISTING**: Retrieve a specific listing by ID.
- **DELETE_LISTING**: Allows a user to delete a listing they own.
- **GET_CATEGORY**: Retrieve all listings under a specific category.
- **GET_TOP_CATEGORY**: Get the category with the most listings.
  
## Prerequisites

- **Python 3.x** or higher
- **SQLite3** (which is embedded in Python standard library)

## Run the CLI application
To start the interactive command line interface:
```
python3 main.py
```

## Process Commands from a File
To execute a set of commands from a file:
```
python3 main.py --file input.txt
```

## Scripts Usage Instructions:
(Assume you have install Python3.10** or higher)

1. Make the scripts executable: `chmod +x build.sh run.sh`

2. To set up the environment:
    - Run the build.sh script to set up the virtual environment and install dependencies: `./build.sh`

3. To run the application:
    - Once the environment is set up, you can use the run.sh script to run the codebase: `./run.sh`
    - If you want to pass a file with commands to the application, use: `./run.sh --file input.txt`
