from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time 

#this is to link with the drone and to takeoff
def arm_and_takeoff(TargetAltitude):
	print ("Executing takeoff")
#this shows that the drone is going to takeoff
	while not drone.is_armable:
		print ("Vehicle is not armable, waiting......")
		time.sleep(1)
#here we are setting the drone on guided mode
	print ("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True
#With this a message pops out showing if the drone is not armed
	while not drone.armed:
		print("Waiting for arming...")
		time.sleep(1)
#drone.simple_takeoff is the command used in order to make the drone takeoff
	print("ready for takeoff, taking off..")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude", Altitude)
		time.sleep(1)
#here we are setting the altitude we want our drone to have
		if Altitude >= TargetAltitude * 0.95:
			print("Altitude Reached")
			break


#Vehicle Connection 
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

#Colocamos las coordenadas de los puntos en la cancha de football
#al poner drone.groundspeed y drone.airspeed logramos que el drone se mueva a una velocidad definida
drone.airspeed=10
punto1 = LocationGlobalRelative(20.736094, -103.456862, 20)
punto2 = LocationGlobalRelative(20.736143, -103.457431, 20)
punto3 = LocationGlobalRelative(20.735687, -103.457451, 20)
punto4 = LocationGlobalRelative(20.735681, -103.456954, 20)


#this is to show that the drone did the takeoff
print("Despegue exitoso")
#whit this the drone goes to the first waypoint
print("Drone se dirige al primer punto")
drone.simple_goto(punto1)
time.sleep(15)
print("Punto1 completado")
#whit this the drone goes to the second waypoint
print("El drone se dirige al segundo punto")
drone.simple_goto(punto2)
time.sleep(15)
print("Punto2 completado")
#whit this the drone goes to the third waypoint
print("El drone se dirige al tercer punto")
drone.simple_goto(punto3)
time.sleep(15)
print("Punto3 completado")
#whit this the drone goes to the fourth waypoint
print("El drone se dirige al cuarto punto")
drone.simple_goto(punto4)
time.sleep(15)
print("Punto 4 completado")
print("Volando al punto de despegue")
print("Regresando a punto de despegue")
#repeting the first waypoint we complete the square
drone.simple_goto(punto1)
time.sleep(10)
#whit this command the drone will return to the launch area
drone.mode = VehicleMode("RTL")
print("El dron regreso exitosamente")
#Whit this code we can show the battery percentage in volts
battery = drone.battery.voltage
print("battery voltage", battery, "V")



