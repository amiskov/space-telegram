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

Also, add your Telegram API key if you plan to use the bot functionality.

Install deps:

```sh
poetry install
```

## Run
All pics will be saved into `./images` directory (which will be created if not exists).

### SpaceX
Fetch pics of the SapceX launch by its ID:

```sh
# Launch ID specified
poetry run python fetch_spacex_images.py 5eb87d47ffd86e000604b38a

# No Launch ID specified, latest launch is used by default
poetry run python fetch_spacex_images.py
```

Some launches don't have pics, so there may be empty results.

### NASA APOD
Fetch NASA Astronomy Pictures of the Day:

```sh
# Fetch 3 APOD pictures
poetry run python fetch_nasa_apod.py 3

# Fetch single APOD picture
poetry run python fetch_nasa_apod.py
```

### NASA EPIC
Fetch NASA Earth Polychromatic Imaging Camera pictures:

```sh
# Fetch 3 EPIC pictures
poetry run python fetch_nasa_epic.py 3

# Fetch single EPIC picture
poetry run python fetch_nasa_epic.py
```
