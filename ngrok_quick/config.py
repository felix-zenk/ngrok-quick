import os
from typing import TypedDict, NotRequired

Config = TypedDict('Config', {
    'ngrok-token': str,
    'ngrok-domain': NotRequired[str],
    'forward-addr': str,
})
"""The configuration dictionary type."""


def generate_config() -> Config:
    """Generate a configuration dictionary.

    Generate a configuration dictionary from the following environment variables:

        NGROK_AUTHTOKEN: The ngrok authtoken.
        NGROK_DOMAIN: (optional) The domain to use with ngrok.
        FORWARD_ADDR: The address to forward to.

    Raises:
        ValueError: If any of the required environment variables are not set.
    """
    for var_name in ('NGROK_AUTHTOKEN', 'FORWARD_ADDR'):
        if not os.getenv(var_name):
            raise ValueError(f"Environment variable {var_name} is not set!")

    config = {
        'ngrok-token': os.environ['NGROK_AUTHTOKEN'],
        'forward-addr': os.environ['FORWARD_ADDR'],
    }
    if 'NGROK_DOMAIN' in os.environ:
        config['ngrok-domain'] = os.environ['NGROK_DOMAIN']
    return config
