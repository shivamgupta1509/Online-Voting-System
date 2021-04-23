from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    msg = models.TextField()
    date = models.DateField()

    def __str__(self):
        datestr = str(self.date)
        displaytext = self.name+"("+datestr+")"
        return displaytext

class ElectionList(models.Model):
    election_name = models.CharField(max_length=122)
    election_date = models.DateField()
    filename = models.CharField(max_length=122)
    election_img = models.ImageField(upload_to='electionimg')
    upload_file = models.FileField(upload_to='files')

    def __str__(self):
        return self.election_name

class VoteGivenData(models.Model):
    election_name = models.CharField(max_length=122)
    voter_ID = models.CharField(max_length=122)

    def __str__(self):
        display_text = self.election_name + "(" + self.voter_ID + ")"
        return display_text

class PartyName(models.Model):
    region_name =  models.CharField(max_length=122);
    party_name = models.CharField(max_length=122);

    def __str__(self):
        display_text = self.party_name + "(" + self.region_name + ")"
        return display_text;
    
    
    