from checks import checkAddressType, checkUrlLength, checkShortening, checkAtSign, checkPortNumber, checkDomainAge, checkRedirects, checkDomainRegistration
from mlforkidsnumbers import MLforKidsNumbers

project = None

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

    addr_data = {
        "address type" : address_type,
        "url length" : url_length,
        "shortening" : shortening,
        "includes @" : includes_at,
        "port number" : port_number,
        "domain age" : domain_age,
        "redirects" : redirects,
        "domain reg" : domain_age,
    }

    if project is not None:
        predictions = project.classify(addr_data)
        prediction = predictions[0]
        print ("Prediction: %s is a %s link (%d%% confidence)" % (addr, prediction["class_name"], prediction["confidence"]))

    print ("")


checkUrl("https://machinelearningforkids.co.uk/help")
checkUrl("https://www.bbc.co.uk")

checkUrl("https://en.wikipedia.org/wiki/Machine_learning")
checkUrl("https://91.198.174.192/wiki/Machine_learning")

checkUrl("https://mickey@bit.ly/35Jnlf8")

checkUrl("https://login.bankofamerica.com@www.josueizagirre.com/wp-content/cache/login.bankofamerica.com.uplogad/update.html")
checkUrl("http://flinxdeicdccc.com/2612aa892d962d6f8056b195ca6e550d/tnFBsV27sc3kIMJg0Z8snqenramMHIXz.php?country=US-United%20States&lang=en")
