import pandas as pd
import matplotlib.pyplot as plt
import os 

# !pip install PyQt6

# df = pd.read_csv('waveforms/11/shot001_ALL.csv', skiprows=11)
# print(df)
dir = 'waveforms/110924/'
files = sorted(os.listdir(dir))
print(files)
csv_files = []

for file in files:
    if (file.endswith('.csv')):
        csv_files.append(file)
print(csv_files)

plt.ioff()  # Выключить интерактивный режим
def plot_graph():
    plt.figure(figsize=(10, 6))
    plt.rcParams["font.family"] = "serif" # font
    plt.subplot(2, 1, 1)
    plt.xlim(df.iloc[0, 0]*1e9, df.iloc[-1, 0]*1e9)
    plt.ylabel('Intensity, mV')
    plt.xlabel('Time, ns')
    plt.plot(df['TIME']*1e9, df['CH1']*1e3, color='red')

    plt.subplot(2, 1, 2)
    plt.xlim(df.iloc[0, 0]*1e9, df.iloc[-1, 0]*1e9)
    plt.ylim(0, df['CH2'].mean()*1e3 * 2 )
    plt.ylabel('Reflectance, of the GST225, mV')
    plt.xlabel('Time, ns')
    plt.plot(df['TIME']*1e9, df['CH2']*1e3)

    plt.tight_layout()  # Автоматическая регулировка расстояния между графиками

for file in csv_files:
    path = dir + file
    df = pd.read_csv(path, skiprows=11)
    print(file)
    plot_graph()
    plt.show()
    save = input('Save?(y or n): ')
    if(save == 'y'): 
        plt.savefig('007.png', dpi=300, bbox_inches='tight')
    plt.close()
    
