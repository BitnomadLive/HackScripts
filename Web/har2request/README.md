# har2request

A little script to turn HAR archives exported from ZAP or a web browser into a python script, that issues the same requests as specified in the HAR archive.

## Usage

har2request.py -i archive.har -o output.py 

Project is still work in progress

To export a HAR archive from your browser, just switch to the network tab of the developers tools, right click
and select "Save All As HAR"

![Firefox export](https://raw.githubusercontent.com/BitnomadLive/HackScripts/main/Web/har2request/images/firefox_har_export.jpg)