import dataclasses
import shutil

import hurry.filesize


@dataclasses.dataclass
class DriveSpace:
    path: str
    total: str
    used: str
    free: str
    free_perc: str


def get_drive_space(path: str) -> DriveSpace:
    total, used, free = shutil.disk_usage(path)

    return DriveSpace(path,
                      hurry.filesize.size(total),
                      hurry.filesize.size(used),
                      hurry.filesize.size(free),
                      f"{(free / total) * 100:.0f}%")
