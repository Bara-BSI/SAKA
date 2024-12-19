
# Inisialisasi pra game.

init:
    python:
        persistent.first_main_menu = True  # Tracks initial main menu visit

        import mysql.connector  # Install using 'pip install mysql-connector-python'
    
        def save_to_db(player_name, personality_type):
            #try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="pmaUser",
                password="pma",
                database="data_mbti",
                charset = "utf8mb4",
                collation = "utf8mb4_unicode_ci"

            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO player_info (name, gender, personality) VALUES (%s, %s, %s)"
            val = (player_name, gender, personality_type)
            mycursor.execute(sql, val)
            mycursor.fetchall()
            mydb.commit()
            # print(mycursor.rowcount, "record inserted.")  # For debugging
            mycursor.close()
            mydb.close()
            #     mydb.commit()
            

            # except mysql.connector.Error as err:
            #     print("Something went wrong: {}".format(err))  # Handle errors appropriately
            # finally:
            #     if mydb.is_connected():
            #         mycursor.close()
            #         mydb.close()



# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# Deklarasikan karakter yang digunakan di game.
define player_name = None
screen gender:
    vbox:
        style_prefix "gender"
        xalign 0.5
        yalign 0.5
        
        text "Saya adalah seorang"
        textbutton "Laki-Laki" action SetVariable("gender", "L"), Return()
        textbutton "Perempuan" action SetVariable("gender", "P"), Return()
        #textbutton "Done" action Return()
style gender_button:
    xpos 30
    hover_background "button_hover.png"

style gender_button_text:
    outlines [(absolute(3), '#E78344', absolute(0), absolute(0))]
    hover_outlines [(absolute(3), '#E78344', absolute(0), absolute(0))]

style gender_text:
    size 44

# Tampilan pemilihan gambar
screen gambartf:
    vbox:
        style_prefix "gambartf"
        xalign 0.5
        yalign 0.5

        text "Saya memilih menggambar..."
        textbutton "Gambar Presisi" action SetVariable("vtf", 1), Return():
            background "images/Property/gambar_presisi.jpg"
            xsize 528
            ysize 377
        textbutton "":
            ysize 10
        textbutton "Gambar Imajinatif" action SetVariable("vtf", 2), Return():
            background "images/Property/gambar_imajinatif.jpg"
            xsize 528
            ysize 377

style gambartf_button_text:
    yalign 1.0
    xalign 0.5
    color "#000000"
    hover_color "#E78344"
    outlines [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]

style gambartf_text:
    size 44
    color "#000000"
    outlines [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]

# Tampilan hasil akhir
screen result:
    vbox:
        image "gui/textbox.png"
        xalign 0.5
        yalign 0.9
    vbox:
        style_prefix "result"
        xalign 0.5
        yalign 0.8

        text "[player_name] adalah seorang [personality_type]"
    vbox:
        style_prefix "result"
        textbutton "":
            action Return()

style result_text:
    size 44
    color "#000000"
    outlines [(absolute(1), "#FFFFFF", absolute(0), absolute(0))]

style result_button:
    background None
    xfill True
    yfill True

# Game dimulai disini.
transform shake_with_pause:
    pause 0.5
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 0 yoffset 0 
    pause 1
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 0 yoffset 0 
    pause 1
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 0 yoffset 0
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    xoffset 10 yoffset -10 
    pause 0.1 
    xoffset -10 yoffset 10 
    pause 0.1 
    pause 0.5
    
transform Blur:
    blur 5.0
transform Normal:
    blur 0

transform abscenter:
    xalign 0.5
    yalign 0.5

transform kremov:
    xalign 0.5
    ypos 1000
    linear 40.0 ypos -4000
    pause 5

screen kredit:
    vbox:
        style_prefix "kredit"
        xalign 0.5

        text "SAKA" at kremov:
            size 60
            bold True
        
        for i in range(4):
            text "" at kremov

        text "Credits" at kremov:
            size 40
            bold True
        text "" at kremov
        text "Project Management" at kremov:
            bold True
        text "Restu Ardi Putranto" at kremov
        text "" at kremov
        text "Character Designer" at kremov:
            bold True
        text "Christina Yuli Anggita" at kremov
        text "" at kremov
        text "Background Designer" at kremov:
            bold True
        text "Restu Ardi Putranto" at kremov
        text "" at kremov
        text "Music & SFX" at kremov:
            bold True
        text "Bara Rifki Annajib" at kremov
        text "" at kremov
        text "Story Board" at kremov:
            bold True
        text "Christina Yuli Anggita" at kremov
        text "" at kremov
        text "Programmer" at kremov:
            bold True
        text "Bara Rifki Annajib" at kremov

        for i in range(4):
            text "" at kremov

        text "Special Thanks" at kremov:
            bold True
        text "Anastasia Meyliana, S.Kom, M.Kom" at kremov
        text "Nani Purwati, S.Kom, M.Kom" at kremov

        for i in range(4):
            text "" at kremov
        
        text "Special Credits" at kremov:
            size 40
            bold True
        text "" at kremov
        text "" at kremov
        image "images/credit/renpy_logo.png" at kremov:
            xalign 0.5
        text "Renpy Game Engine" at kremov
        text "" at kremov
        text "" at kremov
        image "images/credit/medibang_logo.png" at kremov:
            xalign 0.5
        text "Medibang Paint Pro" at kremov
        text "" at kremov
        text "" at kremov
        image "images/credit/figma_logo.png" at kremov:
            xalign 0.5
        text "Figma" at kremov
        text "" at kremov
        text "" at kremov
        image "images/credit/notion_logo.png" at kremov:
            xalign 0.5
        text "Notion" at kremov

        for i in range(4):
            text "" at kremov
        
        text "A game by" at kremov
        text "BARESCRIM" at kremov:
            bold True
        text "" at kremov
        image "images/barescrim_bg_bk.png" at kremov

        for i in range(14):
            text "" at kremov

        text "Thank you for playing!" at kremov
        $ persistent.first_main_menu = True
    
    vbox:
        for i in range(95):
            text "" at kremov
        textbutton "" at kremov:
            action Return()
            xsize 1920
            ysize 1080
            # background "#FFFFFF" # For debugging purpose
            background None





        
        


style kredit_text:
    color "#FFFFFF"
    size 32
    font "droid-sans-mono/DroidSansMono.ttf"