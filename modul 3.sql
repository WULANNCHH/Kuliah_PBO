-- Nama: Wulan Aulia
-- Nim: 24241029
-- Kelas: A
-- Modul: 3

-- nilai iteral, operator matematika, perbandingan, logika
-- fungsi matematika dan tanggal (Date)
-- Klausal WHERE, LIKE

-- praktek 1
-- Menggunakan nilai literal pada SELECT
SELECT 77;

-- praktek 2
-- menggunakan SELECT untuk menampilkan nilai literal dengan tipe data yang berbeda
SELECT 77 AS angka, false AS nilai_logika, 'PTI'As teks;


-- NULL
-- berarti tidak memiliki nilai apapun atau kosong
-- praktek 3
-- menggunakan SELECT untuk menggunakan NULL
SELECT NULL AS kosong;

-- Operator matematika
-- praktek 4
SELECT 5%2 AS sisa_bagi, 5/2 AS hasil_bagi_1, 5 DIV 2 AS hasil_bagi_2;

-- latihan sendiri 1
SELECT 5*4;
SELECT (4*8)%7;
SELECT (4*8) mod 7;

select 5*4;
SELECT 12+4;
SELECT 20-7;
select 81/9;
select 25 mod 4;
select (10+5)*2;
SELECT ((8*5)+10)%6; 

-- praktek 5
-- menggunakan database
USE pti_mart;

-- operatpr matematika untuk dua kolom dalam tabel penjualan
-- ambil data hasil perkalian kolom qty dan harga simpan dalam kolom total beli
-- praktek 6
SELECT qty_harga AS total_beli FROM tr_penjualan;

-- operator perbandingan 
-- simbol untuk membandingkan nilai dari nilai literal ataupun hasil ekspresi matematika
-- praktek 7
SELECT 5=5, 5!=5, 5!=4;



-- latihan 2
SELECT 1 = true;
SELECT 1 = false;
SELECT 5 >= 5;
SELECT 5.2=5.20000;
SELECT NULL = 1;
SELECT NULL = NULL;
SELECT NULL is NULL;

-- fungsi
-- proses yang memiliki nama, bukan simbol seperti 
-- praktek 8
SELECT POW(3,2), ROUND(3.14), ROUND(3.54), RAUND(3.155, 1), 
ROUND(3.155,2), FLOOR(4.28), FLOOR(4.78), CEILING(4.39), CEILING (4.55);

-- praktek 9
SELECT NOW(), YEAR ('2022-05-03'),
ROUND(DATEDIFF(NOW(), '2022-05-03') / 30),
DAY('2022-05-03');

-- latihan mandiri 3
SELECT DATEDIFF('2022-07-23', NOW());
SElECT YEAR('2022-07-23');
SELECT MONTH('2022-07-23');
SELECT  DAY('2022-07-23');
SELECT YEAR(NOW());

-- fungsi penting lainnya
SELECT CURDATE();
SELECT CURTIME();
SELECT NOW();