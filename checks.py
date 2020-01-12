from urllib import parse
from dateutil.parser import parse as dateutilparse
from urllib3.exceptions import InsecureRequestWarning
import re, whois, requests, datetime
from constants import SHORTENING_SERVICES, IP_ADDR_REGEX


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


#
# Checks a URL to see if the host is specified as
#  an IP address or a host name
#
# Returns:
#   "IP addr"     if the host is specified as a dotted IP address
#                  e.g. 104.20.74.246
#   "DNS name"    if the host is specified as a domain name
#                  e.g. "machinelearningforkids.co.uk"
def checkAddressType(addr):
    segments = parse.urlparse(addr)
    if re.search(IP_ADDR_REGEX, segments.hostname):
        return "IP addr"
    else:
        return "DNS name"


#
# Checks the length of the provided URL
#
# Returns:
#   "<54 chars"   if the address is shorter than 54 characters
#   "is 54-75"    if the address is between 54 and 75 characters long
#   ">75 chars"   if the address is longer than 75 characters
def checkUrlLength(addr):
    length = len(addr)
    if length < 54:
        return "<54 chars"
    elif length <= 75:
        return "is 54-75"
    else:
        return ">75 chars"


#
# Checks if the address is using a known shortening service
#  e.g. tinyurl.com or bit.ly
#
# Returns:
#   "yes"         if the address is using a shortening service
#   "no"          if the address is not using a known service
def checkShortening(addr):
    segments = parse.urlparse(addr)
    if segments.hostname in SHORTENING_SERVICES:
        return "yes"
    else:
        return "no"


#
# Checks if the address includes an @ sign.
#
# Returns:
#   "yes"         if the address includes the @ symbol
#   "no"          if the address does not include @
def checkAtSign(addr):
    if "@" in addr:
        return "yes"
    else:
        return "no"


#
# Checks if if the address uses a standard port number for
#  web pages.
#
# Returns:
#   "standard"    if the address uses port 80 or port 443
#   "non-std"     if the address uses a custom, non-standard port
def checkPortNumber(addr):
    segments = parse.urlparse(addr)
    if segments.port is None or segments.port == 80 or segments.port == 443:
        return "standard"
    else:
        return "non-std"


#
# Checks the age of the domain name in the provided address.
#
# Returns:
#   "< 6 month"   if the domain was registered less than 6 months ago
#   "older"       if the domain registration is older than 6 months
def checkDomainAge(addr):
    try:
        registration = whois.whois(addr)
        created = registration.creation_date
        if created is not None:
            if isinstance(created, list):
                created = created[0]
            if isinstance(created, str):
                if created.startswith("before "):
                    created = created[7:]
                created = dateutilparse(created)
            if isinstance(created, datetime.date):
                age = (datetime.datetime.now() - created).days
                if age > 180:
                    return "older"
    except whois.parser.PywhoisError:
        pass
    return "< 6 month"


#
# Counts the number of redirects when the provided address is followed.
#
# Returns:
#   "<= 4"        if there are 4 or fewer redirects
#   "> 4"         if there are more than 4 redirects
def checkRedirects(addr):
    try:
        if len(requests.get(addr, allow_redirects=True, verify=False, timeout=10).history) <= 4:
            return "<= 4"
    except:
        pass
    return "> 4"


#
# Checks when the domain for the provided address is due to expire.
#
# Returns:
#   "expiring"    if the domain is due to expire in less than a year
#   "not"         if the domain has an expiration longer than a year
def checkDomainRegistration(addr):
    try:
        registration = whois.whois(addr)
        expiry = registration.expiration_date
        if expiry is not None:
            if isinstance(expiry, list):
                expiry = expiry[0]
            expiresin = (expiry - datetime.datetime.now()).days
            if expiresin >= 365:
                return "not"
    except whois.parser.PywhoisError:
        pass
    return "expiring"

