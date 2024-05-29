# Usage of .floor Files

## Introduction

The .floor file format is a JSON-based format designed to standardize architectural floor plan data. This document provides instructions on how to use and work with .floor files.

## Creating a .floor File

1. **Define the File Structure**:
   Follow the specification to define the structure of your .floor file. Refer to [floor_format.md](/specification/floor_format.md) for details.

2. **Populate the Data**:
   Populate the .floor file with relevant data such as floor outlines, room data, and additional metadata.

### Example Structure

```json
{
  "version": "1.0",
  "creation_date": "2024-05-29",
  "author": "John Doe",
  "metadata": {
    "project_name": "Custom House Project",
    "location": "123 Main St, Anytown, USA",
    ...
  },
  ...
}
```

## Tools for Working with .floor Files

### Python Parser

Use the provided Python parser to read and manipulate .floor files.

**Installation:**

1. Clone the repository:
  ```bash
  git clone https://github.com/your-organization/floor-specification.git
  cd floor-specification
  ```

2.	Use the parser:
  ```python
  from tools.python_parser import FloorParser
  
  parser = FloorParser('path/to/file.floor')
  parser.parse()
  
  # Access parsed data
  print(parser.project_name)
  print(parser.floors)
  ```

### Blender Add-on

Import .floor files into Blender using the custom add-on.

**Installation:**

1.	Download the add-on from the releases page.
2.	Open Blender and go to Edit > Preferences > Add-ons.
3.	Click Install... and select the downloaded ZIP file.
4.	Enable the add-on from the list.


**Usage:**

1.	Go to File > Import > .floor File.
2.	Select your .floor file to import.

## Best Practices

•	Validate Your Files: Use the Floor File Validator tool to ensure your .floor files are correctly formatted.
•	Keep Files Updated: Always use the latest version of the .floor specification.
•	Contribute: If you find bugs or have suggestions, consider contributing to the project.

For more details, refer to the [full documentation](specification/floor_format.md).
