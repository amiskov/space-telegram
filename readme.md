# Space Pics from APIs
Resources are downloaded from:

- [SpaceX Launches](https://github.com/r-spacex/SpaceX-API)
- NASA's Astronomy Picture of the Day ([APOD](https://api.nasa.gov/#apod))
- NASA Earth Polychromatic Imaging Camera ([EPIC](https://api.nasa.gov/#epic))

## Install
Install dependencies via [Poetry](https://python-poetry.org):

```sh
poetry install
```

## Settings
All settings are kept in `.env` file. Create one from `.env.example`:

```sh
cp .env.example .env
```

You'll also need a [NASA API KEY](https://api.nasa.gov/#signUp). If you plan to use Telegram functionality, you'll also need its API KEY and chat ID.

## Usage
You can download space pictures or post them to your Telegram channel.

All pics will be saved into `IMAGES_DIR` (which will be created if not exists).

### Fetch SpaceX Launch Photos
Fetch pics of the SapceX launch by its ID:

```sh
# Launch ID specified
poetry run python fetch_spacex_images.py 5eb87d47ffd86e000604b38a

# No Launch ID specified, latest launch is used by default
poetry run python fetch_spacex_images.py
```

Some launches don't have pics, so there may be empty results.

### Fetch NASA APOD images
Fetch NASA Astronomy Pictures of the Day:

```sh
# Fetch 3 APOD pictures
poetry run python fetch_nasa_apod.py 3

# Fetch single APOD picture
poetry run python fetch_nasa_apod.py
```

### Fetch NASA EPIC images
Fetch NASA Earth Polychromatic Imaging Camera pictures:

```sh
# Fetch 3 EPIC pictures
poetry run python fetch_nasa_epic.py 3

# Fetch single EPIC picture
poetry run python fetch_nasa_epic.py
```

### Send Random Picture to Telegram Channel Once
Add your Tg Token and Chat ID to `.env`. Replace `POSTING_TIMEOUT_SEC` with the period you with to do periodical posting (in seconds).

Send random photo from `IMAGES_DIR` directory:

```sh
poetry run python tg_send_random_pic.py
```

### Send Random Picture to Telegram Channel Periodically
Run script to send random photos from `IMAGES_DIR` directory forever. It will shuffle photos if all are sent and start over again:

```sh
poetry run python tg_post_periodically.py
```
