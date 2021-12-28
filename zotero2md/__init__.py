from pathlib import Path

__version__ = "0.0.1"

ROOT_DIR: Path = Path(__file__).parent
TOP_DIR: Path = ROOT_DIR.parent

default_params = {
    "convertTagsToInternalLinks": True,
    "doNotConvertFollowingTagsToLink": [],
    "includeHighlightDate": True,
    "hideHighlightDateInPreview": False,
}
