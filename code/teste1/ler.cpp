#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/i2c.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <stropts.h>
#include <stdio.h>
//#include "BMA180Accelerometer.h"
#include <iostream>
#include <math.h>
using namespace std;
#define MAX_BUS 255



int main(int argc, char *argv[]) {


cout << "Starting BMA180 I2C sensor state read" << endl;
 char namebuf[MAX_BUS];
 snprintf(namebuf, sizeof(namebuf), "/dev/i2c-%d", I2CBus);
 int file;


}

