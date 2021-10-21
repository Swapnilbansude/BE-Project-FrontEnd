from django.shortcuts import render,redirect
import datetime
import random
import io
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.contrib import messages
#from requests.auth import HTTPBasicAuth
import json
import requests
import pickle
from utils.fertilizer import fertilizer_dic
from utils.crop import crop_dict

from utils.disease import disease_dic
from utils.model import ResNet9 
from io import BytesIO


#import torch
import torch
from torchvision import transforms
from PIL import Image

#from torchvision import transforms
from PIL import Image

# Create your views here.
AUTH_TOKEN = None
USER_ID = None

#Loading Disease prediction data
disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry_(including_sour)___Powdery_mildew',
                   'Cherry_(including_sour)___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___Leaf_scorch',
                   'Strawberry___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

disease_model_path = 'model/plant_disease_model.pth'
disease_model = ResNet9(3, len(disease_classes))
disease_model.load_state_dict(torch.load(
    disease_model_path, map_location=torch.device('cpu')))
disease_model.eval()


# Loading crop recommendation model

crop_recommendation_model_path = 'model/DecisionTree.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))

def home(request):
    return render(request, 'farmer.html')

def mft(request):
    return render(request, 'mft.html')

def aero(request):
    return render(request, 'aeroponics.html')

def aqua(request):
    return render(request, 'aquaponics.html')

def hydro(request):
    return render(request, 'hydroponics.html')

def mono(request):
    return render(request, 'monoculture.html')

def tissue(request):
    return render(request, 'tissue.html')        

def postcomplaint(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            complaint = request.POST.get('complaint')
            desc = request.POST.get('description')

            data = {
                'name':name,
                'phone':phone,
                'complaint_type':complaint,
                'description':desc
            }

            url = 'http://127.0.0.1:8000/auth/complaints/'
            response = requests.post(url, json=data, headers={'Authorization': AUTH_TOKEN})
            if response.status_code == 201:
                messages.success(request,"Complaint Posted Successfully")
            else:
                messages.error(request,"Error Occured")
        return render(request, 'complaint.html')

def customer(request):
    return render(request, 'customer.html')

def postcropads(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        if request.method == 'POST':
            name = request.POST.get('customer_name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            crop = request.POST.get('crop')
            quantity = request.POST.get('quantity')

            data = {
                "customer_name":name,
                "phone":phone,
                "address":address,
                "crop_req":crop,
                "quantity_req":quantity,
            }
            post_ads_api = 'http://127.0.0.1:8000/auth/adsdetails/'
            response = requests.post(post_ads_api, json=data, headers={'Authorization': AUTH_TOKEN})
            d = response.json()
            if response.status_code == 201:
                messages.success(request,"Advertisement Posted Successfully")
            else:
                messages.error(request,"Error Occured")
        return render(request, 'postads.html')
        #return render(request, 'postads.html')

def myads(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        user_info = 'http://127.0.0.1:8000/auth/users/me/'
        result = requests.get(user_info , headers={'Authorization': AUTH_TOKEN})
        access = result.json()
        phone = access['phone']

        url = f'http://127.0.0.1:8000/auth/customeradspdetails/{phone}'
        json_data={}
        response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        response=response.json()
        return render(request,'myads.html', {'response' : response})
        #return render(request, 'myads.html')

def cmarket(request):
    url = 'http://127.0.0.1:8000/auth/cropdetails/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response = response.json()
    print(response)
    return render(request, 'cmarket.html', {'response' : response})

def addtocart(request, id):
    print(id)
    return render(request, 'changepassword.html')

def home_new(request):
    return render(request, 'home.html')

def mycrop(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        user_info = 'http://127.0.0.1:8000/auth/users/me/'
        result = requests.get(user_info , headers={'Authorization': AUTH_TOKEN})
        access = result.json()
        phone = access['phone']

        url = f'http://127.0.0.1:8000/auth/farmercropdetails/{phone}'
        json_data={}
        response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        response=response.json()
        return render(request,'mycrop.html', {'response' : response})
        #return render(request, 'mycrop.html')

def deletemycrop(request, id):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        delete_url = f'http://127.0.0.1:8000/auth/cropbyid/{id}'
        response = requests.delete(delete_url , headers={'Authorization': AUTH_TOKEN})
        if response.status_code == 204:
            messages.success(request, 'Crop Details Deleted Successfully')
        else:
            messages.error(request, 'Error occured while deleting')
        return redirect('mycrop')

def deletemyads(request, id):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        delete_url = f'http://127.0.0.1:8000/auth/adsbyid/{id}'
        response = requests.delete(delete_url , headers={'Authorization': AUTH_TOKEN})
        if response.status_code == 204:
            messages.success(request, 'Advertisements Details Deleted Successfully')
        else:
            messages.error(request, 'Error occured while deleting')
        return redirect('myads')

def fmarket(request):
    url = 'http://127.0.0.1:8000/auth/adsdetails/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response = response.json()
    #print(response)
    return render(request, 'fmarket.html', {'response' : response})
    #return render(request, 'fmarket.html')

def sendfrequest(request, id):
    f_info_url = 'http://127.0.0.1:8000/auth/users/me/'
    response = requests.get(f_info_url , headers={'Authorization': AUTH_TOKEN})
    access = response.json()
    fname = access['first_name'] + " " + access['last_name']
    fphone = access['phone']
    fadd = access['address']
    #print(fname,fphone,fadd)

    c_info_url = f'http://127.0.0.1:8000/auth/adsbyid/{id}'
    info = requests.get(c_info_url , headers={'Authorization': AUTH_TOKEN})
    data = info.json()
    cname = data['customer_name']
    cphone = data['phone']
    cadd = data['address']
    crop_req = data['crop_req']
    quantity_req = data['quantity_req']
    #print(cname)
    
    result = {
        'fname':fname,
        'fphone':fphone,
        'fadd':fadd,
        'cname':cname,
        'cphone':cphone,
        'cadd':cadd,
        'crop_req':crop_req,
        'quantity_req':quantity_req,
        'status':'Pending'
    }

    send_req_url = 'http://127.0.0.1:8000/auth/frequest/'
    res = requests.post(send_req_url, json=result, headers={'Authorization': AUTH_TOKEN})
    if res.status_code == 201:
        messages.success(request,"Request Send to the customer")
    else:
        messages.error(request,"Error Occured")
    return redirect('fmarket')

def sendcrequest(request, id):
    c_info_url = 'http://127.0.0.1:8000/auth/users/me/'
    response = requests.get(c_info_url , headers={'Authorization': AUTH_TOKEN})
    access = response.json()
    cname = access['first_name'] + " " + access['last_name']
    cphone = access['phone']
    cadd = access['address']
    #print(fname,fphone,fadd)

    f_info_url = f'http://127.0.0.1:8000/auth/cropbyid/{id}'
    info = requests.get(f_info_url , headers={'Authorization': AUTH_TOKEN})
    data = info.json()
    fname = data['farmer_name']
    fphone = data['phone']
    fadd = data['address']
    crop = data['crop_name']
    quantity = data['quantity']
    #print(cname)
    
    result = {
        'cname':cname,
        'cphone':cphone,
        'cadd':cadd,
        'fname':fname,
        'fphone':fphone,
        'fadd':fadd,
        'crop':crop,
        'quantity':quantity,
        'status':'Pending'
    }

    send_req_url = 'http://127.0.0.1:8000/auth/crequest/'
    res = requests.post(send_req_url, json=result, headers={'Authorization': AUTH_TOKEN})
    if res.status_code == 201:
        messages.success(request,"Request Send to the Farmer")
    else:
        messages.error(request,"Error Occured")
    return redirect('cmarket')

def frequest(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        user_info = 'http://127.0.0.1:8000/auth/users/me/'
        response = requests.get(user_info , headers={'Authorization': AUTH_TOKEN})
        access = response.json()
        phone = access['phone']

        url = f'http://127.0.0.1:8000/auth/frequest/{phone}'
        json_data={}
        result = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        result = result.json()
        return render(request,'frequest.html', {'response' : result})
        #return render(request, 'mycrop.html')
        #return render(request, 'frequest.html')

def crequest(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        user_info = 'http://127.0.0.1:8000/auth/users/me/'
        response = requests.get(user_info , headers={'Authorization': AUTH_TOKEN})
        access = response.json()
        phone = access['phone']

        url = f'http://127.0.0.1:8000/auth/crequest/{phone}'
        json_data={}
        result = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        result = result.json()
        return render(request,'crequest.html', {'response' : result})
        #return render(request, 'mycrop.html')
        #return render(request, 'frequest.html')

def fresponse(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        user_info = 'http://127.0.0.1:8000/auth/users/me/'
        response = requests.get(user_info , headers={'Authorization': AUTH_TOKEN})
        access = response.json()
        phone = access['phone']

        url = f'http://127.0.0.1:8000/auth/crequesttofarmer/{phone}'
        #url = f'http://127.0.0.1:8000/auth/frequesttocustomer/7083807084'
        json_data={}
        result = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        result = result.json()
        return render(request,'fresponse.html', {'response' : result})
    #    return render(request, 'fresponse.html')

def cresponse(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        user_info = 'http://127.0.0.1:8000/auth/users/me/'
        response = requests.get(user_info , headers={'Authorization': AUTH_TOKEN})
        access = response.json()
        phone = access['phone']

        url = f'http://127.0.0.1:8000/auth/frequesttocustomer/{phone}'
        #url = f'http://127.0.0.1:8000/auth/frequesttocustomer/7083807084'
        json_data={}
        result = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        result = result.json()
        return render(request,'cresponse.html', {'response' : result})

def cresponseaccept(request, id):
    print(id)
    url = f'http://127.0.0.1:8000/auth/cresponse/accept/{id}'
    result = requests.get(url, headers={'Authorization': AUTH_TOKEN})
    #result = result.json()
    if result.status_code == 200:
        messages.success(request, "Request Accept Successfully")
    else :
        messages.error(request, "Error Occured")
    return redirect('cresponse')

def fresponseaccept(request, id):
    print(id)
    url = f'http://127.0.0.1:8000/auth/fresponse/accept/{id}'
    result = requests.get(url, headers={'Authorization': AUTH_TOKEN})
    #result = result.json()
    if result.status_code == 200:
        messages.success(request, "Request Accept Successfully")
    else :
        messages.error(request, "Error Occured")
    return redirect('fresponse')

def cresponsereject(request, id):
    print(id)
    url = f'http://127.0.0.1:8000/auth/cresponse/reject/{id}'
    result = requests.get(url, headers={'Authorization': AUTH_TOKEN})
    #result = result.json()
    if result.status_code == 200:
        messages.success(request, "Request Rejected Successfully")
    else :
        messages.error(request, "Error Occured")
    return redirect('cresponse')

def fresponsereject(request, id):
    print(id)
    url = f'http://127.0.0.1:8000/auth/fresponse/reject/{id}'
    result = requests.get(url, headers={'Authorization': AUTH_TOKEN})
    #result = result.json()
    if result.status_code == 200:
        messages.success(request, "Request Rejected Successfully")
    else :
        messages.error(request, "Error Occured")
    return redirect('fresponse')

def postcrop(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        if request.method == 'POST':
            name = request.POST.get('farmer_name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            crop = request.POST.get('crop')
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')

            data = {
                "farmer_name":name,
                "phone":phone,
                "address":address,
                "crop_name":crop,
                "quantity":quantity,
                "price":price
            }
            post_crop_api = 'http://127.0.0.1:8000/auth/cropdetails/'
            response = requests.post(post_crop_api, json=data, headers={'Authorization': AUTH_TOKEN})
            d = response.json()
            if response.status_code == 201:
                messages.success(request,"Crop Posted Successfully")
            else:
                messages.error(request,"Error Occured")
        return render(request, 'postcrop.html')

def croppred(request):
    return render(request, 'croppred.html')

def fertilizerpred(request):
    return render(request, 'fertilizerpred.html')

def diseasepred(request):
    return render(request, 'diseasepred.html')
        
def index(request):
    return render(request, 'index.html')

def weather(request):
    return render(request, 'weather.html')

def changepassword(request):
    return render(request, 'changepassword.html')

def profile(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        url = 'http://127.0.0.1:8000/auth/users/'
        response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        response=response.json()
        return render(request, 'profile.html',{'response':response})

def cprofile(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        url = 'http://127.0.0.1:8000/auth/users/'
        response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
        response=response.json()
        return render(request, 'cprofile.html',{'response':response})

def sign_in(request):
    try:
        if request.method == 'POST':
            print("In Login")
            #Retriving username & password form login form template
            phone = request.POST.get('phone')
            password = request.POST.get('pass')
            
            data = {
                'phone': phone,
                'password':  password,
            }

            try:
            # post login details to this api
                url = 'http://127.0.0.1:8000/auth/token/login/'
                result = requests.post(url, json=data)
                if result.status_code == "200":
                    messages.success(request, "User Logged In Successfully in Agrigate Agro")
                    print(result.status_code)
            except requests.RequestException:
                print('wrong login fields')
            #accessing token and putting it into djoser Authorization format
            global AUTH_TOKEN 
            AUTH_TOKEN = 'Token {}'.format(result.json()['auth_token'])
            #This Api provides User Information name , is_admin, is_superuser, email, phone etc
            user_info_api = 'http://127.0.0.1:8000/auth/users/me/'

            #requsting user info form api
            user_info = requests.get(user_info_api, headers={'Authorization': AUTH_TOKEN})

            #storing userinfo response in access in json format
            access = user_info.json()

            if access['category'] == 'Farmer':
                messages.success(request, "User Logged In Successfully in Agrigate Agro")
                return redirect('home')
            elif access['category'] == 'Customer':
                messages.success(request, "User Logged In Successfully in Agrigate Agro")
                return redirect('customer')
    except:
        messages.error(request,"invalid credentials")
        return redirect('index')

def log_out(request):
    if AUTH_TOKEN == None:
        return redirect('index')
    else:
        url = 'http://127.0.0.1:8000/auth/token/logout/'
        response = requests.post(url , headers={'Authorization': AUTH_TOKEN})
        messages.success(request, "Logged out successfully")
        return render(request, 'index.html')

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = "9125290bb7ee0b063cb6aadb11ffc2b1"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


def predict(request):
    if request.method == 'POST':
        print("In Prediction")
        #Retriving prediction data
        N = float(request.POST.get('nitrogen'))
        P = float(request.POST.get('phosphorous'))
        K = float(request.POST.get('potassium'))
        phlevel = float(request.POST.get('phlevel'))
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        rainfall = float(request.POST.get('rainfall'))

        data = np.array([[N, P, K, temperature, humidity, phlevel, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        print(final_prediction)
        response = str(crop_dict[final_prediction])
        return render(request, 'croppred.html',{'response':response})

def fertpred(request):
    if request.method == 'POST':
        print("In Fertilizer Recommendation")

        crop_name = str(request.POST.get('crop'))
        N = int(request.POST.get('nitrogen'))
        P = int(request.POST.get('phosphorous'))
        K = int(request.POST.get('potassium'))

        df = pd.read_csv('data/fertilizer.csv')

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = str(fertilizer_dic[key])
        print(response)
        return render(request, 'fertilizerpred.html',{'response':response})

def dpred(request):
    if request.method == 'POST':     
        file = request.FILES['file']
        img = Image.open(file)
        buf = BytesIO()
        img.save(buf, 'jpeg')
        buf.seek(0)
        image_bytes = buf.read()
        buf.close()
        prediction = predict_image(image_bytes)
        prediction = (str(disease_dic[prediction]))
    return render(request,'diseasepred.html',{'response':prediction})


def register(request):
    if request.method == 'POST':
        print("In register")
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        aadhar = request.POST.get('aadharno')
        address = request.POST.get('address')
        password = request.POST.get('password1')
        re_password = request.POST.get('password2')
        category = request.POST.get('category')

        username = username_generator(fname, lname)

        data = {
            'first_name':fname,
            'last_name':lname,
            'username':username,
            'aadhar_no':aadhar,
            'address':address,
            'email':email,
            'is_admin':'false',
            'category':category,
            'password':password,
            'phone':phone,
            're_password':re_password,
        }

        create_user_api = 'http://127.0.0.1:8000/auth/users/'
        response = requests.post(create_user_api, json=data)
        d = response.json()
        if response.status_code == 201:
            print(response.status_code)
            messages.success(request,"Account Created Successfully..!")
        else:
            messages.error(request,"Error occured in account creation")
            
    return render(request , 'index.html')

def username_generator(first_name, last_name):
    username = first_name[:4].lower() + last_name[0:].lower() + str(random.randint(1,100))
    return username

def predict_image(img, model=disease_model):
    """
    Transforms image to tensor and predicts disease label
    :params: image
    :return: prediction (string)
    """
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor(),
    ])
    image = Image.open(io.BytesIO(img))
    img_t = transform(image)
    img_u = torch.unsqueeze(img_t, 0)

    # Get predictions from model
    yb = model(img_u)
    # Pick index with highest probability
    _, preds = torch.max(yb, dim=1)
    prediction = disease_classes[preds[0].item()]
    # Retrieve the class label
    return prediction
