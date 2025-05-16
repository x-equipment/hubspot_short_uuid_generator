"""
generate_uuid.py

This script generates 8-character uppercase alphanumeric UUIDs. It is designed to be
compatible with both HubSpot custom code actions and command-line execution.

It utilizes the uuid and base64 libraries to generate a standard UUID, encode it
using base32 (which outputs uppercase alphanumeric characters), and truncate
the result to 8 characters.

Usage:
    - In HubSpot: Paste the code into a custom code action in a workflow.
      Ensure the "Outputs" are configured to include "short_uuid".
    - Command-line: Run the script directly using `python generate_uuid.py` or
      `./generate_uuid.py` after making it executable.

Output:
    - In HubSpot: The generated UUID is returned as an output property named "short_uuid".
    - Command-line: The generated UUID is printed to the console.
"""

import uuid
import base64
import sys

def generate_short_uuid():
    """
    Generates an 8-character uppercase alphanumeric UUID.

    Returns:
        str: The generated 8-character UUID.
    """
    standard_uuid = uuid.uuid4()
    short_uuid = base64.b32encode(standard_uuid.bytes).decode('utf-8')[:8]
    return short_uuid

def main(event=None, callback=None):
    """
    Main function to handle both HubSpot and command-line execution.

    Args:
        event (dict, optional): The event data from HubSpot.
        callback (function, optional): The callback function to return results to HubSpot.
    """
    try:
        short_uuid = generate_short_uuid()

        if event:  # HubSpot execution
            return({"outputFields": {"short_uuid": short_uuid}})
        else:  # Command-line execution
            print(short_uuid)

    except Exception as e:
        if callback:
            callback({"error": {"message": str(e)}})
        else:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    if "hubspotHandler.py" in sys.argv[0]:
        main(event={})
    else:
        main()