from typing import List
from pathlib import Path
from tqdm import tqdm

from gefxmlreader import XmlBorehole

SOURCE_DIR = "./testdata"
OUTPUT_DIR = "./testdata"


def case_insensitive_glob(filepath: str, fileextension: str) -> List[Path]:
    """Find files in given path with given file extension (case insensitive)

    Arguments:
        filepath (str): path to files
        fileextension (str): file extension to use as a filter (example .gef or .csv)

    Returns:
        List(str): list of files
    """
    p = Path(filepath)
    result = []
    for filename in p.glob("**/*"):
        if str(filename.suffix).lower() == fileextension.lower():
            result.append(filename.absolute())
    return result


def main():
    xmlfiles = case_insensitive_glob(SOURCE_DIR, ".xml")
    for f in tqdm(xmlfiles):
        fname = f"{Path(f).stem}.gef"
        borehole = XmlBorehole()
        borehole.load_xml(f)
        borehole.to_gef(Path(OUTPUT_DIR) / fname)


if __name__ == "__main__":
    main()
