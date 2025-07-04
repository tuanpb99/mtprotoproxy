PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

# Interval for datacenter info refresh in seconds
# DC_INFO_UPDATE_PERIOD = 24*60*60

# maximum count of Telegram connections in the pool. Reducing this value may
# help when running the proxy for a small number of users.
MAX_CONNS_IN_POOL = 64

# Interval for testing Telegram middle proxies in seconds
# ACTIVE_PROXY_REFRESH_PERIOD = 5*60

# Interval for printing currently connected IPs in seconds
# CONNECTED_IP_PRINT_PERIOD = 5*60

