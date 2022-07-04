The data collected in the accompanying .csv file contains the following information per device,
aggregated during the last 7 days of activity:

Client_ID: the ID of the Nexthink customer to which the data belongs
Office_ID: the unique ID of each office from every customer
BSOD_count: the number of Blue Screens of Death that occured
Hard_reset_count: the number of improper shutdowns (or hard resets) that occured. This means power outages, holding the power button, pushing the reset button, etc.
Boot_Speed: the average time taken by the device to go from BIOS to Logon screen.
Logon_Duration: the average time taken by the device from entering the windows user password to seeing the desktop, in miliseconds 
CPU_Usage: the percentage of time the CPU usage was over 80%, scaled to 0..1
Memory_Usage: the percentage of time the Memory usage was over 80%, scaled to 0..1
System_Free_Space: the ammount of free space on the operating system partition (usually C:\ for Windows), in bytes