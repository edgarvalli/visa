import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "aqzna2wzfcdfbtn6vpy8sr954s4uzc",
    "user": "u6tpsyrrgy1wnoryb9o4sgyn4dnmev",
    "message": "hello world",
    "title": "Test01111",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()