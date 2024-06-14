# Space Telegram

This project is about 5 scripts for fetching images from SpaceX, NASA EPIC, NASA APOD by using API of these services and manually or automatic posting images into telegram channel.

### How to install
#### NASA API key

For getting an api key you may need to visit [this](https://api.nasa.gov/)

Example of key (unusable):
```
hvwSPvHWQsRB8P24gD564EBbrpuc2DJLrKSD2E0l
```
After getting a key you may need to create a .env file and put this key like this:

![image](https://github.com/e13q/WA_lesson4/assets/110967581/29e53380-1e88-4ad4-a61b-91234c9d1642)


#### Telegram Bot
[How to create a bot and get access token](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

Example of token (unusable):
```
3871579594:BBE2p_C131bghARhYe7-qLsvnA2LqZRQT8V
```
After getting a key you may need to create a .env file and put this key like this:

![image](https://github.com/e13q/WA_lesson4/assets/110967581/20aea039-5294-4f30-8db1-cdf8321ea40e)

Also you may need to put your channel link into .env file like this:

![image](https://github.com/e13q/WA_lesson4/assets/110967581/aeb5f422-7dce-480b-a4c5-a08764b764f3)

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### About and how to use
All images will be stored by default in subdirectory /images/ of project. 

You can change this in save_images_from_urls.py by changing DIR_PATH.

#### fetch_spacex_images.py
Download images from last or specific SpaceX launch.

For last launch just run this script.
Example:
```
py fetch_spacex_images.py
```

For specific launch you may need to get an id of launch from [API](https://api.spacexdata.com/v5/launches/).

Example of id:
```
5eb87ce5ffd86e000604b339
```

Example of running script for id=5eb87ce5ffd86e000604b339:
```
py fetch_spacex_images.py 5eb87ce5ffd86e000604b339
```

#### fetch_nasa_apod_images.py
Download some count (which you entered) of images from NASA APOD.

Example of running script to fetch 50 images:
```
py fetch_nasa_apod_images.py 50
```

#### fetch_nasa_epic_images.py
Download some count (which you entered) of images from NASA EPIC.

Example of running script to fetch 25 images:
```
py fetch_nasa_epic_images.py 25
```

### post_image_in_tg_channel.py
Post specific or random image in telegram channel.

Example of running script for posting random image:
```
py post_image_in_tg_channel.py 
```

Example of running script for posting specific image by name from /images/ local subdirectory of this project:
```
py post_image_in_tg_channel.py image.jpg
```

### post_all_images_in_tg_channel.py
Post images in telegram channel with frequency you may choose (in seconds).
Example of running script with default frequency (4 hours):
```
py post_all_images_in_tg_channel.py 
```

Example of running script with default frequency (1 hours):
```
py post_all_images_in_tg_channel.py 3600
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
