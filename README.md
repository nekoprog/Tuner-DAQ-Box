# Tuner-DAQ-Box
Arduino UNO Car Tuning Data Logger

Arduino Side:
3 channel input (02 wideband, engine crank RPM and car speed KM/h)

Python Side:
Realtime graph from serial input (wbo2, rpm, speed sensor) and microphone input (knock sensor)

TODO:
- WB02 linear 5v input
- RPM decoder
- KM/h decoder
- Knock detector using microphone input
- Realtime data stream to PC (usb/wifi/bluetooth)
- PC graph plotting and save to CSV for future analysis
- PC UI
- Use VisPy, PySide, PySerial, NumPy
