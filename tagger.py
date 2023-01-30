while True:
    word=input("Enter the word ")
    gha2b=["هو","هي","هم","هن","هما"]
    eshara=["هذا","هذه","تلك","اولئك","ذلك","هذان","هاتان","هؤلاء","هولاء"]
    mukhatb=["انت","انتَ","انتِ","انتي","انتما","انتم","انتن","أنت","أنتَ","أنتِ","أنتي","أنتما","أنت","أنتن","أنتم"]
    mutklm=["انا","نحن","أنا"]
    algr=["في","من","الى","عن","على"]
    musol=["الذي","التي","اللذان","اللتان","اللذين","اللتين","اللائي","اللاتي","اللواتي","الذين"]
    ataf=["و","ثم","أو","ف","حتى","أم","بل","لا","لكن"]
    makan=["فوق","تحت","أمام","امام","خلف","بين",]
    present=["أ","ن","ي","ت"]
    taksir =["نساء","شيخة","ثيرة","كملة","عملة","فتية","غلمة","صبية","شجعة","غزلة","ولدة","جلّة","علية","سفلة","حُمُر","حمر","صُبُر","كُتب","كُتُب",
             "عُور","ُصحف","صحف","عمد","عُمد","خشب","خَشب","خُشب","غرف","غُرف","إخوة","جيرة","كلاب","بذور","بذور","علوم","برود","نمور",
             "تيجان","حيتان","علمان","دببة","قرطة","قضبان","حملان","ركبان","عدد","ُعُدد","غرف","غُرف","كبر","كُبر","كتب","حروف","سدر","خرق","حمر","حُمر",
             "صم","بكم","صُم","بُكم","قضب","قُضب","رُكع","نُوم","صُوم","جهلة","بررة","كفرة","كرماء","شهداء","فقراء","وزراء","امراء","رئساء","مرضى","سكرى",
             "موتى","العباقرة","حمقى","قرى","طرق","الدمى","عيون","كفوف","اشواق","السبل","سُبل","عُدد","عُرى","سِدر","خِرق","لُعب","موتى","عطشى","حمقى",
             "قتلى","زمنى","أسود","نيران","أجنحه","قطط","خلفاء","الصقور","موز","جزر","أُفق","فساتين","بساتين"]

    mufrad=["تكبير","تخدير","تسليم","تحنيط","تخلف","تشتت","تدبر","قران","تعليم","تفسير","جهاز","خروف","يد","لون","دون","كون","نون","يون","يابس","جدار","صُمود","يتيم","يمين","يسار","يوم","يربوع","يخت","يانسون","يوسقي","يام","أثارة","يابان",
            "يمن","يونان","تاجر","تمساح","توت","تفاح","تمر","تين","تليفون","تنين","تونه","تيس","تاج","كتاب","شهاب","سلام","سفاح","سلاح","جراح","جهاد","صلاة","فنان"]
    dic={"اُكتب":"فعل امر للمفرد المذكر","أَكتب":"فعل مضارع للمفرد المتكلم","أفضل":"فعل او اسم ","أحسن":"فعل او اسم","اشرف":"فعل او اسم","أبقى":"فعل او اسم",
         "الأفضل":"اسم تفضيل معرف","الأحسن":"اسم تفضيل معرف","الأشرف":"اسم تفضيل معرف","الأبقى":"اسم تفضيل معرف","أنفع":"فعل او اسم","الأنفع":"اسم تفضيل معرف",
         "أدق":"اسم او فعل","الأدق":"اسم تفضيل معرف","أبرد":"اسم او فعل","الأبرد":"اسم تفضيل معرف","أنمّ":"اسم او فعل","الأنم":"اسم تفضيل معرف","أكتم":"اسم نكرة او فعل",
         "أبهى":"اسم نكرة او فعل","الأبهى":"اسم تفضيل معرف","أكل":"اسم نكرة او فعل","كُل":"فعل أمر  للمفرد المذكر","كُلي":"فعل أمر للمفرد المؤنث","الأكل":"جمع تكسير معرف",
         "أبعد":"اسم نكرة او فعل","الأبعد":"اسم  تفضيل معرف","ذَاكر":"فعل أمر او فعل ماضي","و":"حرف عطف","يا":"للنداء البعيد والقريب","اي":"للنداء القريب",
         "أيا":"للنداء البعيد","هيا":"للنداء البعيد","الله":"لفظ الجلاله اسم علم مفرد","اللهم":"أسلوب نداء للدعاء ومعناه يا الله","يارب":"اسلوب نداء للدعاء",
         "أشرف":"اسم تفضيل نكرة او فعل","الأشرف":"اسم تفضيل معرف","يرقة":"اسم منكرة مفرد مؤنث","اليرقة":"اسم معرف مفرد مذكر","يمامة":"اسم نكرة مفرد ",
         "اليمامة":"اسم معرف مفرد","أُكتب":"فعل امر للمفرد المذكر","قُل":"فعل أمر للمفرد المذكر","أُكتبي":"فعل امر للمفرد المؤنث",
         "قُلي":"فعل أمر للمفرد المؤنث","كُل":"فعل امر للمفرد المذكر","كُلي":"فعل أمر للمفرد المؤنث","كلوا":"فعل أمر للجمع المذكر","قُلوا":"فعل أمر للجمع المذكر",
         "تكاد":"فعل مضارع للمفرد المؤنث","وراء":"اسم نكرة مفرد وظرف مكان","شمال":"اسم نكرة مفرد وظرف مكان","جنوب":"اسم نكرة مفرد وظرف مكان",
         "شرق":"اسم نكرة مفرد وظرف مكان","غرب":"اسم نكرة مفرد وظرف مكان","الوراء":"اسم معرف مفرد وظرف مكان","الشمال":"اسم معرف مفرد وظرف مكان",
         "الجنوب":"اسم معرف مفرد وظرف مكان","الشرق":"اسم معرف مفرد وظرف مكان","الغرب":"اسم معرف مفرد وظرف مكان","وسط":"اسم نكرة مفرد وظرف مكان",
         "الوسط":"اسم معرف مفرد وظرف مكان","فستان":"اسم نكرة مفرد مؤنث","الفستان":"اسم معرف مؤنث مفرد",}
    if word in dic :
        print(dic[word])
        continue
    if word in mufrad or word[2:] in mufrad  :
            if word[0:2]=="ال":
                if word[-1]=="ة" and word[0:2]=="ال":
                   print("اسم معرف مفرد مؤنث")
                   continue
                else:
                    print("اسم معرف مفرد مذكر")
                    continue
                
            else :
                if word[-1]=="ة":
                    print("اسم نكرة مفرد مؤنث")
                    continue 
                else:
                    print("اسم نكرة مفرد مذكر")
                    continue
    if word in taksir or word[2:] in taksir  :
            if word[0:2]=="ال":
                print ("جمع تكسير معرف")
                continue 
            else :
                print("جمع تكسير نكرة")
                continue


    if word[0:3]=="الأ":                      #الأفعال
        if len(word)==7 and word[-2]=="ا":
            print("جمع تكسير معرف")
            taksir.append(word)
            continue 

        if len(word)==7 and word[-1]=="ة":     # الأفعلة
            print("جمع تكسير معرف")
            taksir.append(word)
            continue 

           
    if word[0]=="أ" and len(word)==4  and word[1]!="ُ" :#أفعل
        if word not in mukhatb:
            print("جمع تكسير نكرة")        
            taksir.append(word)

    elif len(word)==5 and word[-2]=="ا" and word.startswith("أ") :            # أفعال
            print("جمع تكسير نكرة")
            taksir.append(word)

    elif word[-1]=="ة" and word.startswith("أ"):               #افعلة
        print("جمع تكسير نكرة")
        taksir.append(word)
 
    elif word[0:3]=="الأ"and len(word)==6:    #الأفعل
        print("جمع تكسير معرف")
        taksir.append(word)

    
    elif len(word)==6 and word.endswith("اء") and word.startswith("أ"):         #افعلاء
            print ("جمع تكسير نكرة")
            taksir.append(word)

    elif len(word)==8 and word.endswith("اء") and word.startswith("الأ"):         #الأفعلاء
            print("جمع تكسير معرف")
            taksir.append(word)
 
    elif  word[-2]=="و"and word[1]=="ُ":         #فُعول
        print("جمع تكسير نكرة")
        taksir.append(word)
 
    elif word[-2]=="و"and word[0:2]=="ال" and word[3]=="ُ":   #الفُعول
            print("جمع تكسير معرف")
            taksir.append(word)

    elif word[-2:]=="ان":
        if word[1]=="ِ" or word[1]=="ُ":      # فِعلان و فُعلان
            print("جمع تكسير نكرة")
            taksir.append(word)

    elif word[-2:]=="ان"and word[0:2]=="ال" :
        if word[3]=="ِ" or word[3]=="ُ":     #الفِعلان و الفُعلان
            print("جمع تكسير معرف")
            taksir.append(word)

    elif len(word)==4 and word[-2]=="ا"and word[0]!="أ" and word[-2:]!="اء"and word[-2:]!="ان":    #فعال
            print("جمع تكسير نكرة")
            taksir.append(word)

    elif len(word)==6 and word[-2]=="ا" and word.startswith("ال"):#الفعال
        if word[-2:]!="ات" and word[-2:]!="ان" and word[-2:]!="اء":
            print("جمع تكسير معرف")
            taksir.append(word)
    elif len(word)==5 and word[2]=="ا"and word[0]=="أ":   #أفاعل
        print("جمع تكسير نكرة")
        taksir.append(word)
    elif len(word)==7 and word[4]=="ا"and word[0:3]=="الأ": #الأفاعل
        print("جمع تكسير معرف")
        taksir.append(word)
    elif word[-2:]=="اء"and word[1]=="ُ":   #فُعلاء
        print("جمع تكسير نكرة")
        taksir.append(word)
    elif word[-2:]=="اء" and word[3]=="ُ" and word.startswith("ال"): #الفُعلاء
        print("جمع تكسير معرف")
        taksir.append(word)

    
    

    if word in taksir:  # للمنع بين الجمع التكسير والباقي
        continue

    if word in algr:     #حروف الجر
        print("حرف جر")
        continue
    if word in ataf: #حروف العطف
        print("حرف عطف")
        continue
    if word in makan:#ظروف المكان
        print("ظرف مكان")
        continue 

    
    elif word in gha2b:                  #ضمائر الغائب
        if word == "هو":
            print("ضمير غائب للمفرد المذكر")
        elif word == "هي":
            print("ضمير غائب للمفرد المؤنث")
        elif word == "هم":
            print("ضمير غائب للجمع الذكر")
        elif word == "هن":
            print("ضمير غائب للجمع المؤنث")
        elif word == "هما":
            print("ضمير غائب للمثنى المذكر والمؤنث")


    elif word in eshara:  #اسماء الاشارة
        if word=="هذا":
            print("اسم اشارة للمفرد المذكر القريب")
        elif word=="هذه":
            print("اسم اشارة للمفرد المؤنث القريب")
        elif word=="هذان":
            print("اسم اشارة للمثنى المذكر القريب")
        elif word=="هاتان":
            print("اسم اشارة للمثنى المؤنث القريب")
        elif word=="هؤلاء"or word=="هولاء":
            print("اسم اشارة للجمع المذكر والمؤنث")
        elif word=="ذلك":
            print("اسم اشارة للمفرد المذكر البعيد")
        elif word=="تلك":
            print("اسم شارة للمفرد المؤنث البعيد")
        elif word=="اولئك":
            print("اسم اشارة للجمع البعيد")
            
            
    elif word in mukhatb:                         #ضمائر المخاطب
        if word == "انت" or word == "انتَ":
            print("ضمير مخاطب للمفرد المذكر")
        elif word == "أنت" or word == "أنتَ":
            print("ضمير مخاطب للمفرد المذكر")    
        elif word == "انتي" or word == "انتِ":
            print("ضمير مخاطب للمفرد المؤنث")
        elif word == "أنتِ" or word == "أنتي":
            print("ضمير مخاطب للمفرد المؤنث") 
        elif word == "انتم" or word=="أنتم":
            print("ضمير مخاطب للجمع المذكر")
        elif word == "انتن" or word=="أنتن":
            print("ضمير مخاطب للجمع المؤنث")
        elif word == "انتما" or word=="أنتما":
            print("ضمير مخاطب للمثنى المذكر والمؤنث")
            

    elif word in mutklm:              #ضمائر المتكلم
        if word =="انا"or word=="أنا":
            print("ضمير متكلم للمفرد المذكر والمؤنث")
        elif word =="نحن":
            print("ضمير متكلم للجمع الذكر والمؤنث")

    elif word in musol:                        #الاسماء الموصوله
        if word == "الذي":
            print("اسم موصول للمفرد المذكر")
        elif word == "التي":
            print("اسم موصول للمفرد المؤنث")
        elif word == "الذين":
            print("اسم موصول للجمع المذكر")
        elif word == "اللائي" or word=="اللاتي" or word =="اللواتي":
            print("اسم موصول للجمع المؤنث")
        elif word == "اللذان" or word =="اللذين":
            print("اسم موصول للمثنى المذكر")
        elif word =="اللتان" or word =="اللتين" :
            print("اسم موصول للمثنى المؤنث")

            
    else :     #الافعال المضارعة واوانوعها
        
        if word[0]=="ي" and word.endswith("ون")or word[0]=="ي"  and word.endswith("وا")  :
            print("فعل مضارع للجمع الذكر")
            continue
        elif word.startswith("ت")and word.endswith("ن")and word[-2:]!=("ان") :
            print("فعل مضارع للجمع المؤنث")
            continue
        elif word.startswith("ي")and word.endswith("ن")and word[-2:]!=("ان") :
            print("فعل مضارع للجمع المؤنث")
            continue
        elif word.endswith("ان")and word.startswith("ي"):
            print("فعل مضارع للمثنى المذكر")
            continue 
        elif word.endswith("ان")and word.startswith("ت"):
            print("فعل مضارع للمثنى المؤنث")
            continue
        elif word[0]=="أ"and word[1]=="َ":
            print("فعل مضارع للمفرد المتكلم")
            continue
        elif word[0]=="ن"and word[1]=="َ":
            print("فعل مضارع للجمع المتكلم")
            continue 
            
        else:
            if word.startswith("ي"):
                print("فعل مضارع للمفرد المذكر")
                continue
            elif word.startswith("ت") and word[-1]!="ة" and word[-4]!="ا":
                print("فعل مضارع للمفرد المؤنث")
                continue


        if word[0]=="س"and word[1] in present:            #المستقبل
            word=word[1:]
            if word[0]=="ي" and word.endswith("ون")or word[0]=="ي"  and word.endswith("وا")  :
                print("فعل مستقبل للجمع المذكر")
                continue
            elif word.startswith("ت")and word.endswith("ن")and word[-2:]!=("ان") :
                print("فعل مستقبل للجمع المؤنث")
                continue
            elif word.startswith("ي")and word.endswith("ن")and word[-2:]!=("ان") :
                print("فعل مستقبل للجمع المؤنث")
                continue
            elif word.endswith("ان")and word.startswith("ي"):
                print("فعل مستقبل للمثنى المذكر")
                continue
            elif word.endswith("ان")and word.startswith("ت"):
                print("فعل مستقبل للمثنى المؤنث")
                continue
            elif word[0]=="أ":
                print("فعل مستقبل للمفرد المتكلم")
                continue
            elif word[0]=="ن":
                print("فعل مستقبل للجمع المتكلم")
                continue 
            else:
                if word.startswith("ي"):
                    print("فعل مستقبل للمفرد المذكر")
                    continue
                elif word.startswith("ت") and word[-1]!="ة" and word[-4]!="ا":
                    print("فعل مستقبل للمفرد المؤنث")
                    continue
            




        if word[0]not in present and word[1]=="َ":        #الفعل الماضي بأنواعه
            if word[-1]=="ت":
                print("فعل ماضي للمفرد المؤنث")
            elif word[-2:]=="وا":
                print("فعل ماضي للجمع المذكر")
            elif word[-1]=="ن":
                print("فعل ماضي للجمع المؤنث")
            elif word[-1]=="ا":
                print("فعل ماضي للمثنى")
            else:
                print("فعل ماضي للمفرد المذكر")
            continue



        if word[0]=="ا"and word[1]=="ُ" or word[0:2]=="اِ":    #الامر
            if word[-1]=="ي":
                print("فعل أمر للمفرد المؤنث")
                continue
            elif word [-2:]=="وا":
                print("فعل أمر للجمع المذكر")
                continue
            elif word[-1]=="ن":
                print("فعل أمر للجمع المؤنث")
                continue
            elif word[-1]=="ا":
                print("فعل أمر للمثنى ")
                continue
            else:
                print("فعل أمر للمفرد المذكر")
                continue
        
        if word.startswith("ال"):     #الاسماء المعرفة وانواعها
            if  word.endswith("تان")  :
                print("اسم معرف مثنى مؤنث")
            elif word.endswith("ان"):
                print("اسم معرف مثنى مذكر")
            elif word.endswith("ون"):
                print("اسم معرف جمع مذكر")
            elif word.endswith("َين"):
                print("اسم معرف جمع مذكر")
            elif word.endswith("َين"):
                print("اسم معرف مثنى مذكر")
            elif word.endswith("ين"):
                print("اسم معرف جمع او مثنى مذكر")
            elif word.endswith("ات"):
                print("اسم معرف جمع مؤنث")
            elif len(word)==7 and word[-3]=="ا" and word[-1]!="ة":
                print("اسم معرف جمع تكسير")
            elif len(word)==8 and word[-4]=="ا" and word[-1]!="ة":
                print("اسم معرف جمع تكسير")
            else:
                if word.endswith("ة") or word.endswith("اء") or word.endswith("ى") :
                    print ("اسم معرف مفرد مؤنث")
                else :
                    print("اسم معرف مفرد مذكر")

                    
        else: #الاسماء النكرة وانواعها
            if word.endswith("تان")  :
                print("اسم نكرة مثنى مؤنث")
            elif word.endswith("ان"):
                print("اسم نكرة مثنى مذكر")
            elif word.endswith("ون"):
                print("اسم نكرة جمع مذكر")
            elif word.endswith("َين"):
                print("اسم نكرة جمع مذكر")
            elif word.endswith("َين"):
                print("اسم نكرة مثنى مذكر")
            elif word.endswith("ين"):
                print("اسم نكرة جمع او مثنى مذكر")
            elif word.endswith("ات"):
                print("اسم نكرة جمع مؤنث")
            elif len(word)==5 and word[2]=="ا" and word[-1]!="ة" :
                print("اسم نكرة جمع تكسير")
            elif len(word)==6 and word[-4]=="ا" and word[-1]!="ة" :
                print("اسم نكرة جمع تكسير")
            else:
                if word.endswith("ة") or word.endswith("اء") or word.endswith("ى") :
                    print ("اسم نكرة مفرد مؤنث")
                else :
                    print("اسم نكرة مفرد مذكر")
        
            
        
            
        
            
            
                
        
        
    
