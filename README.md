# VizAR Client for WiFi Tags

Bridge data between WiFi tags and VizAR server.

## Installation

This code is tested with Python 3.12 but should work with any relatively recent
Python 3 distribution.

Required Python packages:

- requests

```bash
sudo apt-get install -y python3-requests
```

## Running the Node

We are using several environment variables to configure the node.
The default values are shown below.

```bash
VIZAR_SERVER=http://localhost:5000
VIZAR_LOCATION="WiFi Tag Testing"
VIZAR_TAG_PATTERN="wifi-tag-*"
```

The VIZAR_SERVER variable needs to be set to a valid server URL. We may use
different server URLs during testing and deployment.

The VIZAR_LOCATION variable can be set to a UUID or location name. The code
will ensure that the location exists on the server. One can use different
locations for testing different maps.

The VIZAR_TAG_PATTERN is the pattern with simple wildcard support for naming
WiFi tag features on the server. Since the location map may have a number of
different feature markers, we want to filter only the ones pertaining to
WiFi tags.

The example code finds WiFi tag features and enables one at a time as if a
person were moving from one to the next in a sequence. When a feature is
enabled, it will be visible on the map and in AR headsets, and when it is
disabled, it will be hidden.

```bash
python3 example.py
```
