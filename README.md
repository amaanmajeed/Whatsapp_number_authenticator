# WhatsApp Number Checker

A utility that checks if a phone number is formatted correctly to be used with the WhatsApp API, and generates a link to send automated messages on WhatsApp.

## Features
- Verifies phone number formatting: The script checks if the phone number follows the correct E.164 formatting (e.g., `+1234567890`).
- Outputs formatted number: If the number is not correctly formatted, the script outputs the correct version of the number, ready to be used with the WhatsApp API.
- Generates WhatsApp API link: The script takes an integer input and processes it to generate a link that can be used to send automated messages on WhatsApp.

## Requirements
- [Python 3](https://www.python.org/downloads/)

## Usage
1. Clone or download the repository.
2. Run the script, passing the phone number as an argument: `python whatsapp_number_checker.py +1234567890`
3. To generate the WhatsApp API link, pass an integer input to the script: `python whatsapp_number_checker.py 12345`

## Notes
- The script does not check if the phone number is actually a valid number. It only checks the formatting.

## License
This project is licensed under the [MIT License](LICENSE).
