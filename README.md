# .floor File Format Specification

Welcome to the .floor file format project! The .floor file format is designed to standardize architectural floor plan data for easy integration with various tools and applications.

## Overview

The .floor file format is a JSON-based format that captures detailed information about a building's floor plans, including room outlines, wall data, and additional metadata.

## Table of Contents

- [File Structure](#file-structure)
- [Example .floor Files](#example-floor-files)
- [Tools](#tools)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## File Structure

The .floor file format consists of several key components:
- **Header:** Contains version, creation date, and author information.
- **Metadata:** Includes project name, location, client information, building dimensions, and number of floors.
- **Floor Data:** Contains floor identifier, floor outline, and room data.
- **Room Data:** Contains room identifier, room name, room outline, and wall data.
- **Wall Data:** Contains wall identifier, start and end points, wall height, and wall thickness.
- **Additional Metadata:** Includes materials, electrical outlets, windows, and doors.

For a detailed specification, refer to the [floor_format.md](specification/floor_format.md) file.

## Example .floor Files

Here are some example .floor files to help you get started:
- [Example 1](specification/examples/example1.floor)
- [Example 2](specification/examples/example2.floor)

## Tools

We provide several tools to help you work with .floor files:

### Python Parser

A [Python parser](/tools/python_parser.py) to read and manipulate .floor files.

```python
from tools.python_parser import FloorParser

parser = FloorParser('path/to/file.floor')
parser.parse()

# Access parsed data
print(parser.project_name)
print(parser.floors)
```

### Other Tools

- Floor File Validator
- Floor to SVG Converter

For more information, check out [other_tools.md](/tools/other_tools.md).

## Usage

To learn how to create and use .floor files, refer to the usage.md document. It provides detailed instructions and best practices for working with .floor files.

## Contributing

We welcome contributions from the community! Please read our [contributing.md](/docs/contributing.md) for guidelines on how to contribute to the project.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Getting Started

To get started, clone the repository and explore the provided tools and examples. Feel free to open issues or submit pull requests for any improvements or features you'd like to see.

Thank you for your interest in the .floor project!
