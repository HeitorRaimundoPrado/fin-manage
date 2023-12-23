import sys 
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from api import create_app
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='My Flask App')
    parser.add_argument(dest='config_name', default='development', help='Environment: development, production, testing')
    return parser.parse_args()


def main():
    args = parse_args()
    app = create_app(config_name=args.config_name.lower())

    valid_envs = ['development', 'production']
    
    if args.config_name.lower() not in valid_envs:
        print(f'Invalid environment. Please use one of: {", ".join(valid_envs)}')
        
    app.run()

if __name__ == '__main__':
    main()

