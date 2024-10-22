def konversisuhu(temperature, value): #mengkonversi suhu dari satu satuan ke satuan lainnya
    if value == 'C': #untuk menjalankan blok kode konversi Fahrenheit ke Celcius
        temperaturesuhu = (temperature - 32) * 5/9 #proses konversi suhu dari Fahrenheit ke Celcius
        return temperaturesuhu, 'C' #mengembalikan atau memberikan dua nilai hasil dari fungsi konversisuhu 
    else: # Jika 'value' bukan 'C', konversi dari Celsius ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) + 32 #Rumus konversi Celsius ke Fahrenheit
        return temperaturesuhu, 'F' # Mengembalikan nilai suhu yang sudah dikonversi beserta satuannya
    
celcius_temperature = 30 # Suhu awal dalam Celsius
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F') #Konversi dari Celsius ke Fahrenheit
print(f"{celcius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}") # Cetak hasil konversi

fahrenheit_temperature = 86 # Suhu awal dalam Fahrenheit
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C') # Konversi dari Fahrenheit ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")# Cetak hasil konversi 