import yaml
import os
import stat

from pathlib import Path
from dataformatspec import DataFormatSpec


specfile = Path('event_spec.yaml')
event_cols_required = Path('events_columns_required.inc')

spec = DataFormatSpec.read_yaml(specfile)
spec.write_rst('columns_required', event_cols_required)


st = os.stat(str(event_cols_required))
os.chmod(str(event_cols_required), st.st_mode | stat.S_IEXEC)
























