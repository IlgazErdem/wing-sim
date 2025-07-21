import math

class Pressure:

    def __init__(self, altitude_m, groundtemperature_k =288.0, groundpressure_pa = 101325.0 ,humidity=0):

        self.groundtemperature = groundtemperature_k
        self.altitude = altitude_m
        self.humidity = humidity
        self.groundpressure = groundpressure_pa

        self.gravity = 9.8066 # dim = m * m / s
        self.boltzmann = 1.3806e-23  # dim J / K
        self.mavg = 29.000 * 1.6605e-27  # dim kg
        self.lapserate = 9.8  #dim K / km

        # UNUSED
        # self.gasconstant = 287.05 # dim J / (k * mol)
        # self.standarttemperature = 288.00 # dim K
        # self.standartpressure = 101.325 # dim pa

        # TODO: CHECK AND CONVERT TO USABLE UNITS


        self.temperature = self.calculate_temperature_at_height()
        self.pressure = self.calculate_pressure()

    def calculate_pressure(self):
        #Barometric formula
        #http://hyperphysics.phy-astr.gsu.edu/hbase/Kinetic/barfor.html#c2
        return self.groundpressure * -math.exp(self.altitude * self.gravity * self.mavg / (self.boltzmann * self.temperature))

    def calculate_temperature_at_height(self):

        #R = 287.05 # dim = J / (kg * K)  gas constant
       # g = 9.8066 # dim = m * m / s  standard gravity of earth

        # VERY ROUGH ESTIMATION FOR NOW
        return self.groundtemperature - (int(self.altitude) / 1000) * 3.5









