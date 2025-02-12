def handle_uploaded_file(f):  
    with open('pdf/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 