import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"arches_keep_app"),
        "arches_keep_app.urls",
        name="arches_keep_app",
    ),
)
