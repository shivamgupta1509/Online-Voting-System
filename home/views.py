from django.shortcuts import render, HttpResponse
import datetime
from home.models import Contact, ElectionList, PartyName, VoteGivenData
from django.contrib import messages
from home import rabinKarp
import pandas as pd
from django.conf import settings

# Create your views here.

def index(request):
    context={"home":"active"}
    if(request.method == "POST" and 'vote' in request.POST):
        vid = request.POST.get('voter')
        ele_region = request.POST.get('region')
        votegiven = VoteGivenData(election_name=ele_region, voter_ID=vid)
        votegiven.save()
        messages.success(request, 'Your Vote is Successfully record')
    return render(request, 'index.html', context)
    # return HttpResponse("This is a homePage...")

def contact(request):
    context={"contact":"active"}
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('contact')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact = Contact(name=name, phone=phone, email=email, msg=msg, date=datetime.date.today())
        contact.save()
        messages.success(request, 'Your Message has been send!')
    return render(request, 'contact.html', context)

def about(request):
    context={"about":"active"}
    return render(request, 'about.html', context)

def voteSelection(request):
    data = ElectionList.objects.all();
    today_date = datetime.date.today();
    context ={
        "election_details" : data ,
        "today" : today_date
    }
    return render(request, 'voteSelection.html', context)

def voterInput(request):
    if (request.method == "POST" and 'election-name' in request.POST):
        elec_name = request.POST.get('election-name')
        context = {"election_name" : elec_name}
        return render(request, 'voterInput.html', context)
    if (request.method == "POST" and 'submit' in request.POST):
        voterId = request.POST.get('voterid')
        dob = request.POST.get('dob')
        elec_name = request.POST.get('submit')
        context = {"election_name" : elec_name}
        context['vid'] = voterId
        year = dob[0:4]
        month = dob[5:7]
        day = dob[8:]
        input_date = datetime.date(int(year), int(month), int(day))
        today = datetime.date.today();
        age = today.year - input_date.year - ((today.month, today.day) < (input_date.month, input_date.day))
        if(age < 18):
            messages.error(request, 'Invalid Id or DOB')
            return render(request, 'voterInput.html', context)
        else:
            prevVote = VoteGivenData.objects.all()
            print(prevVote)
            for user in prevVote:
                if(user.election_name == elec_name and user.voter_ID == voterId):
                    messages.error(request, 'You had Already given the Vote')
                    return render(request, 'voterInput.html', context)
            fileObj = ElectionList.objects.get(election_name=elec_name)
            res = validVoter(fileObj, voterId)
            if(res == False):
                messages.error(request, 'Invalid Id or DOB')
                return render(request, 'voterInput.html', context)
            else:
                # print(elec_name)
                party_obj = PartyName.objects.all()
                party_name = [];
                for party in party_obj:
                    name = party.region_name
                    if(name[0] == elec_name[0] or name == 'All'):
                        party_name.append(party.party_name);
                context['partylist'] = party_name;                        
                return render(request, 'ballot.html', context)
    return render(request, 'voterInput.html')

def ballot(request):
    return render(request, 'ballot.html')

def validVoter(fileObj, voterId):
    # print(fileObj);
    # print(fileObj.filename);
    # print(fileObj.upload_file.name);
    # print(fileObj.upload_file.path);
    # print(fileObj.upload_file.url);
    fileContent = pd.read_excel(fileObj.upload_file.path)
    voterIdList = pd.DataFrame(fileContent, columns= ['VoterID']);
    # print(fileContent)
    # print(voterIdList)
    listtolist = voterIdList.values
    listVal =  [item for elm in listtolist for item in elm];
    strVal = " ".join(listVal)
    # print(listtolist)
    # print(strVal)
    # print(listVal)
    # print(voterId)
    # print(rabinKarp.search(voterId, strVal, 101))
    return rabinKarp.search(voterId, strVal, 101);

    