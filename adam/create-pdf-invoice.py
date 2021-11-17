# import zlib
import demjson as json
bytes = b'{return: true}'
bytesString = str(bytes,'utf8')
obj =  json.decode(bytesString)
# billNo = 'cardn/1/211'
# data = bytes(billNo, 'utf8')
# crc = zlib.crc32(data)
# print(crc)
# # from jinja2 import Template
# # t = Template("Hello {{ something }}!")
# # h = t.render(something="World")
# # print(h)
# data = {
#     'product': lambda: 'Sony LED TV'
# }
# product = data['product']()
invoiceData = '''[
    {
        "acc_name": "Cash a/c shop",
        "address": "3A CHOWRINGEE PLACE KOLKATA 1ST FLOOR ROOM NO, 29",
        "bill_memo": "M",
        "bill_memo_id": 15,
        "cgst": 37.01,
        "companyInfo": {
            "addr1": "12 J.L.Nehru Road",
            "addr2": "http://capital-chowringhee.com",
            "comp_name": "Capital chowringhee Pvt Ltd.",
            "email": "capitalch@gmail.com",
            "free1": "Web site: http://capital-chowringhee.com",
            "free2": "For warranty and replacement please contact respective manufacturer companies.",
            "free3": "Materials will be delivered only after the cheque is cleared from our Bank.",
            "free4": "All disputes to be resolved in Kolkata jurisdiction only.",
            "gstin": "19AACCC5685L1Z3",
            "pan": "AACCC5685L",
            "phone": "8777399268, 9163055161, 9903177904",
            "pin": "700013"
        },
        "date": "2021-04-05",
        "email": null,
        "gstin": "19AAFFM1548Q1ZO",
        "id": 6,
        "igst": 0,
        "mobile": "8697443213",
        "name": "MAHESH TEXT TILES",
        "phone": null,
        "pin": "700013",
        "product": "CALCULATOR CASIO MJ120D",
        "products": [
            {
                "brand": "CASIO",
                "discount": 0,
                "hsn": null,
                "item": "CALCULATOR",
                "model": "MJ120D",
                "price": 411.23,
                "qty": 1,
                "spec": null
            }
        ],
        "ref_no": "GRAM/4/21",
        "roundoff": -0.25,
        "sgst": 37.01,
        "total_amt": 485,
        "type": "S"
    },
    {
        "acc_name": "Cash a/c shop",
        "address": "BASIRHAT",
        "bill_memo": "M",
        "bill_memo_id": 13,
        "cgst": 282.2,
        "companyInfo": {
            "addr1": "12 J.L.Nehru Road",
            "addr2": "http://capital-chowringhee.com",
            "comp_name": "Capital chowringhee Pvt Ltd.",
            "email": "capitalch@gmail.com",
            "free1": "Web site: http://capital-chowringhee.com",
            "free2": "For warranty and replacement please contact respective manufacturer companies.",
            "free3": "Materials will be delivered only after the cheque is cleared from our Bank.",
            "free4": "All disputes to be resolved in Kolkata jurisdiction only.",
            "gstin": "19AACCC5685L1Z3",
            "pan": "AACCC5685L",
            "phone": "8777399268, 9163055161, 9903177904",
            "pin": "700013"
        },
        "date": "2021-04-05",
        "email": null,
        "gstin": null,
        "id": 4,
        "igst": 0,
        "mobile": "7584084113",
        "name": "R. SEKH",
        "phone": null,
        "pin": "743456",
        "product": "UVFILTER HMC 67.0MM,M/CARD SANDISK 64GBEXTREMEPRO,CLEANINGKI PHOTRON 6IN1PRO",
        "products": [
            {
                "brand": "HMC",
                "discount": 0,
                "hsn": null,
                "item": "UVFILTER",
                "model": "67.0MM",
                "price": 1101.69,
                "qty": 1,
                "spec": null
            },
            {
                "brand": "SANDISK",
                "discount": 0,
                "hsn": null,
                "item": "M/CARD",
                "model": "64GBEXTREMEPRO",
                "price": 1610.17,
                "qty": 1,
                "spec": null
            },
            {
                "brand": "PHOTRON",
                "discount": 0,
                "hsn": null,
                "item": "CLEANINGKI",
                "model": "6IN1PRO",
                "price": 423.73,
                "qty": 1,
                "spec": null
            }
        ],
        "ref_no": "GRAM/2/21",
        "roundoff": 0.01,
        "sgst": 282.2,
        "total_amt": 3700,
        "type": "S"
    },
    {
        "acc_name": "Cash a/c shop",
        "address": "",
        "bill_memo": "M",
        "bill_memo_id": 12,
        "cgst": 45.9,
        "companyInfo": {
            "addr1": "12 J.L.Nehru Road",
            "addr2": "http://capital-chowringhee.com",
            "comp_name": "Capital chowringhee Pvt Ltd.",
            "email": "capitalch@gmail.com",
            "free1": "Web site: http://capital-chowringhee.com",
            "free2": "For warranty and replacement please contact respective manufacturer companies.",
            "free3": "Materials will be delivered only after the cheque is cleared from our Bank.",
            "free4": "All disputes to be resolved in Kolkata jurisdiction only.",
            "gstin": "19AACCC5685L1Z3",
            "pan": "AACCC5685L",
            "phone": "8777399268, 9163055161, 9903177904",
            "pin": "700013"
        },
        "date": "2021-04-05",
        "email": null,
        "gstin": null,
        "id": 3,
        "igst": 0,
        "mobile": "9874112999",
        "name": "DR GOUTAM DAS",
        "phone": null,
        "pin": null,
        "product": "CALCULATOR CASIO MJ12GST",
        "products": [
            {
                "brand": "CASIO",
                "discount": 0,
                "hsn": null,
                "item": "CALCULATOR",
                "model": "MJ12GST",
                "price": 327.88,
                "qty": 1,
                "spec": null
            }
        ],
        "ref_no": "GRAM/1/21",
        "roundoff": 0.32,
        "sgst": 45.9,
        "total_amt": 420,
        "type": "S"
    }
]'''
