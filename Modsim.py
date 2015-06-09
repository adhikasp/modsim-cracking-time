import matplotlib.pyplot as plt
import seaborn as sns
import math

# CONSTANT
CURRENT_MD5_CRACK_SPEED    = 180*10**9
CURRENT_SHA1_CRACK_SPEED   = 63*10**9
CURRENT_BCRYPT_CRACK_SPEED = 71000
LOG_OF_2                   = math.log(2)
KBBI_WORD_COUNT            = 92000
STANDARD_US_KEYBOARD_CHAR_COUNT = 95

# SIMULATION CONFIGURATION
START_SIMULATION_YEAR = 2012
END_SIMULATION_YEAR   = 2050


class HashMethod():
    def __init__(self, hashSpeed):
        self.hashSpeed = hashSpeed

    def diffYear(self, currentYear):
        return (currentYear - START_SIMULATION_YEAR)

    def getHashSpeedNow(self, currentYear):
        return self.hashSpeed * math.pow(2, self.diffYear(currentYear)/2)

    def getCrackTime(self, currentYear, password):
        return (password.passwordStrength) / (self.getHashSpeedNow(currentYear)*3600*24*365)


class Password():
    """docstring for Password"""
    def __init__(self, plainText, entropy, charset):
        self.plainText = plainText
        self.entropy   = entropy
        self.charset   = charset
        self.passwordStrength = charset**entropy - 1

    def getEntropy(years):
        return self.entropy


MD5    = HashMethod(CURRENT_MD5_CRACK_SPEED)
Bcrypt = HashMethod(CURRENT_BCRYPT_CRACK_SPEED)
years  = [x for x in range(START_SIMULATION_YEAR, END_SIMULATION_YEAR)]

hard_random_password = Password('&oBYILnTra', 10, STANDARD_US_KEYBOARD_CHAR_COUNT)
hard_human_password  = Password('bergelutpanassemesterkacang', 4, KBBI_WORD_COUNT)

# Figure 1: Cracking Time for our password
# Subplot 1 for hard_random_password
plt.figure(1)
plt.subplot(211)
plt.title('Hard Random Password \"&oBYILnTra\"')
plt.plot(years, [MD5.getCrackTime(year, hard_random_password) for year in years], 'b-',
    years, [Bcrypt.getCrackTime(year, hard_random_password) for year in years], 'r-')
plt.yscale('log')
plt.ylabel('Crack Time (in years)')
plt.xlabel('Year')

# Subplot 2 for hard_human_password
plt.subplot(212)
plt.title('Hard Random Password \"bergelutpanassemesterkacang\"')
plt.plot(years, [MD5.getCrackTime(year, hard_human_password) for year in years], 'b-',
    years, [Bcrypt.getCrackTime(year, hard_human_password) for year in years], 'r-')
plt.yscale('log')
plt.ylabel('Crack Time (in years)')
plt.xlabel('Year')

# Figure 2: MD5 and Bcrypt Hash Speed
plt.figure(2)
plt.title('Grafik Kecepatan Komputer untuk meretas')
plt.plot(years, [MD5.getHashSpeedNow(year) for year in years], 'b-',
    years, [Bcrypt.getHashSpeedNow(year) for year in years], 'r-')
plt.yscale('log')
plt.ylabel('Crack speed / second')
plt.xlabel('Year')

plt.show()
