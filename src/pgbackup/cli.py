from argparse import ArgumentParser, Action
known_drivers = ['local','s3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination= values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local' & 's3'")
        namespace.driver=driver.lower()
        namespace.destination=destination


def create_parser():
    parser=ArgumentParser(description='Create a backup of a PostgreSQL db')
    parser.add_argument('-url', '-u', help="URL of the PostgreSQL database to backup")
    parser.add_argument('--driver', nargs=2, action=DriverAction, required=True, help='How and where to store the backup')
    return parser
