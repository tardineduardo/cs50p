def getType(filename: str)-> str:
	filename = filename.strip().lower()
	_, dot, extension = filename.rpartition(".")
	
	types = {
        "gif":	"image/gif",
        "jpg":	"image/jpeg",
        "jpeg":	"image/jpeg",
        "png":	"image/png",
        "pdf":	"application/pdf",
        "zip":	"application/zip",
        "txt":	"text/plain"}
	
	if dot:
		return types.get(extension, "application/octet-stream")
	else:
		return "application/octet-stream"


def main():
	filename = input("File name: ")
	print(getType(filename))


main()