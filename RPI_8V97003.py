
import spidev
import time

# Create an SPI object
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0

# Configure SPI settings
spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz (adjust as needed)
spi.mode = 0                # Set SPI mode (0 or 3)

# Define an 8-bit array to send
data = [0x12, 0x34, 0x56, 0x78]  # Example data (adjust as needed)

try:
    # Send data over SPI
    spi.xfer(data)

    # Wait for a short time (optional)
    time.sleep(0.1)

finally:
    # Close SPI connection
    spi.close()