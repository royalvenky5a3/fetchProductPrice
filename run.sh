#!/bin/bash
productUrl="https://www.amazon.in/Sony-WH-1000XM3-Wireless-Cancellation-Headphones/dp/B07HZ8JWCL/ref=sr_1_4?crid=1G81YUHKSWBTS&keywords=sony+wx1000xm3&qid=1651778771&sprefix=sony+wx%2Caps%2C221&sr=8-4"
senderEmail="venm5a3.a@gmail.com"
senderPassword="Coder@5a3"
receiverEmail="venm5a3@gmail.com"
python main.py "$productUrl" "$senderEmail" "$senderPassword" "$receiverEmail"
