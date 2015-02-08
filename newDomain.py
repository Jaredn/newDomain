#!/usr/bin/python

__author__ = "Brandon Bianchi"
__copyright__ = "2015 - Brandon Bianchi"
__version__ = "1.0"
__maintainer__ = "Brandon Bianchi"
__email__ = "brandon@brandonbianchi.com"
__status__ = "Production"

# Grab domain information, store values
domain = raw_input('Enter new domain name (no www): \n')
domain.rstrip('\n')

prefix, tld = domain.split('.')[-2:]
prefix.rstrip('\n')

# Print output for debug
print("\n")
print(domain, prefix, tld)
print("\n")

# Get IP information for DNS
ipWWW = raw_input('Enter www IP (I am 208.82.212.157: \n')
ipMail = raw_input('Enter mail IP (I am 208.82.212.157: \n')

# Print output for debug
print("\n")
print(ipWWW, ipMail)
print("\n")


