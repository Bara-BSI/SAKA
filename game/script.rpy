# Jalan Cerita
label start:
    stop sound fadeout 2.0
    scene starting with dissolve
    call screen gender
    scene kamar with fade
    play sound "vibration_sound_effect.mp3"
    queue sound "game-music-loop-7-145285.mp3" loop fadein 2.0
    #show awan at abscenter with dissolve
    show hp_alarm at abscenter, shake_with_pause with dissolve
    "\"Bib… bib… bib… ♪♪\"\[Bunyi alarm mengganggu\]" with dissolve
    "\[Mengambil handphone yang tergeletak di meja\]"
    "Aku menekan tombol power dan layar handphoneku menampilkan wallpaper yang bertuliskan namaku"
    python:
        player_name = renpy.input("Namaku adalah... ")
        player_name = player_name.strip()
        vei = 0
        vsn = 0
        vtf = 0
        vjp = 0
    define p = Character("[player_name]")
    hide hp_alarm with dissolve
    if gender=="L":
        show player_male_home_neutral_fix with dissolve
    else:
        show player_female_home_neutral_fix with dissolve
    "Yup, namaku [player_name]."
    if gender=="L":
        show player_male_home_happy_fix with dissolve
    else:
        show player_female_home_happy_fix with dissolve
    "Aku baru saja pindah ke kota ini dan hari ini adalah hari pertamaku masuk SMA."
    if gender=="L":
        show player_male_home_awkward_fix with dissolve
    else:
        show player_female_home_awkward_fix with dissolve
    "Harapanku besar di hari pertama ini, semoga saja berjalan baik. Aku tidak bisa terlambat di hari pertama, maka ku segera bersiap."
    if gender=="L":
        hide player_male_home_neutral_fix with dissolve
        hide player_male_home_happy_fix with dissolve
        hide player_male_home_awkward_fix with dissolve
    else:
        hide player_female_home_neutral_fix with dissolve
        hide player_female_home_happy_fix with dissolve
        hide player_female_home_awkward_fix with dissolve
    if gender=="L":
        show player_male_neutral_fix with dissolve
    else:
        show player_female_neutral_fix with dissolve
    "\[Mengambil ransel\]"
    if gender=="L":
        show player_male_ransel_happy_fix with dissolve
    else:
        show player_female_ransel_happy_fix with dissolve
    p "Ayo berangkat! Jangan sampai telat!"
    "Ucapku untuk kembali fokus."
    
    jump act1
label act1:
    scene gedung sma with fade
    if gender=="L":
        show player_male_ransel_neutral_fix with dissolve
    else:
        show player_female_ransel_neutral_fix with dissolve
    "Aku tiba di sekolah baruku,  beberapa menit sebelum acara penyambutan siswa baru akan dimulai di aula sekolah."
    scene aula sekolah with dissolve
    "Berbagai kegiatan dilalui pada kegiatan tersebut. Karena saking serunya, tak terasa waktu istirahat telah tiba."
    scene tamanai with dissolve
    "Siswa-siswi berpencar, ada yang ke kantin dan ada yang makan bekal di taman."
    if gender=="L":
        show player_male_neutral_fix with dissolve
    else:
        show player_female_neutral_fix with dissolve
    "\[Melihat ke sekeliling\]"
    if gender=="L":
        show player_male_awkward_fix with dissolve
    else:
        show player_female_awkward_fix with dissolve
    p "Hmm, apa yang sebaiknya kulakukan ya?"
    if gender=="L":
        #hide player_male_awkward_fix with dissolve
        show player_male_uncomfortable_fix with dissolve
    else:
        #hide player_female_awkward_fix with dissolve
        show player_female_uncomfortable_fix with dissolve
    p "Aku bisa bergabung dengan kelompok di kantin, tapi di taman sepertinya nyaman. Pilihan yang sulit..."
    "...\[berpikir\]"
    if gender=="L":
        hide player_male_awkward_fix with dissolve
        show player_male_happy_fix with dissolve
    else:
        hide player_female_awkward_fix with dissolve
        show player_female_happy_fix with dissolve
    p "Baiklah, sudah kuputuskan! aku akan:..."
    if gender=="L":
        hide player_male_uncomfortable_fix with dissolve
        show player_male_happy_fix at Blur with dissolve
    else:
        hide player_female_uncomfortable_fix with dissolve
        show player_female_happy_fix at Blur with dissolve
    menu:
        "Aku akan..."
        "Menghampiri dan berinteraksi dengan teman yang bergerombol, dan makan bersama di kantin.":
            $ vei += 1
        "Memakan bekal yang dibawa dari rumah sendirian di bawah pohon yang ada di taman sekolah.":
            $ vei += 2
    
    scene aula sekolah with fade
    "Waktu istirahat telah usai, dan para siswa baru bergegas kembali ke aula."
    "Acara demi acara berlangsung lancar hingga akhirnya kegiatan penyambutan pun selesai."
    "Dengan hati yang puas dan penuh harapan, para siswa baru kemudian meninggalkan aula dan pulang ke rumah masing-masing..."
    " membawa serta pengalaman dan kenangan baru dari hari pertama mereka di sekolah."
    jump act2

label act2:
    scene kamar with fade
    if gender=="L":
        show player_male_ransel_happy_fix with dissolve
    else:
        show player_female_ransel_happy_fix with dissolve
    "Hari pertama sekolah pun tiba, dan aku merasa sedikit gugup sekaligus bersemangat."
    scene kelas ramai  with fade
    if gender=="L":
        show player_male_ransel_neutral_fix with dissolve
    else:
        show player_female_ransel_neutral_fix with dissolve
    stop sound fadeout 2.0
    play sound "generic-crowd-background-noise-31310.mp3" loop fadein 2.0
    "\[Memasuki kelas\]"
    "\[Suara obrolan anak-anak\]"
    
    if gender=="L":
        show player_male_ransel_happy_fix with dissolve
    else:
        show player_female_ransel_happy_fix with dissolve
    p "Wahh… ramai sekali…"
    if gender=="L":
        show player_male_ransel_uncomfortable_fix with dissolve
        hide player_male_ransel_neutral_fix
    else:
        show player_female_ransel_uncomfortable_fix with dissolve
        hide player_female_ransel_neutral_fix
    p "Banyak yang sudah memilih bangku."
    p "Enaknya duduk di mana ya?"
    if gender=="L":
        show player_male_ransel_neutral_fix at Blur,center with dissolve
        hide player_male_ransel_happy_fix
    else:
        show player_female_ransel_neutral_fix at Blur,center with dissolve
        hide player_female_ransel_happy_fix

    menu:
        "Sebaiknya aku..."
        "Melihat-lihat dulu ke sekeliling, siapa tahu dapat spot yang bagus":
            $ vsn += 1
        "Melihat salah satu bangku dan langsung menempatinya. ":
            $ vsn += 2
    
    if gender=="L":
        show player_male_ransel_happy_fix with dissolve
    else:
        show player_female_ransel_happy_fix with dissolve
    p "Di sini sepertinya pas"
    "Aku menempati bangku barisan ke dua paling kanan."
    jump act3

label act3:
    scene kelas ramai with fade
    show zachary_neutral_fix with dissolve
    "\[Seorang anak mendekat\]"
    define r = Character("???")
    hide zachary_neutral_fix with dissolve
    
    show zachary_happy_fix at left with dissolve
    if gender=="L":
        show player_male_neutral_fix at right, Blur with dissolve
    else:
        show player_female_neutral_fix at right, Blur with dissolve
    r "Aku boleh duduk di sini?"

    show zachary_happy_fix at left, Blur with dissolve
    if gender=="L":
        show player_male_neutral_fix at right, Normal with dissolve
    else:
        show player_female_neutral_fix at right, Normal with dissolve
    p "Boleh, silahkan saja."

    show zachary_happy_fix at left, Normal with dissolve
    if gender=="L":
        show player_male_neutral_fix at right, Blur with dissolve
    else:
        show player_female_neutral_fix at right, Blur with dissolve
    r "Hehe… makasih. \[duduk\]"

    show zachary_concern_fix at left, Normal with dissolve
    r "Oh ya, namamu siapa?"

    show zachary_concern_fix at left, Blur with dissolve
    if gender=="L":
        show player_male_happy_fix at right, Normal with dissolve
    else:
        show player_female_happy_fix at right, Normal with dissolve
    p "Oh, kenalkan aku [player_name]"

    show zachary_happy_fix at left, Normal with dissolve
    hide zachary_concern_fix
    if gender=="L":
        show player_male_happy_fix at right, Blur with dissolve
    else:
        show player_female_happy_fix at right, Blur with dissolve
    define z = Character("Zachary")
    z "Aku Zachary, kamu bisa panggil aku Zac. Salam kenal!"

    show zachary_happy_fix at left, Blur with dissolve
    if gender=="L":
        show player_male_happy_fix at right, Normal with dissolve
    else:
        show player_female_happy_fix at right, Normal with dissolve
    p "Salam kenal Zac. \[senyum ramah\]"
    scene kelas_papan_tulis with fade
    play sound "japanese_school_bell.mp3"
    queue sound "game-music-loop-7-145285.mp3" loop
    "\[Bel sekolah berbunyi\]"
    show guru_happy_fix with dissolve
    "\[Guru seni masuk ke kelas dengan senyum ramah\]"
    define s = Character("Guru ???")
    show guru_neutral_fix with dissolve
    s "Selamat pagi, anak - anak!"
    "“Pagi pak!!” jawab murid serentak."
    "Setiap siswa diminta untuk membuat karya seni lukis."
    hide guru_happy_fix with dissolve
    hide guru_neutral_fix with dissolve
    show gambar_imajinatif at abscenter with dissolve
    "Mereka diberikan dua pilihan: melukis gambar abstrak, yang memungkinkan ekspresi bebas dan kreativitas tanpa batas..."
    hide gambar_imajinatif with dissolve
    show gambar_presisi at abscenter with dissolve
    " atau melukis gambar presisi, yang menuntut ketelitian dan detail yang sempurna."
    hide gambar_presisi with dissolve
    "Siswa-siswa mulai berdiskusi di antara mereka, mempertimbangkan pilihan yang akan diambil."
    if gender=="L":
        show player_male_neutral_fix at center, Normal with dissolve
    else:
        show player_female_neutral_fix at center, Normal with dissolve
    "Aku sudah memutuskan akan memilih..."
    if gender=="L":
        show player_male_neutral_fix at Blur with dissolve
    else:
        show player_female_neutral_fix at Blur with dissolve

    # menu:
    #     "melukis gambar presisi":
    #         $ vtf += 1
    #     "melukis gambar abstrak":
    #         $ vtf += 2
    
    call screen gambartf
    # "{color=#FF0000}Debug\n vtf=[vtf] terpilih.{/color}"
    jump act4

label act4:
    stop sound fadeout 2.0
    play sound "school_bell.mp3" fadein 1.0
    queue sound "game-music-loop-7-145285.mp3" fadein 2.0
    scene kelas versi anime with fade
    "Singkat cerita, bel pulang sekolah berbunyi, menandakan akhir dari hari yang panjang. "
    if gender=="L":
        show player_male_ransel_neutral_fix at center, Normal with dissolve
    else:
        show player_female_ransel_neutral_fix at center, Normal with dissolve
    "Aku segera mengemas barang-barangku, mengamati sejenak kelas yang mulai sepi, lalu berjalan keluar dan pulang."
    scene kamar with fade
    if gender=="L":
        show player_male_home_neutral_fix at center, Normal with dissolve
    else:
        show player_female_home_neutral_fix at center, Normal with dissolve
    "Setibanya di rumah, aku berganti pakaian menjadi lebih nyaman dan membuka tas sekolah."
    scene buku tersusun rapi di meja with dissolve
    "Dengan teliti, aku mengeluarkan buku paket dan buku tulis, menatanya rapi di rak buku di kamarku."
    scene kamar_malam with dissolve
    "Waktu terus berlalu, dan malam pun tiba dengan tenang."
    
    if gender=="L":
        show player_male_home_uncomfortable_fix at center, Normal with dissolve
    else:
        show player_female_home_uncomfortable_fix at center, Normal with dissolve
    "Saat bersantai sejenak, aku tiba-tiba teringat dengan tugas seni lukis yang diberikan oleh guru."
    "Aku memutuskan untuk:"
    
    if gender=="L":
        show player_male_home_uncomfortable_fix at center, Blur with dissolve
    else:
        show player_female_home_uncomfortable_fix at center, Blur with dissolve

    menu :
        "Aku memilih untuk..."
        "Membuat jadwal untuk mengerjakan tugas tersebut, misalnya membuat sketsa kasar pada hari pertama, merealisasikan sketsa kasar pada hari kedua, finishing pada hari ketiga.":
            $ vjp += 1
        "Mengerjakan tugas sesuai mood dan ide yang muncul, jika di tengah pengerjaan tugas mendapatkan ide baru bisa saja ide baru tersebut diterapkan pada tugas yang dibuat":
            $ vjp += 2
    
    scene buku tersusun rapi di meja with fade
    if vtf==1:
        show gambar_presisi at abscenter
    else:
        show gambar_imajinatif at abscenter
    show a_grade:
        xalign 0.4
        yalign 0.4
    
    "Hari-hari berlalu, tugas seni lukis pun akhirnya berhasil di selesaikan, dan aku mendapat nilai “A” dari guru."
    "Hasil karya tersebut rencananya akan dipajang di mading sekolah, satu kelaspun memberikan tepuk tangan yang meriah kepadaku."
    jump result
        
        

label result:
    python:
        if vei == 1:
            vei = "E"
        else: vei= "I"
        if vsn == 1:
            vsn = "S"
        else: vsn = "N"
        if vtf == 1:
            vtf = "T"
        else: vtf = "F"
        if vjp == 1:
            vjp = "J"
        else: vjp = "P"
        personality_type = vei + vsn + vtf + vjp
    
    scene kamar with fade
    if gender=="L":
        show player_male_home_neutral_fix at center, Normal with dissolve
    else:
        show player_female_home_neutral_fix at center, Normal with dissolve
    call screen result
    # p "Ternyata saya adalah seorang [personality_type]"
    # $ save_to_db(player_name, personality_type) # Call the save function
    
    scene black with fade
    call screen kredit
    




label splashscreen:
    
    scene black
    #with Pause(1)

    show image "barescrim_shield.png" at abscenter with Fade(1,2,2)
    #with Pause(2)

    hide image "barescrim_shield.png" with Dissolve(2)

    #with Pause(1)

    return