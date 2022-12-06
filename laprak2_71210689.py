import random
class Stack:
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)
    def top(self):
        if len(self.data) == 0:
            return False
        else:
            return self.data[-1]
    def pop(self):
        if len(self.data) == 0:
            return False
        else:
            return self.data.pop()
class Dek_kartu:
    def __init__(self):
        self.kartu = Stack()
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        for kartu in (3,8,5,"J",7,"A",4,9,10,6,"Q","K",2):
            self.kartu.push(f"{kartu}♥️")
            self.kartu.push(f"{kartu}♦️")
            self.kartu.push(f"{kartu}♠️")
            self.kartu.push(f"{kartu}♣️")

    def shuffle(self):
        n = random.randint(21, 36)
        for i in range(n):
            self.stack_1.push(self.kartu.pop())
        for i in range(52-n):
            self.stack_2.push(self.kartu.pop())
        for i in range(n):
            self.kartu.push(self.stack_1.pop())
        for i in range(52-n):
            self.kartu.push(self.stack_2.pop())
        n = random.randint(21, 36)
        for i in range(n):
            self.stack_1.push(self.kartu.pop())
        for i in range(52-n):
            self.stack_2.push(self.kartu.pop())
        for i in range(52):
            if len(self.stack_2.data) != 0:
                self.kartu.push(self.stack_2.pop())
            if len(self.stack_1.data) != 0:
                self.kartu.push(self.stack_1.pop())

    def ambil_kartu(self):
        return self.kartu.pop()
class Player:
    def __init__(self):
        self.hand = []
        self.poin = 0
        self.uang = 1000
        self.poin_map = {}
        for kartu in (2,3,4,5,6,7,8,9,10,"J","Q","K","A"):
            self.poin_map[f"{kartu}♥️"] = kartu
            self.poin_map[f"{kartu}♦️"] = kartu
            self.poin_map[f"{kartu}♠️"] = kartu
            self.poin_map[f"{kartu}♣️"] = kartu
        for i in self.poin_map.keys():
            if str(self.poin_map[i]) in "AJQK":
                self.poin_map[i] = 11

    def hit(self, dek):
        kartu = dek.ambil_kartu()
        self.hand.append(kartu)
        self.poin += self.poin_map[kartu]
    
    def ambil_uang(self, jumlah):
        self.uang -= jumlah
    def terima_uang(self, jumlah):
        self.uang += jumlah
    
if __name__ == "__main__":
    dealer = Player()
    p1 = Player()
    while True:
        p1.hand = []
        dealer.hand = []
        p1.poin = 0
        dealer.poin = 0
        dek = Dek_kartu()
        for i in range(200):
            dek.shuffle()
        for i in range(2):
            dealer.hit(dek)
            p1.hit(dek)
        if p1.poin > 18 or dealer.poin > 18:
            continue
        if p1.uang <= 0:
            print("Maaf, uang Anda habis")
            break
        print(f'Sisa uang Anda: ${p1.uang}')
        print(f"Dealer: {['??'] + dealer.hand[1:]}, ( ?? )")
        print(f"Player: {p1.hand}, ({p1.poin})")
        taruhan = float(input('Masukkan taruhan: $'))
        as_p1 = ["A♥️", "A♦️", "A♠️","A♣️"]
        as_dealer = ["A♥️", "A♦️", "A♠️","A♣️"]
        while True:
            print("Pilih option (1/2):\n1. Hit\n2. Stick")
            option = input("pilihan: ")
            if int(option) == 1:
                p1.hit(dek)
                if p1.poin == 21:
                    p1.terima_uang(taruhan)
                    print('\nHasil akhir:')
                    print("ANDA MENANG!!!!!")
                    print(f"Dealer: {dealer.hand}, ({dealer.poin})")   
                    print(f"Player: {p1.hand}, ({p1.poin})")
                    print(f'SISA UANG ANDA: ${p1.uang}')
                    break                    
                if p1.poin > 21:
                    jumlah_as = []
                    for kartu in p1.hand:
                        if kartu in as_p1:
                            jumlah_as += [kartu]

                    for i in jumlah_as:
                        p1.poin -= 10
                        as_p1.remove(i)
                        if p1.poin <= 21:
                            break
                    else:
                        p1.ambil_uang(taruhan)
                        print("\nHasil akhir:")
                        print("Anda Kalah")
                        print(f"Dealer: {dealer.hand}, ({dealer.poin})")
                        print(f"Player: {p1.hand}, ({p1.poin})")
                        print(f'SISA UANG ANDA: ${p1.uang}')
                        break

                print(f"Dealer: {['??'] + dealer.hand[1:]}, ( ?? )")
                print(f"Player: {p1.hand}, ({p1.poin})")
#GILIRANNYA DEALER
            else:
                n = random.randint(15, 19)
                while dealer.poin < n:
                    dealer.hit(dek)
                if dealer.poin == 21:
                        p1.ambil_uang(taruhan)
                        print("\nHasil akhir:")
                        print("Anda Kalah")
                        print(f"Dealer: {dealer.hand}, ({dealer.poin})")
                        print(f"Player: {p1.hand}, ({p1.poin})")
                        print(f'SISA UANG ANDA: ${p1.uang}')
                        break            
                if dealer.poin > 21:
                    jumlah_as = []
                    for kartu in dealer.hand:
                        if kartu in as_dealer:
                            jumlah_as += [kartu]
                    for kartu in jumlah_as:
                        dealer.poin -= 10
                        as_dealer.remove(kartu)
                        if dealer.poin <= 21:
                            break
                    else:
                        p1.terima_uang(taruhan)
                        print('\nHasil akhir:')
                        print("ANDA MENANG!!!!!")
                        print(f"Dealer: {dealer.hand}, ({dealer.poin})")   
                        print(f"Player: {p1.hand}, ({p1.poin})")
                        print(f'SISA UANG ANDA: ${p1.uang}')
                        break             
                break


                
        if p1.poin >=21 or dealer.poin >=21:
            replay = input("Main lagi?(y/t): ")
            if replay == 't':
                break
            else:
                print()
                continue
        elif p1.poin > dealer.poin:
            p1.terima_uang(taruhan)
            print('\nHasil akhir:')
            print("ANDA MENANG!!!!!")
            print(f"Dealer: {dealer.hand}, ({dealer.poin})")   
            print(f"Player: {p1.hand}, ({p1.poin})")
            print(f'SISA UANG ANDA: ${p1.uang}')            
        elif p1.poin < dealer.poin:
            p1.ambil_uang(taruhan)
            print('\nHasil akhir:')
            print("anda kalah")
            print(f"Dealer: {dealer.hand}, ({dealer.poin})")
            print(f"Player: {p1.hand}, ({p1.poin})")
            print(f'SISA UANG ANDA: ${p1.uang}')
        elif p1.poin == dealer.poin:
            print('\nHasil akhir:')
            print("DRAW")
            print(f"Dealer: {dealer.hand}, ({dealer.poin})")
            print(f"Player: {p1.hand}, ({p1.poin})")
            print(f'SISA UANG ANDA: ${p1.uang}')
        replay = input("Main lagi?(y/t): ")
        if replay == 't':
            break
        else:
            print()
            continue



