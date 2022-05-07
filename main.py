# Python script takes 3 arguments
#   1. List of product urls //TODO
#   2. senderEmail
#   3. senderPassword
#   4. receiverEmail
import sys

from util.emailUtil import sendEmail
from util.webScrap import getAmountFromAmazonProduct

if len(sys.argv) != 5:
    raise ValueError("Invalid argument length")
print(sys.argv)
amountBody = getAmountFromAmazonProduct(sys.argv[1])
sendEmail(amountBody, sys.argv[2], sys.argv[3], sys.argv[4])


