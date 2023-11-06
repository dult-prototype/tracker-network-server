## Tracker Network Server for DULT

- This is a simulation of a tracker network server.  
- The server has an endpoint ```/serial-number-decrypt``` which
takes a serial number as a parameter and returns an HTML view.
- The view contains decrypted serial number, and obfuscated owner information along with disablement instructions.

### Note
- For now, the server returns a dummy HTML page.  
- Ideally, the server should query the pairing registry database
 for owner info and disablement instructions and use those values in the HTML page response.

### Run

```python3 app.py```