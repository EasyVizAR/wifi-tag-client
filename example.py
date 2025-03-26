import os
import time

from vizar_client.client import VizarClient


VIZAR_SERVER = os.environ.get("VIZAR_SERVER", "http://localhost:5000")
VIZAR_LOCATION = os.environ.get("VIZAR_LOCATION", "WiFi Tag Testing")
VIZAR_TAG_PATTERN = os.environ.get("VIZAR_TAG_PATTERN", "wifi-tag-*")


if __name__ == "__main__":
    client = VizarClient(VIZAR_SERVER, VIZAR_LOCATION)

    features = client.get_matching_features(VIZAR_TAG_PATTERN)

    print("Found {} features:".format(len(features)))
    for feature in features:
        print("  {} (ID: {})".format(feature['name'], feature['id']))

        # Set all to inactive
        client.set_feature_enabled(feature['id'], False)

    print("Simulating detections at each of the tags...")
    for feature in features:
        time.sleep(1)
        print("Enable tag {}".format(feature['name']))
        client.set_feature_enabled(feature['id'], True)

        time.sleep(3)
        print("Disable tag {}".format(feature['name']))
        client.set_feature_enabled(feature['id'], False)
