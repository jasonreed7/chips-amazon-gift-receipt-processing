# importing required modules
import PyPDF2


def main():
    # creating a pdf file object
    pdfFileObj = open('chips_amazon.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    pageCount = len(pdfReader.pages)
    # printing number of pages in pdf file
    print(f"Page count: {pageCount}")

    giftCount, orderCount, unclassifiedCount = 0, 0, 0

    for pageNumber in range(pageCount):
        # creating a page object
        pageObj = pdfReader.pages[pageNumber]

        # extracting text from page
        pageText = pageObj.extract_text()

        if is_gift_receipt(pageText):
            giftCount += 1
            process_gift_receipt(pageText, pageNumber)
        elif is_order_receipt(pageText):
            orderCount += 1
            process_order_receipt(pageText, pageNumber)
        else:
            unclassifiedCount += 1
            process_unclassified_receipt(pageText, pageNumber)

    print(f"\n\nGift count: {giftCount}")
    print(f"Order count: {orderCount}")
    print(f"Unclassified count: {unclassifiedCount}")

    # closing the pdf file object
    pdfFileObj.close()


# def process_page(pdfReader: PyPDF2.PdfReader, pageNumber: int):
#     if pageNumber < 0 or pageNumber >= len(pdfReader.pages):
#         raise Exception("Invalid page number")


def is_gift_receipt(receiptText: str):
    return receiptText.find("A gift for you") != -1 or \
        receiptText.find("Enjoy your gift") != -1 or \
        receiptText.find("Gift Receipt") != -1 or \
        receiptText.find("Send a Thank You Note") != -1 or \
        receiptText.find("You can learn more about your gift") != -1 or \
        receiptText.find("start a return here too") != -1 or \
        receiptText.find("Scan using the Amazon app or visit") != -1


def is_order_receipt(receiptText: str):
    return receiptText.find("Order of") != -1 or \
        receiptText.find("Qty. Item") != -1 or \
        receiptText.find("Return or replace your item") != -1 or \
        receiptText.find("Visit Amazon") != -1


def process_gift_receipt(receiptText: str, pageNumber: int):
    print("---------------\n\n")
    print(f"Page {pageNumber}")
    print("Type: Gift receipt\n\n")
    print(receiptText)
    print("\n\n---------------")


def process_order_receipt(receiptText: str, pageNumber: int):
    print("---------------\n\n")
    print(f"Page {pageNumber}")
    print("Type: Order receipt\n\n")
    print(receiptText)
    print("\n\n---------------")


def process_unclassified_receipt(receiptText: str, pageNumber: int):
    print("---------------\n\n")
    print(f"Page {pageNumber}")
    print("Type: Unclassified receipt\n\n")
    print(receiptText)
    print("\n\n---------------")


if __name__ == "__main__":
    main()
