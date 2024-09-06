import csv
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

            # Write to CSV file
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, email, password])

            return redirect('index')  
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

            # Read from CSV file and check credentials
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[1] == email and row[2] == password:
                        # Authentication successful
                    return redirect('home')  # Redirect to success URL

            # Authentication failed
         # Redirect back to index page or handle accordingly

    return render(request, 'index.html')

# Your other views (contact and working) remain as you have implemented them.


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Write to CSV file
        with open('contacts.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, subject, message])

        # Redirect to a success page or handle accordingly
        return redirect('home')  # Redirect to the 'working' page after submission

    return render(request, 'contact.html')

def working(request):
    return render(request, 'working.html')

def home(request):
    return render(request, 'home.html')
