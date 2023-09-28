from datetime import date
import datetime
 from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import simplejson as json
from django.core.files.storage import FileSystemStorage
con=MySQLdb.connect("localhost","root","","cliq")
c=con.cursor()
# Create your views here.
def home(request):
    return render(request,'index.html')
def cusregdisp(request):
    return render(request,'customerregistration.html')
def adminpage(request):
    return render(request,'adminhome.html')
def customerhome(request):
    return render(request,'customerhome.html')
def contact(request):
    return render(request,'contact.html')
def contact(request):
    return render(request,'contact.html')
def photographerhome(request):
    return render(request,'photographerhome.html')
def associationhome(request):
    return render(request,'associationhome.html')
def cusreg(request):
    msg=""
    if(request.POST):
        na=request.POST.get("name")
        addr=request.POST.get("addr")
        gen=request.POST.get("rad")
        dis=request.POST.get("dis")
        email=request.POST.get("email")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        password=request.POST.get("pass")
        
        tr="insert into cusreg(name,addr,gender,district,email,phno,uname,password) values('"+str(na)+"','"+str(addr)+"','"+str(gen)+"','"+str(dis)+"','"+str(email)+"','"+str(phno)+"','"+str(uname)+"','"+str(password)+"')"
        c.execute(tr)
        print(tr)
        type="customer"
        st="approved"
        tv="insert into login(username,password,type,status) values('"+str(uname)+"','"+str(password)+"','"+str(type)+"','"+str(st)+"')"
        c.execute(tv)
        con.commit()
        msg="Registered Successfull"
       
    return render(request,'customerregistration.html',{'msg':msg})

def photoreg(request):
    msg=""
    p="select * from district"
    c.execute(p)
    data=c.fetchall()
    if(request.POST):
        na=request.POST.get("name")
        addr=request.POST.get("addr")
        gen=request.POST.get("rad")
        dis=request.POST.get("dis")
        email=request.POST.get("email")
        pl=request.POST.get("pl")
        sp=request.POST.get("sp")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        password=request.POST.get("pass")
        asoc="not member"
        uploaded_file_url=""
        #if request.FILES.get("f1"):
            
        myfile=request.FILES.get("f1")
        print(myfile)
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)
        st="not approved"
        c.execute("select did from district where district='"+str(dis)+"'")
        da=c.fetchone()
        did=da[0]
        tr="insert into photographerreg(name,addr,gender,district,place,specialization,email,phno,image,uname,password,status,association1,association2) values('"+str(na)+"','"+str(addr)+"','"+str(gen)+"','"+str(dis)+"','"+str(pl)+"','"+str(sp)+"','"+str(email)+"','"+str(phno)+"','"+str(uploaded_file_url)+"','"+str(uname)+"','"+str(password)+"','"+str(st)+"','"+str(asoc)+"','"+str(asoc)+"')"
        c.execute(tr)
        ty="insert into place(did,location) values('"+str(did)+"','"+str(pl)+"')"
        c.execute(ty)
        print(ty)
        type="photographer"
        st="not approved"
        tv="insert into login(username,password,type,status) values('"+str(uname)+"','"+str(password)+"','"+str(type)+"','"+str(st)+"')"
        c.execute(tv)
        con.commit()
        msg="Successfully Registered"
       
    return render(request,'photographerreg.html',{'data':data,'msg':msg})

def associationreg(request):
    msg=""
    if(request.POST):
        na=request.POST.get("name")
        addr=request.POST.get("addr")
        gen=request.POST.get("ah")
        
        email=request.POST.get("email")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        password=request.POST.get("pass")
        st="not approved"        
        tr="insert into associationreg(name,addr,assochead,email,phno,username,status) values('"+str(na)+"','"+str(addr)+"','"+str(gen)+"','"+str(email)+"','"+str(phno)+"','"+str(uname)+"','"+str(st)+"')"
        c.execute(tr)
        print(tr)
        type="association"
        st="not approved"
        tv="insert into login(username,password,type,status) values('"+str(uname)+"','"+str(password)+"','"+str(type)+"','"+str(st)+"')"
        c.execute(tv)
        msg="Successfully Registered"
        con.commit()
        
       
    return render(request,'associationreg.html',{'msg':msg})


def login(request):
    if(request.POST):
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")       
        st="approved"
        v="select type from login where username='"+str(uname)+"' and password='"+str(pswd)+"' and status='"+str(st)+"'"
        c.execute(v)
        da=c.fetchone()
        print(v)
        
        request.session["un"]=uname
        if not bool(da):
            msg="invalid username or password"
            return render(request,'login.html',{'msg':msg})

        if da[0]=="admin":
                #  msg="Login As Admin"
                 return HttpResponseRedirect("/adminhome/")
        if da[0]=="photographer":

                nb="select name,pid from photographerreg where uname='"+str(uname)+"'"
                c.execute(nb)
                cc=c.fetchall()
                request.session["name"]=cc[0][0]
                request.session["pid"]=cc[0][1]    
                return HttpResponseRedirect("/photographerhome/")
        if da[0]=="customer":
                c.execute("select name,cid from cusreg where uname='"+str(uname)+"'")
                cc=c.fetchall()
                print(cc)
                
                request.session["name"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                return HttpResponseRedirect("/customerhome")
        if da[0]=="association":
                c.execute("select name,associd from associationreg where username='"+str(uname)+"'")
                cc=c.fetchall()
                request.session["assoname"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                return HttpResponseRedirect("/associationhome")
        con.commit()  
    return render(request,'login.html')

def adminapprovepg(request):
    id=request.GET.get("id")
    em=request.GET.get('un')
    
    st="approved"
    t="update photographerreg set  status='"+str(st)+"' where pid='"+str(id)+"'"
    c.execute(t)
    print(t)
    tr="select uname from photographerreg where pid='"+str(id)+"'"
    c.execute(tr)
    v=c.fetchone()
    un=v[0]
    p="update login set  status='"+str(st)+"' where username='"+str(un)+"'"
    c.execute(p)
    con.commit()
    print(p)
    sta="approved"
    p="select * from photographerreg where status='"+str(sta)+"'"
    print("qry",p)
    c.execute(p)
    data=c.fetchall()
    return render(request,'adminviewphotographers.html',{'data':data})

def adminapproveassoc(request):
        id=request.GET.get("id")
        
        st="approved"
        t="update associationreg set  status='"+str(st)+"' where associd='"+str(id)+"'"
        c.execute(t)
        print(t)
        tr="select username from associationreg where associd='"+str(id)+"'"
        c.execute(tr)
        v=c.fetchone()
        un=v[0]
        p="update login set  status='"+str(st)+"' where username='"+str(un)+"'"
        c.execute(p)
        con.commit()
        print(p)
        sta="not approved"
        p="select * from associationreg where status='"+str(sta)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewassociation.html',{'data':data})
def adminrejectpg(request):
        id=request.GET.get("id")
     
       
       
        t="delete from photographerreg where pid='"+str(id)+"'"
        c.execute(t)
       
        tr="select uname from photographerreg where pid='"+str(id)+"'"
        c.execute(tr)
        v=c.fetchone()
        un=v[0]
        p="delete from login  where username='"+str(em)+"'"
        c.execute(p)
        con.commit()
        print(p)
        sta="not approved"
        p="select * from photographerreg where status='"+str(sta)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewphotographers.html',{'data':data})

def adminrejectassoc(request):
        
        id=request.GET.get("id")
        
       
        t="delete from associationreg where associd='"+str(id)+"'"
        c.execute(t)
       
        tr="select uname from associationreg where associd='"+str(id)+"'"
        c.execute(tr)
        v=c.fetchone()
        un=v[0]
        p="delete from login  where username='"+str(un)+"'"
        c.execute(p)
        con.commit()
        print(p)
        sta="not approved"
        p="select * from associationreg where status='"+str(sta)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewassociation.html',{'data':data})
def viewphotographers(request):
        st="not approved"
        p="select * from photographerreg where status='"+str(st)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewphotographers.html',{'data':data})
def viewassociation(request):
        st="not approved"
        p="select * from associationreg where status='"+str(st)+"'"
        c.execute(p)
        data=c.fetchall()
        print(data)
        return render(request,'adminviewassociation.html',{'data':data})
def adminviewusers(request):
        
        p="select * from cusreg"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewusers.html',{'data':data})
def adminviewallpg(request):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        sta="approved"
        p="select * from photographerreg where status='"+str(sta)+"'"
        print(p)
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewallphotographers.html',{'data':data})
def addfeedback(request):  
    d=request.GET.get('id')
    request.session["phidfeedback"]=d 
    if(request.POST):
        cid=request.session["cid"]
        phid=request.session["phidfeedback"]
        na=request.POST.get("feed")
        rate=request.POST.get("rating")
        da=date.today()
        fg="select count(*) from feedback where cid='"+str(cid)+"' and phid='"+str(phid)+"'"
        c.execute(fg)
        data23=c.fetchone()
        cou=data23[0]
        print(fg,cou)
        if cou==0:
            tr="insert into feedback(cid,feedbackmsg,date,rating,phid) values('"+str(cid)+"','"+str(na)+"','"+str(da)+"','"+str(rate)+"','"+str(phid)+"')"
            c.execute(tr)
            print(tr)
            con.commit()
        else:
            msg="Already Added"
            return render(request,"customeraddrating.html",{'msg':msg})

       
    return render(request,"customeraddrating.html")
def photographeraddcomplaint(request):   
    if(request.POST):
        pid=request.session["pid"]
        pname=request.session["name"]
        na=request.POST.get("name")
        da=date.today()
        ty="photographer"
        tr="insert into complaint(cid,cname,complaintdes,date,type) values('"+str(pid)+"','"+str(pname)+"','"+str(na)+"','"+str(da)+"','"+str(ty)+"')"
        c.execute(tr)
        print(tr)
        con.commit()
       
    return render(request,'photographeraddfeedback.html')
def customeraddcomplaint(request):   
    if(request.POST):
        cid=request.session["cid"]
        pname=request.session["name"]
        na=request.POST.get("name")
        da=date.today()
        ty="customer"
        tr="insert into complaint(cid,cname,complaintdes,date,type) values('"+str(cid)+"','"+str(pname)+"','"+str(na)+"','"+str(da)+"','"+str(ty)+"')"
        c.execute(tr)
        print(tr)
        con.commit()
       
    return render(request,'customer_addfeedback.html')

def district(request):

        p="select * from district"
        c.execute(p)
        data=c.fetchall()
        if(request.POST):
                dis=request.POST.get("district")
                na=request.POST.get("name")
                lk="select did from district where district='"+str(dis)+"'"
                c.execute(lk)
                da=c.fetchone()
                did=da[0]
                tr="insert into place(did,location) values('"+str(did)+"','"+str(na)+"')"
                c.execute(tr)
                print(tr)
                con.commit()
       
        return render(request,'adminaddplace.html',{'data':data})
def pgaddpackage(request):

    msg=""
    if(request.POST):
        pa=request.POST.get("pack")
        amt=request.POST.get("amt")
        pid=request.session["pid"]
        
        tr="insert into packages(phid,package,amount) values('"+str(pid)+"','"+str(pa)+"','"+str(amt)+"')"
        c.execute(tr)
        print(tr)
        con.commit()
        msg="Package Added Successfully"
       
    return render(request,'photographeraddpackage.html',{"msg":msg})
def viewpackage(request):
        pid=request.session["pid"]
        
        p="select * from packages where phid='"+str(pid)+"'"
        c.execute(p)
        print(p)
        data=c.fetchall()
        return render(request,'photographerviewpackage.html',{'data':data})
def customerviewpackage(request):
        pid=request.GET.get("reg_id")
        
        p="select * from packages where phid='"+str(pid)+"'"
        c.execute(p)
        data=c.fetchall()
        return render(request,'customerviewpackages.html',{'data':data})
def morebooking(request):
        msg=""
        pd=request.GET.get("reg_id")
        da=datetime.date.today().year
        
        if(request.POST):
            pkgid=request.POST.get("id")
            fdate=request.POST.get("fd")
            tdate=request.POST.get("td")
            days=request.POST.get("nd")
            loc=request.POST.get("n1")
            de=request.POST.get("n2")
            td=tdate
            print(td[0:4])
            if da!=int(td[0:4]):
                msg="cannot choose that year"
                return render(request,'customerbook.html',{'msg':msg})       
            else:
                bv="select phid,amount from packages where pkgid='"+str(pkgid)+"'"
                c.execute(bv)
                print(bv)
                data1=c.fetchall()
                phid=data1[0][0]
                amt=data1[0][1]
                r="select name from photographerreg where pid='"+str(phid)+"'"
                c.execute(r)
                da=c.fetchone()
                phname=da[0]
                cdate=date.today()
                sta="processing"
                sta1="approved"
                r="select count(fromdate) from booking where phid='"+str(phid)+"' and status='"+str(sta)+"' or status='"+str(sta1)+"'"
                c.execute(r)
                da=c.fetchone()
                bokdate=da[0]
                cid=request.session["cid"]
                print(cid)
                if bokdate>0:
                    r="select fromdate from booking where phid='"+str(phid)+"' and status='"+str(sta)+"' or status='"+str(sta1)+"'"
                    c.execute(r)
                    da=c.fetchone()
                    bokdate=da[0]
                # cna=request.session["name"]
                    cid=request.session["name"]
                    print(cid,"photogrpaheriddddddddd")
                    if bokdate==fdate:
                        print("entered")
                        m="select * from district"
                        c.execute(m)
                        data=c.fetchall()
                        count=0
                        msg="Already Booked in this date"
                        if 'searchsub' in request.POST:

                            dis=str.lower(request.POST.get("district"))
                            pl=request.POST.get("n1")
                            
                        # fd=request.POST.get("fdate")
                        # td=request.POST.get("tdate")
                            mn="select count(*) from photographerreg where district='"+str(dis)+"' and place='"+str(pl)+"'"
                            c.execute(mn)
                            
                            d1=c.fetchone()
                            if d1[0]>0:
                                count=1
                                mn="select * from photographerreg where district='"+str(dis)+"' and place='"+str(pl)+"'"
                                c.execute(mn)
                                print(mn)
                                ds=c.fetchall()
                                print(ds)
                                #phid=ds[0]
                                #mk="select * from packages where phid='"+str(phid)+"'"
                                #c.execute(mk)
                                #data1=c.fetchall()
                                return render(request,'customer view photographer.html',{'data1':ds,'count':count}) 
                            else:
                                msg="No Photographers Available"
                                return render(request,'customer view photographer.html',{'data':data,'msg':msg})
                        return render(request,'customer view photographer.html',{'data':data,'msg':msg})

                else:
                    st="not approved"
                    lk="insert into booking(phid,pkgid,bookingdate,fromdate,todate,days,location,description,cid,tamount,status) values('"+str(phid)+"','"+str(pkgid)+"','"+str(cdate)+"','"+str(fdate)+"','"+str(tdate)+"','"+str(days)+"','"+str(loc)+"','"+str(de)+"','"+str(cid)+"','"+str(amt)+"','"+str(st)+"')"
                    c.execute(lk)
                    print(lk)
                    con.commit()
                    msg="Request Send"
                    return HttpResponseRedirect("/customerhome/",{"msg":msg}) 
            
        return render(request,'customerbook.html',{'data':pd})       
def viewfeedback(request):
       
        p="select feedback.*,photographerreg.name,photographerreg.phno from feedback inner join photographerreg on photographerreg.pid=feedback.phid"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminViewfeedback.html',{'data':data})
def adminviewcomplaint(request):
       
        p="select * from complaint"
        c.execute(p)
        data=c.fetchall()
        return render(request,'adminviewcomplaints.html',{'data':data})
def editpackage(request):

        id=request.GET.get("id")
        tr="select * from packages where pkgid='"+str(id)+"'"
        c.execute(tr)
        data=c.fetchall()
        if(request.POST):

            pkgid=request.POST.get("packid")
            pkgna=request.POST.get("pack")
            pkgamt=request.POST.get("amt")
            p="update packages set  package='"+str(pkgna)+"',amount='"+str(pkgamt)+"' where pkgid='"+str(pkgid)+"'"
            data=c.execute(p)
            print(data)
            con.commit()
            return HttpResponseRedirect("/viewpackage/")
        return render(request,'photographer edit package.html',{'data':data})

def updatepackage(request):
     if(request.POST):

        pkgid=request.POST.get("packid")
        pkgna=request.POST.get("pack")
        pkgamt=request.POST.get("amt")
        p="update packages set  package='"+str(pkgna)+"',amount='"+str(pkgamt)+"' where pkgid='"+str(pkgid)+"'"
        c.execute(p)
        con.commit()
        print(p)
        return HttpResponseRedirect("/viewpackage/")
def removepackage(request):
        id=request.GET.get("id")
        
       
        t="delete from packages where pkgid='"+str(id)+"'"
        c.execute(t)
       
        con.commit()
        pid=1
        p="select * from packages where phid='"+str(pid)+"'"
        c.execute(p)
        data=c.fetchall()
        
        return render(request,'photographerviewpackage.html',{'data':data})
def placelist(request):

    pan_list=[]
    did=request.GET.get("d_id")
    
    c.execute("select location from place where did ='"+ str(did)+"'")
    
    data2=c.fetchall()
    print(data2)
    
    return HttpResponse(json.dumps(data2),content_type="application/json")
def customerviewphotographers(request):
    m="select * from district"
    c.execute(m)
    data=c.fetchall()
    count=0
    msg=""
    if(request.POST):

        dis=request.POST.get("district")
        pl=request.POST.get("place")
        
       # fd=request.POST.get("fdate")
       # td=request.POST.get("tdate")
        mn="select count(*) from photographerreg where district='"+str(dis)+"' and place='"+str(pl)+"'"
        c.execute(mn)
        print(mn)
        d1=c.fetchone()
        print(d1)
        bn=d1[0]
        stus='approved'
        if bn>0:
            count=1
            mn="select * from photographerreg where district='"+str(dis)+"' and place='"+str(pl)+"' and status='"+str(stus)+"'"
            c.execute(mn)
            print(mn)
            ds=c.fetchall()
            print(ds)
            #phid=ds[0]
            #mk="select * from packages where phid='"+str(phid)+"'"
            #c.execute(mk)
            #data1=c.fetchall()
            return render(request,'customer view photographer.html',{'data1':ds,'count':count}) 
        else:
            msg="No Photographers Available"
            return render(request,'customer view photographer.html',{'data':data,'msg':msg}) 
    return render(request,'customer view photographer.html',{'data':data,'count':count,'msg':msg})

def photographerprofile(request):
    
    did=request.GET.get("reg_id")
 
    st="approved"
    b="select *  from photographerreg   where pid ='"+ str(did)+"'"
    c.execute(b)
    print(b)
    data2=c.fetchall()
    b="select *  from packages where phid ='"+ str(did)+"'"
    c.execute(b)
    dat=c.fetchall()
    b="select *  from specification where phid ='"+ str(did)+"'"
    c.execute(b)
    specdata=c.fetchall()
    p="select feedback.feedbackmsg,feedback.rating,cusreg.name from feedback inner join cusreg on feedback.cid=cusreg.cid where feedback.phid='"+ str(did)+"'"
    c.execute(p)
    
    feeddata=c.fetchall()
    print(feeddata)
    h="select *  from photographerimage where phid ='"+ str(did)+"'"
    c.execute(h)
    imgdat=c.fetchall()
    print(imgdat)
    h="select *  from photographervideo where phid ='"+ str(did)+"'"
    c.execute(h)
    videodat=c.fetchall()
    return render(request,'CustomerViewPhotographerProfile.html',{'data':data2,'data1':dat,'specdata':specdata,'feeddata':feeddata,'imgdat':imgdat,'videodat':videodat})

def photographerartgallery(request):
    
    
    did=request.GET.get("reg_id")
    h="select *  from artgallery where phid ='"+ str(did)+"'"
    c.execute(h)
    imgdat=c.fetchall()
    print(imgdat)
    h="select *  from giftgallery where phid ='"+ str(did)+"'"
    c.execute(h)
    videodat=c.fetchall()
    return render(request,'customerviewphotographerartsgallery.html',{'imgdat':imgdat,'videodat':videodat})




def photographerlist(request):

    
    did=request.GET.get("d_id")
 
    
    c.execute("select name from photographerreg where place ='"+ str(did)+"'")
    
    data2=c.fetchall()
    print(data2)
    
    return HttpResponse(json.dumps(data2),content_type="application/json")

def bookpg(request):
    
    pkgid=request.GET.get("id")
    if(request.POST):
        pkgid=request.POST.get("id")
        fdate=request.POST.get("fd")
        tdate=request.POST.get("td")
        days=request.POST.get("nd")
        bv="select phid,amount from packages where pkgid='"+str(pkgid)+"'"
        c.execute(bv)
        print(bv)
        data1=c.fetchall()
        phid=data1[0][0]
        amt=data1[0][1]
        r="select name from photographerreg where pid='"+str(phid)+"'"
        c.execute(r)
        da=c.fetchone()
        phname=da[0]
        cdate=date.today()
        
        # cna=request.session["name"]
        cid=request.session["cid"]
        st="not approved"
        lk="insert into booking(phid,pkgid,bookingdate,fromdate,todate,days,cid,tamount,status) values('"+str(phid)+"','"+str(pkgid)+"','"+str(cdate)+"','"+str(fdate)+"','"+str(tdate)+"','"+str(days)+"','"+str(cid)+"','"+str(amt)+"','"+str(st)+"')"
        c.execute(lk)
        print(lk)
        con.commit()
        return HttpResponseRedirect("/customerhome/")
    return render(request,'customerbook.html',{'data':pkgid})
    
def phimage(request):
    msg=""
    if(request.POST):
        print("hhhi")
        cap=request.POST.get("cap")
        phid=request.session["pid"]
        uploaded_file_url=""
        if request.FILES.get("f1"):
            
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)

            t="insert into photographerimage(caption,image,phid) values('"+str(cap)+"','"+str(uploaded_file_url)+"','"+str(phid)+"')"
            c.execute(t)
            print(t)
            con.commit()
            msg="Aork Added"
    return render(request,"photographerAddImage.html",{"msg":msg})
def phartimage(request):
    msg=""
    if(request.POST):
        
        cap=request.POST.get("cap")
        amt=request.POST.get("f2")
        phid=request.session["pid"]
        uploaded_file_url=""
        if request.FILES.get("f1"):
            
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)

            t="insert into artgallery(caption,image,amount,phid) values('"+str(cap)+"','"+str(uploaded_file_url)+"','"+str(amt)+"','"+str(phid)+"')"
            c.execute(t)
            print(t)
            con.commit()
            msg="Added Successfully"
    return render(request,"photographeraddartgallery.html",{"msg":msg})
def phgiftimage(request):
    msg=""
    if(request.POST):
        
        cap=request.POST.get("cap")
        amt=request.POST.get("f2")
        phid=request.session["pid"]
        uploaded_file_url=""
        if request.FILES.get("f1"):
            
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)

            t="insert into giftgallery(caption,image,amount,phid) values('"+str(cap)+"','"+str(uploaded_file_url)+"','"+str(amt)+"','"+str(phid)+"')"
            c.execute(t)
            print(t)
            con.commit()
            msg="Work Added"
    return render(request,"photographeraddgiftgallery.html",{"msg":msg})


def phspec(request):
    msg=""
    if(request.POST):
        
        cap=request.POST.get("cam")
        mod=request.POST.get("mo")
        des=request.POST.get("des")
        phid=request.session["pid"]
        uploaded_file_url=""
        if request.FILES.get("f1"):
            
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)

            t="insert into specification(camera,cmodel,description,image,phid) values('"+str(cap)+"','"+str(mod)+"','"+str(des)+"','"+str(uploaded_file_url)+"','"+str(phid)+"')"
            c.execute(t)
            print(t)
            con.commit()
            msg="Work Added"
    return render(request,"photographeraddspecification.html",{"msg":msg})
def phvideo(request):
    msg=""
    if(request.POST):
       
        link=request.POST.get("link")
        phid=request.session["pid"]
        uploaded_file_url=""
        if request.FILES.get("f1"):
            
            myfile=request.FILES.get("f1")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)

            t="insert into photographervideo(phid,image,link) values('"+str(phid)+"','"+str(uploaded_file_url)+"','"+str(link)+"')"
            c.execute(t)
            print(t)
            con.commit()
            msg="Work Added"
    return render(request,"photographerAddVideo.html",{"msg":msg})
def viewalbum(request):
    p="select * from district"
    c.execute(p)
    data=c.fetchall()
    if 'search' in request.POST:
        pl=request.POST.get("place")
        pg=request.POST.get("pg")
        bn="select pid from photographerreg where name='"+str(pg)+"' and place='"+str(pl)+"'"
        c.execute(bn)
        da=c.fetchone()
        id=da[0]
        lk="select * from photographerimage where phid='"+str(id)+"'"
        c.execute(lk)
        dat=c.fetchall()
        return render(request,"CustomerViewAlbum.html",{'data':dat})
    return render(request,"customer view albumimage.html",{'data':data})
def viewvideo(request):
    p="select * from district"
    c.execute(p)
    data=c.fetchall()
    if 'search' in request.POST:
        pl=request.POST.get("place")
        pg=request.POST.get("pg")
        bn="select pid from photographerreg where name='"+str(pg)+"' and place='"+str(pl)+"'"
        c.execute(bn)
        da=c.fetchone()
        id=da[0]
        lk="select * from photographervideo where phid='"+str(id)+"'"
        c.execute(lk)
        print(lk)
        data1=c.fetchall()
        return render(request,"CustomerViewVideo.html",{'data1':data1})
    return render(request,"CustomerViewAlbumVideo.html",{'data':data})   
def viewvideolink(request):
    id=request.GET.get("https://www.youtube.com/embed/id")
    return render(request,"video.html",{'id':id})
def photographerviewbookings(request):
    phid=request.session["pid"] 
    st="not approved"
    bg="select cusreg.name,cusreg.phno,booking.* from booking inner join cusreg  ON cusreg.cid=booking.cid where phid='"+str(phid)+"' and status='"+str(st)+"'"
    c.execute(bg)
    print(bg)
    data=c.fetchall()
    return render(request,"PhotographerViewBookings.html",{'data':data})

def photographerupdatebookings(request):
    phid=request.session["pid"] 
    st="not approved"
    sta="paid"
    bg="select cusreg.name,cusreg.phno,booking.* from booking inner join cusreg  ON cusreg.cid=booking.cid where phid='"+str(phid)+"' and status!='"+str(st)+"'"
    c.execute(bg)
    print(bg)
    data=c.fetchall()
    return render(request,"photographerupdatebookingstatus.html",{'data':data})
def approvebooking(request):
    bid=request.GET.get("id")
    st="approved"
    kl="update booking set status='"+str(st)+"' where bid='"+str(bid)+"'"
    c.execute(kl)
    con.commit()
    return HttpResponseRedirect("/photographerviewbookings/")
def bookingprocessing(request):
    bid=request.GET.get("id")
    st="processing"
    kl="update booking set status='"+str(st)+"' where bid='"+str(bid)+"'"
    c.execute(kl)
    con.commit()
    return HttpResponseRedirect("/photographerupdatebookings/")
def bookingcompleted(request):
    bid=request.GET.get("id")
    st="completed"
    kl="update booking set status='"+str(st)+"' where bid='"+str(bid)+"'"
    c.execute(kl)
    con.commit()
    return HttpResponseRedirect("/photographerupdatebookings/")
def rejectbooking(request):
    bid=request.GET.get("id")
    st="rejected"
    kl="update booking set status='"+str(st)+"' where bid='"+str(bid)+"'"
    c.execute(kl)
    con.commit()
    return HttpResponseRedirect("/photographerviewbookings/")

def viewnotification(request):
    cusid=request.session["cid"]
    st="approved"
    bg="select booking.fromdate,booking.todate,(booking.days*booking.tamount) as totalamt,photographerreg.name,photographerreg.phno,photographerreg.email,booking.bid,booking.status,photographerreg.pid from booking inner join photographerreg ON booking.phid=photographerreg.pid where booking.cid='"+str(cusid)+"'"
    c.execute(bg)
    print(bg)
    
    data=c.fetchall()

   
    return render(request,"CustomerViewNotification.html",{'data':data})
def viewrejectedbookings(request):
    cusid=request.session["cid"]
    st="rejected"
    bg="select booking.fromdate,booking.todate,(booking.days*booking.tamount) as totalamt,photographerreg.name,photographerreg.phno,photographerreg.email,booking.bid,booking.status from booking inner join photographerreg ON booking.phid=photographerreg.pid where booking.cid='"+str(cusid)+"'"
    c.execute(bg)
    print(bg)
    
    data=c.fetchall()

   
    return render(request,"CustomerViewRejectedNotification.html",{'data':data})
def payment1(request):
    cid=request.session["cid"]
    bid=request.GET.get('id')
    
    
    if request.POST:
        cno=request.POST.get("cardno")
        request.session["card_no"]=cno
        kl="select phid,(days*tamount) as totalamt from booking where bid='"+str(bid)+"'"
        c.execute(kl)
        print(kl)
        da=c.fetchall()
        pid=da[0][0]
        amt=da[0][1]
        print(amt)
        request.session["amt"]=amt
        b="insert into payment(custid,phid,amount) values('"+str(cid)+"','"+str(pid)+"','"+str(amt)+"')"
        c.execute(b)
        h="paid"
        by="update booking set status='"+str(h)+"' where bid='"+str(bid)+"'"
        c.execute(by)
        con.commit()
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    cno=request.session["card_no"]
   # amount=request.session["pay"]
    amount=request.session["amt"]
    if request.POST:
       
      #  n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
       
       # c.execute(n)
      #  con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
  #  cno=request.session["card_no"]
    today = date.today()
   # n="select * from delivery where card='"+str(cno)+"'"
    #c.execute(n)
    #data=c.fetchall()
    if 'gohome' in request.POST:
    
        return HttpResponseRedirect("/customerhome/")
    return render(request,"payment5.html",{"today":today})

def goback(request):
    if 'go' in request.POST:

        return HttpResponseRedirect("/customerhome")
def pgviewpayment(request):
    phid=request.session["pid"] 
    
    bg="select cusreg.name,cusreg.phno,payment.* from payment inner join cusreg  ON cusreg.cid=payment.custid where phid='"+str(phid)+"'"
    c.execute(bg)
    print(bg)
    data=c.fetchall()
    return render(request,"photographerviewpayment.html",{'data':data})

def award(request):
    
    
    if(request.POST):
        na=request.POST.get("name")
        pn=request.POST.get("pname")
        de=request.POST.get("des")
        #pid=request.session["pid"]

        pid=1
        d=date.today()
        assoc=request.session["assoname"]
        tr="insert into award(assocname,award,pname,descrip,date) values('"+str(assoc)+"','"+str(na)+"','"+str(pn)+"','"+str(de)+"','"+str(d)+"')"
        c.execute(tr)
        print(tr)
        con.commit()
       
    return render(request,'associationaddaward.html')

def noti(request):
    
    
    if(request.POST):
        na=request.POST.get("name")
        pn=request.POST.get("pname")
        de=request.POST.get("des")
        loc=request.POST.get("loc")
        #pid=request.session["pid"]
        
        assoc=request.session["assoname"]
        tr="insert into notification(assocname,event,date,descrip,loc) values('"+str(assoc)+"','"+str(na)+"','"+str(pn)+"','"+str(de)+"','"+str(loc)+"')"
        c.execute(tr)
        print(tr)
        con.commit()
       
    return render(request,'associationaddnotification.html')

def addassoc(request):
    st="approved"
    aso="not member"
    p="select * from photographerreg where status='"+str(st)+"' and association1='"+str(aso)+"' or association2='"+str(aso)+"'"
    c.execute(p)
    print(p)
    data=c.fetchall()
    return render(request,'associationviewphotographers.html',{'data':data})

def assocmember(request):
    st="approved"
    aso=request.session["assoname"]
    p="select * from photographerreg where status='"+str(st)+"' and association1='"+str(aso)+"' or association2='"+str(aso)+"'"
    c.execute(p)
    print(p)
    data=c.fetchall()
    return render(request,'associationviewmembers.html',{'data':data})

def photographeraddtoassoc(request):
    bid=request.GET.get('id')
    print("haii")
    asoname=request.session["assoname"]
    aso="not member"
    p="select association1,association2 from photographerreg where pid='"+str(bid)+"' "
    c.execute(p)
    print(p)
    print(asoname)
    data=c.fetchall()
    aso1=data[0][0]
    aso2=data[0][1]
    #assna=request.session["assoname"]
    if aso1!=asoname and aso2!=asoname:
        if aso1=='not member':
            aname=request.session["assoname"]
            by="update photographerreg set association1='"+str(aname)+"' where pid='"+str(bid)+"'"
            c.execute(by)
            print(by)
            con.commit()
        elif aso2=='not member':
            aname=request.session["assoname"]
            by="update photographerreg set association2='"+str(aname)+"' where pid='"+str(bid)+"'"
            c.execute(by)
            con.commit()
    else:
        msg="already member"
        print("kuuiiiiiiiiiiiiiiiii")
        return render(request,'associationviewphotographers.html',{'msg':msg})

   
    return HttpResponseRedirect("/addassoc")

def Map(request):
    return render(request,'Map.html')

def customerviewaward(request):
    st=request.session["pid"]
    #aso=request.session["assoname"]
    pn="select association1,association2 from photographerreg where pid='"+str(st)+"'"
    c.execute(pn)
    
    data12=c.fetchall()
    assoc1=data12[0][0]
    assoc2=data12[0][1]
    p="select * from award where assocname='"+str(assoc1)+"' or assocname='"+str(assoc2)+"'"
    c.execute(p)
    
    data=c.fetchall()
    print(data)
    return render(request,'photographerviewaward.html',{'data':data})
def photographerviewnotification(request):
    st=request.session["pid"]
    #aso=request.session["assoname"]
    pn="select association1,association2 from photographerreg where pid='"+str(st)+"'"
    c.execute(pn)
    
    data12=c.fetchall()
    assoc1=data12[0][0]
    assoc2=data12[0][1]
    p="select * from notification where assocname='"+str(assoc1)+"' or assocname='"+str(assoc2)+"'"
    c.execute(p)
    
    data=c.fetchall()
    print(data)
    return render(request,'photographerviewnotification.html',{'data':data})
def photographerviewassociation(request):
    st="approved"
    p="select * from associationreg where status='"+str(st)+"'"
    c.execute(p)
    
    data=c.fetchall()
    print(data)
    return render(request,'photographerviewassociation.html',{'data':data})
def requestmembership(request):
    an=request.GET.get('aname')
    pid=request.session["pid"]
    st="approved"
    p="select association1,association2 from photographerreg where pid='"+str(pid)+"'"
    c.execute(p)
    
    data1=c.fetchall()
    aso=data1[0][0]
    aso1=data1[0][1]
    if aso==an or aso1==an:
        msg="already member"
        st="approved"
        p="select * from associationreg where status='"+str(st)+"'"
        c.execute(p)
        
        data=c.fetchall()
    
        return render(request,'photographerviewassociation.html',{'data':data,'msg':msg})
    elif aso=='not member':
        gb="update photographerreg set association1='"+str(an)+"' where pid='"+str(pid)+"'"
        return HttpResponseRedirect("/photographerviewassociation")
    elif aso1=='not member':
        gb="update photographerreg set association2='"+str(an)+"' where pid='"+str(pid)+"'"
        return HttpResponseRedirect("/photographerviewassociation")
    return render(request,'photographerviewassociation.html',{'data':data})

def rate_now(request):
    
    return render(request,"customeraddrating.html")

def placelist1(request):
    
    pan_list=[]
    did=request.GET.get("d_id")
    fg="select did from district where district='"+str(did)+"'"
    c.execute(fg)
    dd=c.fetchone()
    did=dd[0]
    c.execute("select distinct(location) from place where did ='"+ str(did)+"'")
    
    data1=c.fetchall()
    print(data1)
    
    return HttpResponse(json.dumps(data1),content_type="application/json")