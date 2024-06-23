import spidev
import time

# Create an SPI instance
spi = spidev.SpiDev()

# Open SPI bus 0, device (CS) 0
spi.open(0, 0)

# Set SPI speed and mode
spi.max_speed_hz = 500000  # 500 kHz
spi.mode = 0b00  # SPI mode 0

def read_spi(channel):
    """Read data from SPI device on the specified channel."""
    if channel < 0 or channel > 7:
        return -1
    
    # Perform SPI transaction
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    
    # Process returned data
    data = ((adc[1] & 3) << 8) + adc[2]
    
    return data

def write_spi(data):
    """Write data to SPI device."""
    spi.xfer2([data])

try:
    while True:
        # Read data from channel 0
        adc_value = read_spi(0)
        print(f"ADC Value: {adc_value}")

        # Write data to SPI device
        write_spi(0xAA)

        # Sleep for a bit before next read/write
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup and close SPI connection
    spi.close()
    print("SPI connection closed.")

