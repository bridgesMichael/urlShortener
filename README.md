# urlShortener

This application allows you to 'encode' urls to shorter urls, and then 'decode' those urls if they were encoded and saved into the database prior. urls must be decoded to function properly, and only urls that are in your database will be decoded. 

To run:

  - Clone repo
  - Set up your virtual environment
  - pip install from 'requirements.txt'
  - create psql database called "urlshortener"
  - migrate database
  - run server "python manage.py runserver"

To shorten/encode:

  - Enter URL to shorten in "Encode URL"
  - Hit button and shortened URL will be generated and displayed

To decode/get full URL:
  - Enter shortened URL in "Decode URL"
  - Hit button and full URL will be retrieved and displayed
