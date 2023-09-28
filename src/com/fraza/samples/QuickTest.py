#!/anaconda3/bin/python

months = {
    1: "Jan",
    3: "Mar",
    "12": "December"
}
print(months.keys())
print(months.items())
print(months.get(3))

print(months.__contains__("12"))


dict = {
    "Total Bid Quantity": "-1",
    "Total Offer Quantity": "-1"
}
capture_data = False
capture_key = "none"
data = "Total Bid Quantity"
    
if dict.__contains__(data):
    capture_data = True
    capture_key = data
else:
    capture_data = False        
    capture_key = "none"
    
print(capture_data)
print(capture_key)

