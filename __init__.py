from neutts.neutts import NeuTTS, BACKBONE_LANGUAGE_MAP  # noqa

# Also expose the version for convenience
try:
    from neutts._version import __version__
except ImportError:
    __version__ = "unknown"
