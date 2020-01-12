from checks import checkAddressType, checkUrlLength, checkShortening, checkAtSign, checkPortNumber, checkDomainAge, checkRedirects, checkDomainRegistration
from mlforkids import classify

MLFORKIDS_API_KEY = None

def checkUrl(addr):
    address_type = checkAddressType(addr)
    url_length = checkUrlLength(addr)
    shortening = checkShortening(addr)
    includes_at = checkAtSign(addr)
    port_number = checkPortNumber(addr)
    domain_age = checkDomainAge(addr)
    redirects = checkRedirects(addr)
    domain_reg = checkDomainRegistration(addr)

    print (addr)
    print ("   address type :", address_type)
    print ("   url length   :", url_length)
    print ("   shortening   :", shortening)
    print ("   includes @   :", includes_at)
    print ("   port number  :", port_number)
    print ("   domain age   :", domain_age)
    print ("   redirects    :", redirects)
    print ("   domain reg   :", domain_reg)

    if MLFORKIDS_API_KEY is not None:
        addr_data = [ address_type, url_length, shortening, includes_at, port_number, domain_age, redirects, domain_reg ]
        prediction = classify(MLFORKIDS_API_KEY, addr_data)
        print ("Prediction: %s is a %s link (%d%% confidence)" % (addr, prediction["class_name"], prediction["confidence"]))

    print ("")


checkUrl("https://machinelearningforkids.co.uk/help")
checkUrl("https://www.bbc.co.uk")

checkUrl("https://en.wikipedia.org/wiki/Machine_learning")
checkUrl("https://91.198.174.192/wiki/Machine_learning")

checkUrl("https://mickey@bit.ly/35Jnlf8")

checkUrl("https://login.bankofamerica.com@www.josueizagirre.com/wp-content/cache/login.bankofamerica.com.uplogad/update.html")
checkUrl("http://flinxdeicdccc.com/2612aa892d962d6f8056b195ca6e550d/tnFBsV27sc3kIMJg0Z8snqenramMHIXz.php?country=US-United%20States&lang=en")
