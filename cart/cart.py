class Cart():
    def __init__(self,request) :
        self.session=request.session

        # wenn es eine session gibt
        cart=self.session.get('session_key')

        if 'session_key' not in cart:
            cart=self.session['session_key'] = {}

        # make sure that cart session is everey where availible on the websitee
        
        self.cart=cart