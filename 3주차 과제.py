class sys:
    sys_count = 0

    def __init__(self, name, birth, key):
        self.name = name
        self.birth = birth
        self.key = key
        sys.sys_count += 1

    def info(self):
        print(f'이름: {self.name}')
        print(f'생일 : {self.birth}')
        print(f'신장: {self.key}')
        print()


sys1 = sys('구서영', 629, 158)
sys2 = sys('안영석', 726, 175)

sys1.info()
sys2.info()

sys1.attack(1)
sys2.attack(0)
