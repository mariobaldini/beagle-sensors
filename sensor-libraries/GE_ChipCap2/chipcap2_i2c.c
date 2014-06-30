
// Author: Mario Baldini (mario.baldini@ieee.org)
// Date: 30 June 2014

// Read the temperature and humidity of a GE ChipCap2 sensor connected to the I2C bus (2)
// Compatible with Beaglebone/Raspberry.
// Build with: gcc chipcap2_i2c.c -o chipcap2_i2c-2_arm.bin


// References: 
// https://www.kernel.org/doc/Documentation/i2c/dev-interface
// http://www.ge-mcs.com/download/moisture-humidity/916-108E.pdf
// Example for ChipCap2 library for Mosquino/Arduino


#include <linux/i2c-dev.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdlib.h>



int main(int argc, char** argv) {


    int file;
    int i2c_bus_number = 2; 
    char filename[20];
    int addr = 0x28; /* The I2C DEVICE address for GE ChipCap2*/
    char buf[10];


    snprintf(filename, 19, "/dev/i2c-%d", i2c_bus_number);
    file = open(filename, O_RDWR);
    if (file < 0) {
      exit(1);
    }

    if (ioctl(file, I2C_SLAVE, addr) < 0) {
      exit(1);
    }



    if (write(file,buf,1) != 1) {
          printf("Failed to write to the i2c bus.\n");
    }

    // Wake the sensor from sleep and trigger a measurement (may take up to 50 mili sec)
    usleep(50 * 1000);


    if (read(file, buf, 4) != 4) {
         printf("ERROR HANDLING: i2c transaction failed\n");
    } else {
        // debug 
        // printf("buf[0]: 0x%x\n", buf[0]);
        // printf("buf[1]: 0x%x\n", buf[1]);
        // printf("buf[2]: 0x%x\n", buf[2]);
        // printf("buf[3]: 0x%x\n", buf[3]);
        // printf("buf[4]: 0x%x\n", buf[4]);
        // printf("buf[5]: 0x%x\n", buf[5]);
        // printf("buf[6]: 0x%x\n", buf[6]);
        // printf("buf[7]: 0x%x\n", buf[7]);
        // printf("buf[8]: 0x%x\n", buf[8]);
        // printf("buf[9]: 0x%x\n", buf[9]);
    }


    uint16_t value_umi;
    float humidity;
    value_umi = buf[0];
    value_umi = (value_umi & 0x3F) << 8;
    value_umi = value_umi | buf[1];
    humidity = value_umi;
    humidity = humidity / 163.84;
    // printf("humidity: %f\n", humidity); 


    uint16_t value_temp;
    float temperature;

    value_temp = buf[2];
    value_temp = value_temp << 8;
    value_temp = value_temp | buf[3];
    value_temp = value_temp & 0xFFFC;
    temperature = value_temp;
    temperature = ((temperature / 65536) * 165) - 40;
    // printf("temperature: %f\n", temperature); 


    // Prints the temperature and humidity, comma separated, with 2 decimal precision
    printf("%0.2f,%0.2f\n", temperature, humidity); 


    return 0;
}



