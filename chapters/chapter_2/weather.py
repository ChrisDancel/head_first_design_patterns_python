import numpy as np
from abc import ABC, abstractmethod

# Observer pattern
# The oberserver pattern defines a one-to-many relationship between a set of objects.
#
# When the state of one object changes, all of its dependents are notified

# CREATE INTERFACES
class Subject(ABC):

    @abstractmethod
    def registerObserver(self):
        raise NotImplementedError

    @abstractmethod
    def removeObserver(self):
        raise NotImplementedError

    @abstractmethod
    def notifyObserver(self):
        raise NotImplementedError


class Observer(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def registerObserver(self, o):
        self.observers.append(o)

    def removeObserver(self, o):
        self.observers.remove(0)

    def notifyObserver(self):
        [o.update() for o in self.observers]

    def measurementsChanged(self):
        self.notifyObserver()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weatherData):
        self.temperature = None
        self.humidity = None
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self):
        self.temperature = self.weatherData.getTemperature()
        self.humidity = self.weatherData.getTemperature()
        self.display()

    def display(self):
        print(f'Current Conditions: {self.temperature}F degrees and {self.humidity}% humidity')


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weatherData):
        self.temperature = []
        self.humidity = []
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self):
        self.temperature = self.weatherData.getTemperature()
        self.humidity = self.weatherData.getTemperature()
        self.display()

    def display(self):
        print(
            f'Avg/Max/Min temperature: {np.mean(self.temperature)}/{np.max(self.temperature)}/{np.min(self.temperature)}')


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weatherData):
        self.temperature = None
        self.humidity = None
        self.currentPressure = 29.92
        self.lastPressure = None
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self):
        self.lastPressure = self.currentPressure
        self.currentPressure = weatherData.getPressure()
        self.temperature = self.weatherData.getTemperature()
        self.humidity = self.weatherData.getTemperature()
        self.display()

    def display(self):

        if self.currentPressure == self.lastPressure:
            print('Forecast: more of the same')
        elif self.currentPressure < self.lastPressure:
            print('Forecast: Watch out for cooler, rainy weather')
        elif self.currentPressure > self.lastPressure:
            print('Forecast: Improving weather on the way!')


def heat_index(t, rh):
    index = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
              (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
              (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
              (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                                                                                  (rh * rh * rh)) + (
                      0.00000142721 * (t * t * t * rh)) +
              (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
              0.000000000843296 * (t * t * rh * rh * rh)) -
             (0.0000000000481975 * (t * t * t * rh * rh * rh)))

    return index


if __name__ == '__main__':
    weatherData = WeatherData()
    currentDisplay = CurrentConditionDisplay(weatherData)
    statisticalDisplay = StatisticsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)

    weatherData.setMeasurements(80.0, 65.0, 30.4)
    weatherData.setMeasurements(82.0, 70.0, 29.2)
    weatherData.setMeasurements(78.0, 90.0, 29.2)
