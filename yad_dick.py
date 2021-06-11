import yadisk

TOKEN = 'AQAAAABDbQxIAAco2ZXCPiJcaUzWmybTUCHESK4'

y = yadisk.YaDisk(token=TOKEN)
print(y.check_token())


print(list(y.listdir("bet365")))

# Загружает "file_to_upload.txt" в "/destination.txt"
y.upload("2.png", "/2.png")