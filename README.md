# Astro
This is a simple Python script that tracks the asteroids near the earth and display all the information about them.

![astro1-Screenshot 2023-07-07 172012](https://github.com/SinghIsWriting/astro/assets/122283853/73937e86-dd04-4c37-a899-a58e467fe522)


## Prerequisites
* Python interpreter
* Basic understanding of python programming concepts
* You will need NASA Open API key to run this script, to do the same you can visit https://api.nasa.gov/. Create your account and generate your own API Key.

## How to Run
1. Clone the repository or download the source code file.
2. git clone https://github.com/SinghIsWriting/astro.git
3. Open a terminal or command prompt.
4. Navigate to the directory where the source code file is located.
5. Install required python packages using following command:
6. pip3 install -r requirements.txt
7. Run the python program:
8. python3 main.py
9. Follow the prompts to enter the given options.

![astro2-Screenshot 2023-07-07 172305](https://github.com/SinghIsWriting/astro/assets/122283853/93bd8ae7-cdac-4915-874b-10e1ab1ed271)


10. The program will display the number of asteroids and details.

## Usage
1. The program prompts the user to enter the two options to see the asteroid details of the current day or in between a time interval. If you choose first options then extract the current date automaticall and proivdes to the requestin url.
2. It then requests to api.nasa.gov/ website using requests python library and scraps the data.
3. The program displays the found information about the asteroids.

## Contributing
Contributions to this repository are welcome. If you would like to improve code, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Test your changes thoroughly.
5. Commit your changes with a descriptive commit message.
6. Push your changes to your forked repository.
7. Create a pull request detailing your changes.
