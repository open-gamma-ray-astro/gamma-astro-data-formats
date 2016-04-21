"""This is a class representing an data specification"""

from pathlib import Path

all = ['DataFormatSpec']


class DataFormatSpec(object):
    def __init__(self, spec):
        self.spec = spec

    @classmethod
    def read_yaml(cls, filename):
        """Read specification from YAML file"""
        import yaml
        specfile = Path(filename)
        with specfile.open('r') as fh:
            spec = yaml.safe_load(fh)
        return cls(spec)

    def to_rst(self, key):
        """Create RST code for the docs

        Parameters
        ----------
        key : str {columns_required, columns_optional, header_required, header_optional}
        """
        entries = self.spec[key]
        ss = ''
        for e in entries:
            val = '* ``{name}`` type: {ttype}'.format(name = e['name'], ttype=e['type'])
            extra_infos = [e[key] for key in e.keys() if key.startswith("extra")] 
            for extra in extra_infos:
                val += '\n    * {extra}'.format(**locals())
            ss += val

        return ss
            
    def write_rst(self, key, filename):
        filename = Path(filename)
        with open(str(filename), 'w') as fh:
            val = self.to_rst(key)
            fh.write(self.to_rst(key))
