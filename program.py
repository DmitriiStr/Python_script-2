import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

# Шифруем файл
# pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# Дешифруем
pyAesCrypt.decryptFile('data.txt.aes', 'datata.txt', password)
