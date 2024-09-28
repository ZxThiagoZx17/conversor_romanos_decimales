class RomanNumerals:
    @staticmethod
    def to_roman(num_decimal : int) -> str:
        romano= []
        valor_romano={"M":1000, "CM":900, "D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        for key, value in valor_romano.items():
            while value <= num_decimal:
                romano.append(key)
                num_decimal -= value
        return "".join(romano)
    
    @staticmethod
    def from_roman(roman_num : str) -> int:
        valor_romano={"M":1000, "CM":900, "D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        total = 0
        roman_num = roman_num.upper()
        lista_dec = [valor_romano.get(i) for i in roman_num]
        for ind , valor in enumerate(lista_dec):
            if ind+1 != len(lista_dec):
                if valor >= lista_dec[ind+1]:
                    total+=valor
                else: total-=valor
            else:total+=valor
        return total