from django.shortcuts import render, render_to_response
import requests

def jsonResponse(request):
    r = requests.get(url='https://s3.ap-south-1.amazonaws.com/ss-local-files/products.json')
    jsonDict = r.json()
    productDict = jsonDict["products"]

    # for productCode in jsonDict["products"]:
    #     print("ProductCode: ", productCode)
    #     for key, value in jsonDict["products"][productCode].items():
    #         print (key, " : ", value)

    return render(request, "index.html", {'dictionary': productDict})
    