# Space Pics from APIs
Resources are downloaded from:

- [SpaceX Launches](https://github.com/r-spacex/SpaceX-API)
- NASA's Astronomy Picture of the Day ([APOD](https://api.nasa.gov/#apod))
- NASA Earth Polychromatic Imaging Camera ([EPIC](https://api.nasa.gov/#epic))

## Install
Get your [NASA API KEY](https://api.nasa.gov/#signUp) and insert it into `.env` using `.env.example` as a template:

```sh
cp .env.example .env # and paste your secrets into `.env`
```

Install deps:

```sh
poetry install
```

## Run
TBD:

```sh
poetry python main.py
```

All pics will be saved into `./images` directory (will be created if not exists).

### SpaceX
```sh
# With Launch ID passed
poetry run python fetch_spacex_images.py 5eb87d47ffd86e000604b38a

# No Launch ID specified, latest launch is used by default
poetry run python fetch_spacex_images.py
```
