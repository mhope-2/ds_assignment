from . import models
from .forms import ContactForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, TemplateView
import phonenumbers
import random
import requests
# Create your views here.

class Index(CreateView):
    model = models.Contact
    form_class = ContactForm
    template_name = 'index.html'
    success_url = reverse_lazy('thanks')


class Thanks(TemplateView):
    template_name = 'thanks.html'

class FileView(ListView):
    model = models.Contact
    template_name = 'file_page.html'
    queryset = models.Contact.objects.all()

    def get_context_data(self, **kwargs):

        try:
            with open('media/files/contact.txt', 'r') as file:
                # ALGORITHM TO READ AND CLEAN FILE USING phonenumbers LIRARY AND ROUTE NETWORK PREFIXES TO DB
                file.seek(0)
                content = file.readlines()
                
                for i in content:
                    try:
                        x = phonenumbers.parse(i)
                        phone_number = list(str(x).split(' '))
               
                    except:
                            print("Not a contact")

                            country_code = phone_number[2]
                            national_number = phone_number[-1]
                            network_prefix = "0"+phone_number[-1][0:2]
                            print(country_code, ' ', national_number, ' ', network_prefix)
                                
                            if (network_prefix == "024" | network_prefix == "054" | network_prefix == "059"):
                                models.Contact(mtn)
                            elif network_prefix == "020":
                                models.Contact(vodafone)
                            elif network_prefix == "026" | network_prefix == "056" | network_prefix == "027" | network_prefix == "057":
                                models.Contact(airtelTigo)
                        
                        
                   
                # END ALGORITHM TO READ AND CLEAN FILE USING phonenumbers LIRARY AND ROUTE NETWORK PREFIXES TO DB
                
                        # ALGORITHM TO SPLIT THE DATA INT0 PERCENTAGES AND SEND TO RESPECTIVE URLS

                            f60 = open("60-percent-output.txt", 'wb') # file to store 60% of the data
                            f40 = open("40-percent-output.txt", 'wb') # file to store 40% of the data

                            for line in file:
                                r = random.random()
                                if r <= 0.6:
                                    f60.write(line)
                                else:
                                    f40.write(line)
                            f60.close()
                            f40.close()

                            URLA = "http://domainA:12345/sendsms?username=domainA&password=passA&to=233548617798&from=senderA&text=TestA"
                            URLB = "http://domainB:09876/sendsms?username=domainB&password=passB&to=233267722174&from=senderB&text=TestB"
        
                            dataA = f60
                            dataB = f40
                            
                            requests.post(URLA, data=dataA) # post 60% to URL A
                            requests.post(URLB, data=dataB) # post 40% to URL B
                            
                        # END ALGORITHM TO SPLIT THE DATA INT0 PERCENTAGES AND SEND TO RESPECTIVE URLS
        except:
            print("File Not Found")

        
        context = super(FileView, self).get_context_data(**kwargs)
        name = list(str(x).split(' '))
        context['country_code'] = name[2]
        context['national_number'] = name[-1]
        context['network_prefix'] = "0"+name[-1][0:2]
        return context


  
    
        


