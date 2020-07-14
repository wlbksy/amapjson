import json


class Geojson:
    def __init__(self):
        self.result = {
            'type': 'FeatureCollection',
            'features': []
        }
        self.empty = True

    def add_feature(self, feature):
        if feature is not None:
            self.result['features'].append(feature.toGeojson())
            self.empty = False

    def toJSON(self, f):
        if f is None:
            exit('file is not open.')
        if self.empty:
            return None
        return json.dump(self.result, f)
