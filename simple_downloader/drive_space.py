import shutil

import hurry.filesize


def get_drive_space(path: str) -> dict[str, str]:
    total, used, free = shutil.disk_usage(path)

    return {
        'path': path,
        'total': hurry.filesize.size(total),
        'used': hurry.filesize.size(used),
        'free': hurry.filesize.size(free),
        'free_perc': f"{(free / total) * 100:.0f}%"
    }
