Create_Buyer_Account_Page:


<First_Page_Widgets>:
    orientation: "vertical"
    spacing:"10dp"
    Label:
        text:"GrapNGo"
        font_size: "65sp"
        color: [0.5,0.4,0.8,1]
        size_hint_y: 1
        size_hint_x: 1
        bold: True

    Image:
        source: "C:/Users/LENOVO/Pictures/logo.png"
        size_hint_y: 0.8
        size_hint_x: 0.8
        allow_strech: True
        keep_ration:True
        pos_hint: {'center_x': 0.5}

    Label:
        text: "Connecting you to a Global market"
        color: [0,0,0,1]
        font_size: "30sp"
        size_hint_y: 1
        size_hint_x: 1

    Button:
        text: "Login as a buyer"
        size_hint_y: 0.5
        size_hint_x: 0.5
        vallign: "center"
        background_color: [.1,.8,.6,1]
        pos_hint: {'center_x': 0.5}



    Button:
        text: "Login as a seller"
        size_hint_y: 0.5
        size_hint_x: 0.5
        vallign: "center"
        background_color: [.1,.8,.6,1]
        pos_hint: {'center_x': 0.5}




    Label:
        text: "Don't have an account yet"
        font_size: "15sp"
        color: [0,0,0,1]
        size_hint_y: 0.3
        size_hint_x: 0.3

    Button:
        text: "Create a buyer account"
        size_hint_y: 0.3
        size_hint_x: 0.3
        background_color: [.8,.3,.2,1]
        pos_hint: {'center_x': 0.3}



    Button:
        text: "Create a seller account"
        size_hint_y: 0.3
        size_hint_x: 0.3
        background_color: [.8,.3,.2,1]
        pos_hint: {'center_x': 0.3}

<Login_Page>:
    orientation: "vertical"
    BoxLayout:
        orientation: "vertical"
        size_hint: ("1dp","0.25dp")
        Label:
            text:"GrapNGo"
            font_size: "65sp"
            color: [0.7,0.7,0.8,1]
            size_hint_y: 1
            size_hint_x: 1
            bold: True
            pos_hint: {'center_x': 0.5}


        Label:
            text: "Buyer Login"
            bold: True
            font_size: "40sp"
            pos_hint: {'center_x': 0.3}
            color:[0,0,0,1]

        Label:
            text: "Enter your infomation"
            color: [0.2,0.7,0.8,1]
            font_size: "25sp"
            pos_hint: {'center_x': 0.2}



    BoxLayout:
        orientation:"vertical"
        size_hint: ("1dp","0.65dp")
        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter your Full Name"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: name
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter your Email"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: email
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1


        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter a password"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: password
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

 

        Button:
            text: "Forgot password"
            size_hint_y: 0.3
            size_hint_x: 0.3
            background_color: [.8,.3,.2,1]
            pos_hint: {'center_x': 0.2}

        Label:
            text:""

        Button:
            text: "Login"
            size_hint_y: 0.7
            size_hint_x: 0.3
            background_color: [.4,.5,.8,1]
            pos_hint: {'center_x': 0.2}

        

<Create_Buyer_Account_Page>:
    orientation: "vertical"
#    color: [0.7,0.7,0.8,1]
    BoxLayout:
        orientation: "vertical"
        size_hint: ("1dp","0.25dp")
        Label:
            text:"GrapNGo"
            font_size: "65sp"
            color: [0.7,0.7,0.8,1]
            size_hint_y: 1
            size_hint_x: 1
            bold: True
            pos_hint: {'center_x': 0.5}


        Label:
            text: "Create Buyer Account"
            bold: True
            font_size: "40sp"
            pos_hint: {'center_x': 0.3}
            color:[0,0,0,1]

        Label:
            text: "Enter your infomation"
            color: [0.2,0.7,0.8,1]
            font_size: "25sp"
            pos_hint: {'center_x': 0.2}



    BoxLayout:
        orientation:"vertical"
        size_hint: ("1dp","0.65dp")
        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter your Full Name"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: name
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter your Email"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: email
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter your Phone number"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: phone
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter your Location"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: location
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

        BoxLayout:
            orientation:"horizontal"
            spacing: "10dp"

            Label:
                color: [0,0,0,1]
                text: "Enter a password"
                font_size: "25sp"
                pos_hint: {'center_x': 0.3}

            TextInput:
                id: password
                font_size: 25
                size_hint_y: 0.6
                readonly: False
                hallign: "right"
                multiline: False
                background_color: [0.2,0.2,0.2,1]
                foreground_color: [1,1,1,1]
                color: 0,1,1,1

 

        Button:
            text: "Forgot password"
            size_hint_y: 0.3
            size_hint_x: 0.3
            background_color: [.8,.3,.2,1]
            pos_hint: {'center_x': 0.2}

        Label:
            text:"Entering your location helps us know where you are/nso as to locate the clossest services to you"
            font_size:"15sp"
            color: [0,0,0,0]

        Button:
            text: "Create Account"
            size_hint_y: 0.7
            size_hint_x: 0.3
            background_color: [.4,.5,.8,1]
            pos_hint: {'center_x': 0.2}

        

            


        

    

    

        
