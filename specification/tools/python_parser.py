import json

class FloorParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)

    def parse_header(self):
        header = self.data.get('header')
        if not header:
            raise ValueError("Invalid file format: Missing header.")
        self.version = header.get('version')
        self.creation_date = header.get('creation_date')
        self.author = header.get('author')

    def parse_metadata(self):
        metadata = self.data.get('metadata')
        if not metadata:
            raise ValueError("Invalid file format: Missing metadata.")
        self.project_name = metadata.get('project_name')
        self.location = metadata.get('location')
        self.client_info = metadata.get('client_info')
        self.building_dimensions = metadata.get('building_dimensions')
        self.number_of_floors = metadata.get('number_of_floors')

    def parse_floors(self):
        self.floors = []
        for floor in self.data.get('floors', []):
            self.floors.append(self.parse_floor(floor))

    def parse_floor(self, floor_data):
        floor = {
            'floor_id': floor_data.get('floor_id'),
            'floor_outline': floor_data.get('floor_outline'),
            'rooms': [self.parse_room(room) for room in floor_data.get('rooms', [])]
        }
        return floor

    def parse_room(self, room_data):
        room = {
            'room_id': room_data.get('room_id'),
            'room_name': room_data.get('room_name'),
            'room_outline': room_data.get('room_outline'),
            'walls': [self.parse_wall(wall) for wall in room_data.get('walls', [])]
        }
        return room

    def parse_wall(self, wall_data):
        wall = {
            'wall_id': wall_data.get('wall_id'),
            'start_point': wall_data.get('start_point'),
            'end_point': wall_data.get('end_point'),
            'wall_height': wall_data.get('wall_height'),
            'wall_thickness': wall_data.get('wall_thickness')
        }
        return wall

    def parse_additional_metadata(self):
        self.additional_metadata = self.data.get('additional_metadata')

    def parse(self):
        self.read_file()
        self.parse_header()
        self.parse_metadata()
        self.parse_floors()
        self.parse_additional_metadata()

# Usage
parser = FloorParser('path/to/file.floor')
parser.parse()

# Access parsed data
print(parser.project_name)
print(parser.floors)
