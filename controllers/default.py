# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    if auth.user!=None:
        redirect(URL('default','homeFree'))
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


#home page for a free user
@auth.requires_login()
def homeFree():
    if auth.user.first_name=='admin':
        redirect(URL('default','admin'))
    message="hello. dis is your home page"
    row=db(db.auth_user.id==auth.user.id).select().first()
    if row.premium=='1':
        redirect(URL('default','homePremium'))
    userName=auth.user.first_name
    query=(auth.user.gender!=db.auth_user.gender) & (db.auth_user.religion==auth.user.religion) & (db.auth_user.caste==auth.user.caste)
    rows=db(query).select()
    return locals() 

#home page for a premium user
@auth.requires_login()
def homePremium():
    message ="this is home page of a premium user"
    userName=auth.user.first_name
    matches = {}
    query=(auth.user.gender!=db.auth_user.gender) & (db.auth_user.religion==auth.user.religion) & (db.auth_user.caste==auth.user.caste)
    rows=db(query).select()
    myInter=db(db.Interests.userId==auth.user.id).select().first()
    for row in rows:
        if row.premium=='1':
            tempRow=db(db.Interests.userId==row.id).select().first()
            if(tempRow.Reading==myInter.Reading):
                if row.id not in matches:
                    matches[row.id]=1
                else:
                    matches[row.id]=matches[row.id]+1

            if(tempRow.Music==myInter.Music):
                if row.id not in matches:
                    matches[row.id]=1
                else:
                    matches[row.id]=matches[row.id]+1

            if(tempRow.Movies==myInter.Movies):
                if row.id not in matches:
                    matches[row.id]=1
                else:
                    matches[row.id]=matches[row.id]+1

            if(tempRow.Travelling==myInter.Travelling):
                if row.id not in matches:
                    matches[row.id]=1
                else:
                    matches[row.id]=matches[row.id]+1

            if(tempRow.Fitness==myInter.Fitness):
                if row.id not in matches:
                    matches[row.id]=1
                else:
                    matches[row.id]=matches[row.id]+1


        if row.diet==auth.user.diet:
            if row.id not in matches:
                matches[row.id]=1
            else:
                matches[row.id]=matches[row.id]+1

        if row.smoke==auth.user.smoke:
            if row.id not in matches:
                matches[row.id]=1
            else:
                matches[row.id]=matches[row.id]+1

        if row.drink==auth.user.drink:
            if row.id not in matches:
                matches[row.id]=1
            else:
                matches[row.id]=matches[row.id]+1

        if row.bodyType==auth.user.bodyType:
            if row.id not in matches:
                matches[row.id]=1
            else:
                matches[row.id]=matches[row.id]+1

        if row.skinTone==auth.user.skinTone:
            if row.id not in matches:
                matches[row.id]=1
            else:
                matches[row.id]=matches[row.id]+1
    mIds=[]
    mCount=[]
    for i in matches:
        mIds.append(i)
        mCount.append(matches[i])
    

    i=0
    while i<len(mCount):
        j=0
        while j<len(mCount)-1:
            if mCount[j]<mCount[j+1]:
                temp=mCount[j]
                mCount[j]=mCount[j+1]
                mCount[j+1]=temp

                temp=mIds[j]
                mIds[j]=mIds[j+1]
                mIds[j+1]=temp
            j=j+1
        i=i+1
    return locals()


#profile view of a free user 
@auth.requires_login()
def myProfileFree():
    if auth.user.first_name=='  admin':
        redirect(URL('default','admin'))
    row=db(db.auth_user.id==auth.user.id).select().first()
    if row.premium=='1':
        redirect(URL('default','myProfilePremium'))
    myInfo=auth.user
    return locals()


#profile view of a premium user who has filled additional info
@auth.requires_login()
def myProfilePremium():
    myInfo=auth.user
    myIntr=db(db.Interests.userId==auth.user.id).select().first()
    return locals()


#suggested profile visibilty for a free user
@auth.requires_login()
def freeProfile():
    row=db(db.auth_user.id==request.args[0]).select().first()
    if row.premium=='1':
        redirect(URL('default','premiumProfile',args=request.args))
    userInfo=db(db.auth_user.id==request.args[0]).select()
    return locals()

#suggested profile visibility for a premium user
@auth.requires_login()
def premiumProfile():
    userInfo=db(db.auth_user.id==request.args[0]).select()
    userIntr=db(db.Interests.userId==request.args[0]).select().first()
    myIntr=db(db.Interests.userId==auth.user.id).select().first()
    myInfo=auth.user
    return locals()


def myValidation(form):
    form.vars.userId=auth.user.id



@auth.requires_login()
def goPremium():
    if auth.user.first_name=='admin':
        redirect(URL('default','admin'))
    form=SQLFORM(db.Interests)

    if form.process(onvalidation=myValidation).accepted:
        row = db(db.auth_user.id==auth.user.id).select().first()
        row.update_record(premium='1')
        auth.user.premium=1
        email=auth.user.email
        if mail.send(to=[email],subject='Re: Premium Trail Activated (iConnect)',message='Dear User, Your premium account trail period has been activated. Expires in 1 month.'):
            response.flash = 'email sent'
        else:
            response.flash = 'sent failed'

        
        redirect(URL('homePremium'))
    return locals()




#making dummy payment
@auth.requires_login()
def payment():
    if auth.user.first_name=='admin':
        redirect(URL('default','admin'))
    return locals()


#handling likes
def onLike():
    lId=request.args[0]
    userId=auth.user.id

    rows =db((db.likesTable.userId==userId) & (db.likesTable.lId==lId)).select()
    if len(rows)==0:
        db.likesTable.insert(userId=userId,lId=lId)
        response.flash='U liked this profile'
    else:
        response.flash='U already liked this profiles'
    

    rows1 = db(db.likesTable.lId==lId).select()
    likes=len(rows1)
    return " "+str(likes)


#handling spams
def onSpam():
    sId=request.args[0]
    userId=auth.user.id

    rows =db((db.spamTable.userId==userId) & (db.spamTable.sId==sId)).select()
    if len(rows)==0:
        db.spamTable.insert(userId=userId,sId=sId)
        response.flash='U spamed this profile'
    else:
        response.flash='U already spamed this profiles'
    

    rows1 = db(db.spamTable.sId==sId).select()
    spams=len(rows1)
    return " "+str(spams)


#wishlist 
@auth.requires_login()
def wishList():
    if auth.user.first_name=='admin':
        redirect(URL('default','admin'))
    if auth.user.premium=='0':
        session.flash="You are a Free User. Upgrade to Premium"
        redirect(URL('default','payment'))

    rows=db(db.WishlistTable.userId==auth.user.id).select()
    myList=[]
    for row in rows:
        myList.append(row.wId)
    myInfo=auth.user

    return locals()

#full list
@auth.requires_login()
def fullList():
    if auth.user.first_name=='admin':
        redirect(URL('default','admin'))
    if auth.user.premium=='0':
        session.flash="You are a Free User. Upgrade to Premium"
        redirect(URL('default','payment'))

    users=db(db.auth_user.gender!=auth.user.gender).select()
    userList=[]
    likeCount=[]
    for i in users:
        userList.append(i.id)
        likes=db(db.likesTable.lId==i.id).select()
        likeCount.append(len(likes))

    i=0
    while i<len(userList):
        j=0
        while j<len(userList)-1:
            if likeCount[j]<likeCount[j+1]:
                temp=likeCount[j]
                likeCount[j]=likeCount[j+1]
                likeCount[j+1]=temp

                temp=userList[j]
                userList[j]=userList[j+1]
                userList[j+1]=temp
            j=j+1
        i=i+1


    return locals()


#add users to wishList
def addToWishlist():
    wId=request.args[0]
    userId=auth.user.id

    rows =db((db.WishlistTable.userId==userId) & (db.WishlistTable.wId==wId)).select()
    if len(rows)==0:
        db.WishlistTable.insert(userId=userId,wId=wId)
        response.flash='Added to Wishlist'
    else:
        response.flash="Already in yourt Wishlist"



#admin begin ********

def admin():
    user_table = None
    interests_table = None
    spams_table = None
    if request.args(0) == "auth_user":
        user_table = SQLFORM.smartgrid(db.auth_user)
    elif request.args(0) == "interests" or request.args(0) == "Interests":
        interests_table = SQLFORM.smartgrid(db.Interests)
    elif request.args(0) == "spams" or request.args(0) == "Spams":
        spams_table = SQLFORM.smartgrid(db.spamTable)

    return locals()


#admin end ****



#send maild
def sendMail():
    row = db(db.auth_user.id==request.args[0]).select().first()
    fname=row.first_name
    lname=row.last_name
    mailId=row.email
    form=SQLFORM.factory(Field('Subject','string',requires=IS_NOT_EMPTY()),Field('Body','text',requires=IS_NOT_EMPTY()))
    
    if form.accepts(request,session):
        subject=form.vars.Subject
        body=form.vars.Body
        email=row.email
        if mail.send(to=[email],subject=subject,message=body):
            response.flash = 'email sent'
        else:
            response.flash = 'sent failed'
        redirect(URL('default','premiumProfile',args=[request.args[0]]))

    return locals()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


