
def login_req(func):
    def inner(islogin):
        if islogin ==False:
            print('Login required')

        else :
            return func(islogin)    
    return inner

# @login_req
def home_page(islogin):
    print("Home page")
home_page(True)    

# @login_req
def About_page(islogin):
    print("about page")
About_page(False)    


@login_req
def order_page(islogin):
    print("order page")
order_page(False)


# Home page
# about page
# Login required