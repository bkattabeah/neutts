from neutts.neutts import NeuTTS, BACKBONE_LANGUAGE_MAP  # noqa

# Also expose the version for convenience
try:
    from neutts._version import __version__
except ImportError:
    __version__ = "unknown"

# Expose commonly used symbols at the package level for easier imports
# Note: NeuTTSError added here so callers can catch it without digging into submodules
try:
    from neutts.neutts import NeuTTSError
    __all__ = ["NeuTTS", "BACKBONE_LANGUAGE_MAP", "__version__", "NeuTTSError"]
except ImportError:
    # NeuTTSError may not exist in all versions; degrade gracefully
    __all__ = ["NeuTTS", "BACKBONE_LANGUAGE_MAP", "__version__"]

# Personal note: I find it handy to print the version on import during development.
# Uncomment the line below when debugging version mismatches across environments.
# print(f"[neutts] loaded version: {__version__}")
