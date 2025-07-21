class Pressure:

    # the defaults for pressure and temperature at sea level are 101,325 Pa and 288 K

    def __init__(self, altitude_m, groundtemperature_k =288.0, groundpressure_pa = 101325.0 ,humidity=0):

        self.groundtemperature = groundtemperature_k
        self.altitude = altitude_m
        self.humidity = humidity
        self.groundpressure = groundpressure_pa

        self.pressure = self.calculate_pressure()
        self.tempuratur = self.calculate_temperature_at_height()

    def calculate_pressure(self):
        #Barometric formula
        #http://hyperphysics.phy-astr.gsu.edu/hbase/Kinetic/barfor.html#c2
        # P final = P ground * e ^ (-m * g * h / (k * T) )
        placeholder = 0
        return placeholder

    def calculate_temperature_at_height(self):

        #R = 287.05 # dim = J / (kg * K)  gas constant
       # g = 9.8066 # dim = m * m / s  standard gravity of earth

        # VERY ROUGH ESTIMATION FOR NOW
        return self.groundtemperature - (int(self.altitude) / 1000) * 3.5









