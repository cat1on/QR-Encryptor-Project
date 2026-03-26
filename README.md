🔐 QR Encryptor
QR Encryptor is a two-part application (Desktop + Android) designed for secure offline storage of sensitive information using encrypted QR codes.
🖥 Desktop Application
The desktop app allows users to:
Create a passphrase
Enter text to encrypt
Generate a QR code containing encrypted data
The generated QR code can be printed and stored physically (e.g., on paper), ensuring offline and secure storage without relying on cloud services.
📱 Android Application
The mobile app allows users to:
Scan the generated QR code
Enter the same passphrase
Decrypt and retrieve the original text
🔒 Security
Encryption is performed using AES-GCM (Advanced Encryption Standard in Galois/Counter Mode)
Each encryption uses a random salt and nonce
Data is safely packed into a compact JSON format and encoded into a QR code
💡 Use Cases
Storing passwords or recovery phrases
Secure offline backups
Transferring sensitive data without internet
⚠️ Important
Without the correct passphrase, the data inside the QR code cannot be decrypted.
⚠️ Note: Avoid storing large amounts of data in a single QR code. Excessive data may reduce readability and prevent successful scanning.
## 💖 Support the Project

If you find this project useful, feel free to support me:

- **Binance Pay ID:** `cat1on`  

📱 Scan this QR code using Binance app (Binance Pay):

![Binance QR](./assets/binance_qr.png)

OR

USDT (Tether)
Network: TRC20

Address: TMpYLbgRDvoPyMXV9fb1N9ojQrkZYypdtZ
⚠️ Please select TRC20 network
