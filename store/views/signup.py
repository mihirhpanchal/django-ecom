from django.views import View
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        firstName = postData.get('firstName')
        lastName = postData.get('lastName')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'firstName': firstName,
            'lastName': lastName,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(firstName=firstName,
                            lastName=lastName,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            #print(firstName, lastName, phone, email, password)
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.firstName):
            error_message = "First Name Required !!"
        elif len(customer.firstName) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.lastName:
            error_message = 'Last Name Required'
        elif len(customer.lastName) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        return error_message
