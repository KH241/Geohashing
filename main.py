import webbrowser
import config
from Generator import Generator


def main():
    generator = Generator()
    latitude, longitude = generator.getCoordinates()

    webbrowser.open(config.api_request.format(latitude, longitude))


if __name__ == '__main__':
    main()
