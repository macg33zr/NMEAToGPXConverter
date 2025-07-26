#
# Some utilities
#
import os
import fnmatch
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from ipyfilechooser import FileChooser

# Get a directory or file path using a browsing UI
def browse_for_path(path, only_directories = True):
    # Show a dialog to browse for the path
    fdialog = FileChooser(
        path,
        title='<b>Browse to Recordings to Process</b>',
        show_hidden=False,
        select_default=True,
        use_dir_icons=True,
        show_only_dirs=only_directories
    )
    display(fdialog)

    # Return the file dialog. Browsed item is fdialog.selected
    return fdialog

# Find the list of files in a given path, sort by name
def find_and_sort_files_on_path(path):
    files = fnmatch.filter(os.listdir(path), "*.LOG")
    files.sort()
    print(files)
    return files

def nmea_to_decimal(coord, direction):
    """Convert NMEA coordinate format to decimal degrees."""
    degrees = int(float(coord) / 100)
    minutes = float(coord) - degrees * 100
    decimal = degrees + minutes / 60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def convert_nmea_to_gpx(input_file_path):
    """Convert an NMEA file with GPRMC sentences to a GPX file."""
    input_path = Path(input_file_path)
    output_path = input_path.with_suffix('.gpx')

    with open(input_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    track_points = []
    for line in lines:
        if not line.startswith("$GPRMC"):
            continue
        parts = line.split(',')
        if len(parts) < 10 or parts[2] != 'A':
            continue
        try:
            time_str = parts[1]
            lat = nmea_to_decimal(parts[3], parts[4])
            lon = nmea_to_decimal(parts[5], parts[6])
            date_str = parts[9]
            dt = datetime.strptime(date_str + time_str.split('.')[0], "%d%m%y%H%M%S")
            track_points.append((dt.isoformat() + "Z", lat, lon))
        except (ValueError, IndexError):
            continue

    gpx = ET.Element('gpx', version="1.1", creator="NMEA to GPX Converter", xmlns="http://www.topografix.com/GPX/1/1")
    trk = ET.SubElement(gpx, 'trk')
    trkseg = ET.SubElement(trk, 'trkseg')

    for time, lat, lon in track_points:
        trkpt = ET.SubElement(trkseg, 'trkpt', lat=str(lat), lon=str(lon))
        ET.SubElement(trkpt, 'time').text = time

    tree = ET.ElementTree(gpx)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

    print(f"GPX file created: {output_path}")
    return str(output_path)

# Combine several GPX files into one track
import xml.etree.ElementTree as ET
from pathlib import Path

def combine_gpx_files(gpx_file_paths, output_path):
    """
    Combine multiple GPX files into one valid GPX file with a single <trk> and <trkseg>.
    """
    gpx_ns = "http://www.topografix.com/GPX/1/1"
    nsmap = {'': gpx_ns}
    ET.register_namespace('', gpx_ns)  # This ensures clean output without setting xmlns manually

    # Create new root GPX element (do NOT set 'xmlns' here)
    gpx = ET.Element('gpx', version="1.1", creator="GPX Combiner")
    trk = ET.SubElement(gpx, 'trk')
    trkseg = ET.SubElement(trk, 'trkseg')

    for file_path in gpx_file_paths:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Find all track points using the namespace
        for trkpt in root.findall(".//{%s}trkpt" % gpx_ns):
            new_trkpt = ET.Element('trkpt', attrib=trkpt.attrib)
            for child in trkpt:
                new_child = ET.Element(child.tag.split('}')[-1])  # Strip namespace
                new_child.text = child.text
                new_trkpt.append(new_child)
            trkseg.append(new_trkpt)

    ET.ElementTree(gpx).write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"✅ Combined GPX saved to: {output_path}")
    return str(output_path)