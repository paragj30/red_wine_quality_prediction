from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    '''
    This is en entity. It is a custom return type of the function using "dataclass". 
    Similar to the "confibox". This is inbuilt return type of the function.
    Below variables from config.yaml with its data type.
    '''
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path