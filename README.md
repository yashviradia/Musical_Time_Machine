# Musical_Time_Machine
Takes top 100 music from date in past to create a Spotify playlist.

## Table of contents
- [Overview](#overview)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview


### Screenshot
![img.png](images/spotify_image_1.png)

### Links
- Github Repository - [Musical_Time_Machine](https://github.com/yashviradia/Musical_Time_Machine)

## My process

### Built with
- Python
- Beautiful Soap
- Spotipy Module

### What I learned
- Read Spotipy Documentation
- Using try and except blocks
  ```
  try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
  except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")
  ```

### Useful resources
- [Stack Overflow](https://stackoverflow.com/)
- [Google](https://www.google.com/)

## Author
- Website - [Yash Viradia](http://yashviradia.tech/)
- Twitter - [@theyashviradia](https://twitter.com/theyashviradia)

## Acknowledgments
- LondonAppBrewery - [LondonAppBrewery](https://www.londonappbrewery.com/)
