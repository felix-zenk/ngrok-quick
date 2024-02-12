from __future__ import annotations

import logging

from ngrok.ngrok import forward

from .config import generate_config

__all__ = [
    'main'
]

logger = logging.getLogger(__name__)


def main() -> None:
    proxy_config = generate_config()
    listener = forward(
        addr=proxy_config['forward-addr'],
        authtoken=proxy_config['ngrok-token'],
        domain=proxy_config.get('ngrok-domain'),
    )

    logger.info('Listener is running at: %s', listener.url())
    return
