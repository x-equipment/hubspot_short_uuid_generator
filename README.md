# HubSpot Short UUID Generator

[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python->=3.6-blueviolet?style=flat-square)]()
[![Maintained](https://img.shields.io/badge/Maintained-Yes-green?style=flat-square)]()
[![Contributions](https://img.shields.io/badge/Contributions_welcome-Yes-blueviolet?style=flat-square)]()

This Python script generates 8-character uppercase alphanumeric UUIDs for use in HubSpot custom code actions and command-line execution. This allows for the creation of unique identifiers across HubSpot and other systems.

## Features

-   **Short UUID Generation:** Creates 8-character UUIDs in the format `[0-9A-Z]{8}`.
-   **HubSpot Custom Code Compatibility:** Can be executed within HubSpot workflows using custom code actions.
-   **Command-Line Compatibility:** Can be executed directly from the command line (Bash).
-   **Base32 Encoding:** Utilizes base32 encoding to ensure only uppercase alphanumeric characters are used.
-   **Error Handling:** Includes basic error handling for both HubSpot and command-line environments.

## Prerequisites

-   A HubSpot account (for HubSpot usage).
-   Python 3.6 or later.

## Installation

1.  **Clone the Repository (Optional):**

    ```bash
    git clone [https://github.com/x-equipment/hubspot_short_uuid_generator.git](https://github.com/x-equipment/hubspot_short_uuid_generator.git)
    cd hubspot_short_uuid_generator
    ```

2.  **No external dependencies:** The script relies on standard python libraries, and does not require a `requirements.txt` file.

## Usage

### HubSpot Custom Code

1.  In your HubSpot workflow, create a "Custom Code" action.
2.  Copy and paste the contents of `generate_short_uuid.py` into the code editor.
3.  In the "Outputs" section, add an output named `short_uuid`.
4.  Create a HubSpot property to store the generated UUID.
5.  Use a "Set property value" action to store the `short_uuid` output in your HubSpot property.
6.  Test and publish the workflow.

### Bash Execution

1.  Ensure you have Python 3 installed.
2.  Save the `generate_short_uuid.py` script.
3.  Run the script from your terminal:

    ```bash
    python generate_short_uuid.py
    ```

## Configuration

-   No configuration is required. The script uses standard libraries and performs the UUID generation directly.

## Error Handling

-   **HubSpot Custom Code:** Errors are logged to the HubSpot execution logs.
-   **Bash Execution:** Errors are printed to the console (stderr).

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the Apache 2.0 License.