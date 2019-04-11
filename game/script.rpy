# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    show bckgrnd

    show desk
    play music "main.mp3"

    define a = Character("Agent")
    define c = Character("Client")
    define i = Character("Instructor")
    define s = Character("**Scene**")


# The game starts here.

#label start:
    
    show really at left with moveinleft:
        xzoom 0.5 yzoom 0.5

    i "Hi Future Agent ... Today I'm gonna be your instructor."
    i "We're going to simulate some several scenes and see whether you're going to choose the right desicion or not."
    i "And based on your tests, I'm gonna help you improve your level so it can be more and more adaptive with every case you'll face in the future."
    
    hide really
    show hmm at left:
        xzoom 0.5 yzoom 0.5

    i "What do you think ? Do you want to start ?"

    menu:
        "Yes":
            jump yes
        "No":
            jump no

    label yes:
        i "Please choose what chapter you want to play first."
        hide hmm
        menu:
            "Introduction":
                jump begin
            "Chapter 1":
                jump yes22
    label no:
        hide hmm
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Oh !"
        hide shocked
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Maybe next time."
        return

 # intro tuto chap -youssef-       


label begin:    
    hide really
    s "The client enters ..."

    show really at left:
        xzoom 0.5 yzoom 0.5

    i "Smile so he can feel comfortable in your presence."
    i "Did he smile back ?"

    hide really
    show hmm at left:
        xzoom 0.5 yzoom 0.5

    menu :
        "Yes":
            jump yes1
        "No":
            jump no2
    label yes1:
        i "Lucky you. This means he's having a good day."
        hide hmm
        show really at left:
            xzoom 0.5 yzoom 0.5
        jump action
    label no2:
        i "This means he's having a bad day. You may face some problems dealing with him."
        hide hmm
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Don't panic. We'll see how to deal with that."
        jump action

label action:
    show really at left:
            xzoom 0.5 yzoom 0.5
    i "Here he comes ... see you !"
    hide really
    hide shocked
    show normal at right behind desk with moveinright:
        xzoom 0.5 yzoom 0.5
    c "Good morning Sir"
    show speaking_1 at right behind desk:
        xzoom 0.5 yzoom 0.5
    a "Hey, welcome ... How are you ?"
    hide speaking_1
    show speaking_2 at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Good thanks ... How about you ?"
    hide speaking_2
    show speaking_3 at right behind desk:
        xzoom 0.5 yzoom 0.5
    a "I am doing well thanks"

label qst1:
    hide shocked
    hide angry
    show speaking_3 at right behind desk:
        xzoom 0.5 yzoom 0.5
    a " How can I help you ?"
    c "I want to insure my car"
    menu:
        "Which insurance service do you want to benefit from ?":
            jump QestA
        "Do you already have any experience with any other insurance agency ?":
            jump QestB
        "How can I help you ?":
            jump QestC
        "Have you ever insured in our agency ?":
            jump QestD
    label QestA:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice ... let's repeat it again."
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst1
    label QestB:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Nice move"
        hide really
        a "Do you already have any experience with any other insurance agencies ?"
        show speaking_1 at right behind desk:
            xzoom 0.5 yzoom 0.5
        hide really
        jump qst2
    label QestC:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice ... let's repeat it again."
        jump qst1
    label QestD:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice ... let's repeat it again."
        jump qst1
label qst2:
    hide shocked
    hide angry
    show sad at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Yes i had a bad experience, cause those agencies seek nothing but profit, they don't care about their clients."
    menu:
        "Whould you mind telling me why ?":
            jump QestE
        "I totaly disagree":
            jump QestF
        "We are not like others":
            jump QestG
        "No, insurance agencies are looking just for profit":
            jump QestH
    label QestE:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Nice move again ..."
        show speaking_1 at right:
            xzoom 0.5 yzoom 0.5
        hide really
        a "Would you mind telling me why you have this impression on insurance agencies."
        jump qst3
    label QestF:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice"
        show shocked at left:
            xzoom 0.5 yzoom 0.5

        jump qst2
    label QestG:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice"
        show shocked at left:
            xzoom 0.5 yzoom 0.5

        jump qst2
    label QestH:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice"
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst2
label qst3:
    hide shocked
    hide angry
    show sad at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "I had an accident, but my formal insurance agency didn't cover my losts."
    menu:
        "So ? What do you know about our agency ?":
            jump QestI
        "We are different from other agencies":
            jump QestJ
        "That's too bad":
            jump QestK
    label QestI:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Nice !! you're so good."
        hide really
        show speaking_1 at right behind desk:
            xzoom 0.5 yzoom 0.5
        a "So ? What do you know about our agency ?"
        jump qst4
    label QestJ:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_1
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad decision ... let's repeat."
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst3
    label QestK:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_1
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Not Quite!"
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst3
    label QestL:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_1
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Let's try that again !"
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst3
label qst4:
    hide shocked
    hide angry
    show shy at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Not too much, but I think you're not that different."
    menu:
        "You are wrong":
            jump QestM
        "I totaly understand, but we have some offers that may satisfy you. Tell me about your needs.":
            jump QestN
    label QestM:
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Wrong"
        jump qst4
    label QestN:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Perfect"
        show really at left:
            xzoom 0.5 yzoom 0.5
        jump qst5
label qst5:
    hide really
    hide shocked
    hide angry
    show speaking_2 at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "I want an insurance plan for every risk or damage my vehicle may take, but it should be less cheaper and with exactly the same features my formal insurance gave me."
    menu:
        "What are you asking sir is insane.":
            jump QestO
        "We have exactly what are you looking for. And it is much more cheaper than what provides your formal insurance agency.":
            jump QestP
        "Yes, we can provide you with that insurance plan, but it will cost you a bit.":
            jump QestQ
    label QestO:
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Not Quite."
        jump qst5
    label QestP:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Awesome !"
        hide really
        jump qst6
    label QestQ:
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Not the perfect choice."
        jump qst5
label qst6:
    a "We have exactly what are you looking for. And it is much more cheaper than what provides your formal insurance agency."
    show speaking_1 at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Awesome, I want to sign up for it."
    a "Sure thing sir, our offer fits people with needs as yourself, now about the documents that we'll need."
    show hmm at left:
        xzoom 0.5 yzoom 0.5
    i "Good job ... see you in the next chapter."
    hide hmm
    hide speaking_1
    hide shy
    hide speaking_3
    hide speaking_2
    hide sad
    hide normal
    hide angry
    hide thinking


 #start of chapter 1 -authorkhalil-

    s " Do you want to start this chapter !"
    
    menu:
        "Yes":
            jump yes22
        "No":
            jump no22

    label yes22:
        
        show inshappy at left:
            xzoom 0.1 yzoom 0.1
        i "I'll be your instructor for this chapter, i hope we will get along !"
        jump begin2
    label no22:     
        return

    
label begin2:    
    hide inshappy
    s "Client enters !"

    show bmad at center behind desk with moveinright:
        xzoom 0.2 yzoom 0.2
    c "..."
    a " Welcome sir ... can I help you ? "
    c "Yeah, you gave me the wrong papers yesterday !  "
    show insnormal at left:
        xzoom 0.1 yzoom 0.1
    i "Let’s face it ! Sometimes, we screw something up. It’s Okay, we’re only human! "
    i "However, you need to be transparent when making mistakes."
    hide insnormal

    label qu2:
        menu:
            "Be aggressive !":
                jump agro
            "Run to your boss in fear !":
                jump fearo
            "Apologize and try to resolve the problem peacefully !":
                 jump peaco
        label agro:
            a "It's your fault for not paying attention."
            a "Get lost !"
            show inshock at left:
                xzoom 0.1 yzoom 0.1
            i " Trust me ! Being aggressive won't solve the problem, it will just make it worse. "
            hide inshock
            jump qu2
        label fearo:
            a "Boss ! help me !"
            show inshock at left:
                xzoom 0.1 yzoom 0.1
            i "Running away is not the solution this time !"
            hide inshock
            jump qu2
        label peaco:
            a "I’m really sorry, sir. I've made a mistake, I will fix it immediately ! "
            a "it may take up a few minutes to prepare your papers. I will assure you this won't happen again."
            hide bmad
            show bnormal at center behind desk:
                xzoom 0.2 yzoom 0.2
            c "We're gonna see about that ! "
            show insnormal at left:
                xzoom 0.1 yzoom 0.1
            i "Millennials right !!"
            i "Don't let him provoke you, and keep your calm.That's the best way to deal with the situation."
            i "And of course ! don't forget to smile "

            s "After 15 minutes."

            i "Now the customer's papers are ready, what's next is to win his trust again !"
            show inshappy at left:
                xzoom 0.1 yzoom 0.1
            i "Let's see how you're going to do that !"
            hide inshappy

    label qu3 :
        menu:
            "Give the papers in silence":
                jump silco
            "Apologize again ":
                jump sorro
            "Empathize with the client":
                jump plz
        label silco :
            a "..."
            hide bnormal
            show bmad at center behind desk:
                xzoom 0.2 yzoom 0.2
            c "Such a waste of my time !!"
            c "I hope this time you got it right."
            show insnormal at left:
                xzoom 0.1 yzoom 0.1
            i "Silence could be a good option, but there is a strong chance, "
            i "that you will lose your client !"
            hide insnormal
            jump qu3
        label sorro :
            a "I apologize again if I have caused you any inconvenience. "
            hide bnormal
            show bmad at center behind desk:
                xzoom 0.2 yzoom 0.2
            c "That's right, now give me those papers !"
            show insnormal at left:
                xzoom 0.1 yzoom 0.1
            i "mmm, apologizing again won't do the trick !"
            hide insnormal
            jump qu3
        label plz :
            a "Here is your papers sir !"
            a "I can see why you'd be frustrated ... I'd be upset too if that happened to me !"
            c "... I am glad that you understand that it is your fault!"
            c "but I'll give you credit for your service, bye !"
            show inshappy at left:
                xzoom 0.1 yzoom 0.1
            i "Empathazing with the client may sound childish, but it is a well known customer service skills "
            i "I am very proud of you agent, you did well managing the situation !"
            i "I'll see you in the next chapter !"
            hide bmad 
    
    # chapter 2 en cours -author X-
    # tourist girl motorcycle insurance ! (3 choices)

        







        


        








    stop music fadeout 1.0
    show insnormal at left:
        xzoom 0.1 yzoom 0.1
    i "Thanks for playing , come again !! "
    return