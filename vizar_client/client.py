import fnmatch
import os
import uuid

import requests

from .server_resource import ServerResource


class VizarClient:
    def __init__(self, server: str, location_id: str):
        """
        Helper client for communicating with VizAR server.

        server: base URL for the server, e.g. "https://example.org"
        location_id: location UUId or name, in which case, the name is assumed to be unique
        """
        self.server = server
        self.location_id = location_id

        self.location = ServerResource(f"{server}/locations", location_id)

    def get_matching_features(self, pattern: str = "*"):
        """
        Get list of features matching a string pattern.

        This supports simple wildcard matching, e.g. "wifi-tag-*".
        """
        url = f"{self.location.url}/features"
        res = requests.get(url)

        features = res.json()
        results = []
        for feature in features:
            if fnmatch.fnmatch(feature['name'], pattern):
                results.append(feature)

        return results

    def set_feature_enabled(self, feature_id: int, enabled: bool):
        """
        Set the enabled flag on one feature.
        """
        url = f"{self.location.url}/features/{feature_id}"
        data = dict(enabled=enabled)
        res = requests.patch(url, json=data)
        return res.json()
