from lm_datasets.datasets.base import Availability, GB, License
from lm_datasets.datasets.hf_dataset import HFDataset

class WuraCorpus(HFDataset):
    """
    OVERLAP_WITH mc4
    """
    DATASET_ID = "wura"

    TITLE = "WURA"
    DESCRIPTION = (
        """WURA is a document-level dataset covering 16 African Languages and
        4 high-resource languages widely spoken in Africa (English, French,
        Arabic and Portuguese). This dataset was created by auditing mC4 and
        crawling additional verified news sources. It was first used to train
        AfriTeVa V2."""
    )

    HOMEPAGE = "https://huggingface.co/datasets/castorini/wura"
    LICENSE = License(
        name="Apache License Version 2.0",
        url="http://www.apache.org/licenses/LICENSE-2.0"
    )
    AVAILIBILITY = Availability.DIRECT_DOWNLOAD

    LANGUAGES = ["en", "fr", "pt", "af", "am", "ha", "ig", "rw", "mg", "ny",
    "om", "sn", "sn","so", "st", "swa", "ti", "xh", "yo", "zu"]

    HF_DATASET_ID = "castorini/wura"
    HF_DATASET_CONFIGS = ["afr", "amh", "arz", "eng", "fra", "hau", "ibo", "kin", "mlg", "nya", "orm",
     "por", "sna", "som", "sot", "swa", "tir", "xho", "yor", "zul"]
    HF_DATASET_SPLIT = ["train","validation"]
    HAS_OVERLAP_WITH = "mC4"

    keep_columns = True
    text_column_name = "content"