from jsonpath_ng import jsonpath, parse
from robot.api.deco import keyword
from robot.utils.robotpath import abspath
from JSONLibrary import JSONLibrary
import json

class APILibrary:

    @keyword("Build Request Data")
    def build_request_data(self, example_path, key_mapping_path, default_path=None, **request_data):
        #load all the json files
        example_obj = self._convert_file_to_obj(example_path)
        mapping_obj = self._convert_file_to_obj(key_mapping_path)
        default_obj = self._convert_file_to_obj(default_path) if default_path != None else None
        
        request_payload = example_obj

        for key, value in default_obj.items():
            if key in mapping_obj:
                request_payload = self._update_example_payload(mapping_obj[key], value, request_payload)
        
        for key, value in request_data.items():
            if key in mapping_obj:
                request_payload = self._update_example_payload(mapping_obj[key], value, request_payload)
        
        return request_payload
    
    @keyword("Get Values From Response")
    def get_values_from_response(self, response, key_mapping_path, key):
        mapping_obj = self._convert_file_to_obj(key_mapping_path)
        content_obj = json.loads(response.content.decode('utf-8'))
        if key in mapping_obj:
            jsonlibrary = JSONLibrary()
            return jsonlibrary.get_value_from_json(content_obj, mapping_obj[key])

    @keyword("Get Value From Response")
    def get_value_from_response(self, response, key_mapping_path, key, index=0):
        return (self.get_values_from_response(response, key_mapping_path, key))[index]
    
    def _convert_file_to_obj(self, file_path):
        with open(file_path, 'r') as f1:
            return json.load(f1)

    def _update_example_payload(self, json_path, new_value, example_obj):
        jsonpath_expr = parse(json_path)
        jsonpath_expr.find(example_obj)
        jsonpath_expr.update(example_obj,new_value)
        return example_obj

# if __name__ == "__main__":
#     example_path = os.path.join(abspath('.'),'tests','Example','example.json')
#     key_mapping_path = os.path.join(abspath('.'),'tests','Mapping','mapping.json')
#     default_path = os.path.join(abspath('.'),'tests','Defaults','defaults.json')
#     library = AutoAPILibrary()
#     request_data = library.build_request_data(example_path, key_mapping_path, default_path)
