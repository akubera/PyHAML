
from setuptools import Command


def validate_manifest(dist, attr, value):
    from distutils.errors import DistutilsSetupError
    try:
        Manifest.validate(value)
    except TypeError:
        msg = (f"{attr} should be a dict of mappings"
                "{'package.name': ('haml/path', 'html/path')}")
        raise DistutilsSetupError(msg)


class Manifest:

    def __init__(self, manifests):
        self.manifests = manifests

    @classmethod
    def validate(cls, manifests):
        if manifests is None:
            manifests = {}


class build_haml(Command):
    """
    Builds haml files
    """

    description = __doc__.strip()

    user_options = [
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


    def run(self):
        manifests = Manifest(tself.distribution.haml_manifests)
        print('manifests')
