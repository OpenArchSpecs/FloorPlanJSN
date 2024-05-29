# .floor File Format Specification

## Overview

The .floor file format is a JSON-based format designed to standardize the representation of architectural floor plan data. This format aims to facilitate easy integration with various tools and applications, promoting interoperability and efficiency in architectural projects.

## Table of Contents

- [File Structure](#file-structure)
- [Header](#header)
- [Metadata](#metadata)
- [Floor Data](#floor-data)
- [Room Data](#room-data)
- [Wall Data](#wall-data)
- [Additional Metadata](#additional-metadata)
- [Example .floor File](#example-floor-file)
- [Validation](#validation)

## File Structure

The .floor file format is composed of several key sections:

1. **Header**
2. **Metadata**
3. **Floor Data**
4. **Room Data**
5. **Wall Data**
6. **Additional Metadata**

### Header

The header contains general information about the file.

- **version**: Specifies the format version.
- **creation_date**: The date the file was created.
- **author**: The author of the file.

```json
{
  "version": "1.0",
  "creation_date": "2024-05-29",
  "author": "John Doe"
}
```

### Metadata

Metadata includes project-specific information.

- **project_name**: The name of the project.
- **location**: The location of the project.
- **client_info**: Information about the client.
- **building_dimensions**: Overall dimensions of the building (length, width, height).
- **number_of_floors**: The total number of floors in the building.

```json
{
  "metadata": {
    "project_name": "Custom House Project",
    "location": "123 Main St, Anytown, USA",
    "client_info": "Client Name",
    "building_dimensions": {
      "length": 30,
      "width": 20,
      "height": 10
    },
    "number_of_floors": 2
  }
}
```

### Floor Data

Each floor in the building is represented by an object containing:

- **floor_id**: Identifier for the floor (e.g., "Floor 1").
- **floor_outline**: An array of coordinates defining the floor's outline.

```json
{
  "floors": [
    {
      "floor_id": "Floor 1",
      "floor_outline": [
        {"x": 0, "y": 0},
        {"x": 30, "y": 0},
        {"x": 30, "y": 20},
        {"x": 0, "y": 20}
      ]
    }
  ]
}
```

### Room Data

Rooms are nested within floors and contain:

- **room_id**: Identifier for the room (e.g., "Room 101").
- **room_name**: Name of the room (e.g., "Living Room").
- **room_outline**: An array of coordinates defining the room's outline.
- **walls**: An array of wall objects within the room.

```json
{
  "rooms": [
    {
      "room_id": "Room 101",
      "room_name": "Living Room",
      "room_outline": [
        {"x": 0, "y": 0},
        {"x": 15, "y": 0},
        {"x": 15, "y": 10},
        {"x": 0, "y": 10}
      ],
      "walls": [
        {
          "wall_id": "Wall 101",
          "start_point": {"x": 0, "y": 0, "z": 0},
          "end_point": {"x": 15, "y": 0, "z": 0},
          "wall_height": 10,
          "wall_thickness": 0.5
        }
      ]
    }
  ]
}
```

### Wall Data

Walls are described within rooms and include:

- **wall_id**: Identifier for the wall.
- **start_point**: The starting coordinate of the wall.
- **end_point**: The ending coordinate of the wall.
- **wall_height**: The height of the wall.
- **wall_thickness**: The thickness of the wall.

```json
{
  "walls": [
    {
      "wall_id": "Wall 101",
      "start_point": {"x": 0, "y": 0, "z": 0},
      "end_point": {"x": 15, "y": 0, "z": 0},
      "wall_height": 10,
      "wall_thickness": 0.5
    }
  ]
}
```

### Additional Metadata

Additional metadata can include various other attributes like materials, electrical outlets, windows, and doors.

```json
{
  "additional_metadata": {
    "materials": "Brick",
    "electrical_outlets": 5,
    "windows": 4,
    "doors": 2
  }
}
```

## Example .floor File

```json
{
  "version": "1.0",
  "creation_date": "2024-05-29",
  "author": "John Doe",
  "metadata": {
    "project_name": "Custom House Project",
    "location": "123 Main St, Anytown, USA",
    "client_info": "Client Name",
    "building_dimensions": {
      "length": 30,
      "width": 20,
      "height": 10
    },
    "number_of_floors": 2
  },
  "floors": [
    {
      "floor_id": "Floor 1",
      "floor_outline": [
        {"x": 0, "y": 0},
        {"x": 30, "y": 0},
        {"x": 30, "y": 20},
        {"x": 0, "y": 20}
      ],
      "rooms": [
        {
          "room_id": "Room 101",
          "room_name": "Living Room",
          "room_outline": [
            {"x": 0, "y": 0},
            {"x": 15, "y": 0},
            {"x": 15, "y": 10},
            {"x": 0, "y": 10}
          ],
          "walls": [
            {
              "wall_id": "Wall 101",
              "start_point": {"x": 0, "y": 0, "z": 0},
              "end_point": {"x": 15, "y": 0, "z": 0},
              "wall_height": 10,
              "wall_thickness": 0.5
            }
          ]
        }
      ]
    }
  ],
  "additional_metadata": {
    "materials": "Brick",
    "electrical_outlets": 5,
    "windows": 4,
    "doors": 2
  }
}
```

## Validation

To ensure your .floor file adheres to the specification, you can use the provided Floor File Validator tool. Refer to the [other_tools.md](../tools/other_tools.md) for more information on how to install and use the validator.

---

This document outlines the complete specification for the .floor file format. For any questions or contributions, please refer to our [contributing guidelines](../docs/contributing.md).
