print("Tabel Perkalian dan Statistik") #[cite: 16]
n = int(input("n: ")) #[cite: 16]

while n <= 0: #[cite: 16]
    print("n harus positif.") #[cite: 16]
    n = int(input("n: ")) #[cite: 16]

total_semua = 0 #[cite: 16]
count_genap = 0 #[cite: 16]

for i in range(1, n + 1): #[cite: 16]
    total_baris = 0 #[cite: 16]
    for j in range(1, n + 1): #[cite: 16]
        hasil = i * j #[cite: 16]
        print(f"{hasil:4}", end="") #[cite: 16]
        total_baris += hasil #[cite: 16]
        total_semua += hasil #[cite: 16]
        if hasil % 2 == 0: #[cite: 16]
            count_genap += 1 #[cite: 16]
    print(f" | jumlah baris {total_baris}") #[cite: 16]

print(f"Total seluruh hasil {total_semua}") #[cite: 16]
print(f"Banyak hasil genap {count_genap}") #[cite: 16]