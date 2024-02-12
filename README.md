ngrok-quick
===

Simple docker container to expose your local server to the internet quickly using ngrok.

---

## Usage

Use this container along the server you want to forward in docker compose:

```yaml
services:
  my-web-service:
    build:
      context: ./my-web-service
      dockerfile: Dockerfile
  ngrok-quick:
    image: ghcr.io/felix-zenk/ngrok-quick:latest
    environment:
      NGROK_AUTHTOKEN: your-auth-token
      # NGROK_DOMAIN: your-domain.ngrok.app  # optional set ngrok domain to use for forwarding
      FORWARD_ADDR: my-web-service:80
    restart: unless-stopped
```

`FORWARD_ADDR` can be in any format supported by the
[`ngrok.forward`](https://ngrok.github.io/ngrok-python/module.html#ngrok.forward) command. \
This includes `127.0.0.1`, `localhost:1234`, `http://localhost`, `https://localhost:443`, etc.

If `NGROK_DOMAIN` is not set, ngrok will use a random subdomain of `ngrok-free.app`.

Run `docker-compose up -d` and your local server will be exposed via ngrok. \
To get the public URL look at the logs of the container with `docker-compose logs ngrok-quick`
