from dronekit import connect, VehicleMode, LocationGlobalRelative
import time



#vehicle Conne tion
drone = connect('127.0.0.1.:14551', wait_ready=True)

while not drone.is_armable:
	print("Vehicle is not armable, waiting...")
	time.sleep(1)

print("Ready to arm")
drone.mode = VehicleMode("Guided")
drone.armed = True