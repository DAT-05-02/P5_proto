import pandas as pd

from core import log
from core.data.fetch import fetch_images, setup


if __name__ == "__main__":
    df = setup("leopidotera-dk/multimedia.txt", "leopidotera-dk.csv")
    #
    # Uncomment below depending on how many images you want to download
    #
    df = df[10000:10101]
    fetch_images(df, "identifier")