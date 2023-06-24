import requests
import string
import csv

categories = ['Development', 'Business', 'Design', 'Finance+%26+Accounting', 'Health+%26+Fitness',
              'IT+%26+Software', 'Lifestyle', 'Marketing', 'Music', 'Office Productivity', 'Personal Development',
              'Photography+%26+Video', 'Teaching+%26+Academics']
ids_instructor = []
ids_courses = []


data_courses = "udefrika_data_course.csv"
with open(data_courses, "a") as data_courses:
  data_courses.write("id_udemy;title;url;price;user;category;image;\
    language;description;gift_url;headline;vendor;avg_rating;instructional_level\n\n")
data_courses.close()

data_users = "udefrika_data_instructor.csv"
with open(data_users, "a") as data_users:
  data_users.write("id;title;name;display_name;job_title;\
    image_50x50;image_100x100;initials;url;user_id\n\n")
data_users.close()

base_url = "https://www.udemy.com"
c = 1

for category in categories:  
  print("category: ",c," in progress...")
  i = 0
  url = "https://www.udemy.com/api-2.0/courses/?fields[course]=title,url,avg_rating,\
  visible_instructors,locale,image_480x270,price,price_detail,\
  gift_url,instructional_level,headline,description,category="+category+",is_paid=1"

  while(i<50):
    id_inst = 0
    response = requests.get(url, auth=('key_user','key_id'))
    url = response.json()['next']
    

    for result in response.json()['results']:
      id_udemy =result['id']
      title_course = result['title']
      url_course = base_url + result['url']
      price = 0
      
      if result['price'] != 'Free':
        amount = int(result['price_detail']['amount'])
        price = amount*658 + 5000
      
      user = 1
      category = c
      image = result['image_480x270']

      language = result['locale']['locale']

      description = result['description']
      gift_url = result['gift_url']
      headline = result['headline']
      avg_rating = result['avg_rating']
      instruction_level = result['instructional_level']

      for instructor in result['visible_instructors']:
        id = (str(instructor['image_100x100']))\
        .replace("https://img-c.udemycdn.com/user/100x100/","").replace("_","").replace(".jpg","")
        id = (str(instructor['image_100x100']))\
        .replace("https://img-b.udemycdn.com/user/100x100/","").replace("_","").replace(".jpg","")
        
        title = instructor['title'] 
        name = instructor['name']
        display_name = instructor['display_name']
        job_title = instructor['job_title']
        image_50x50 = instructor['image_50x50']
        image_100x100 = instructor['image_100x100']
        initials = instructor['initials']
        url_instructor = base_url+instructor['url']
        if id not in ids_instructor:
          #print('here')
          ids_instructor.append(id)
          id_inst = len(ids_instructor) - 1 
          try:
            data_users = "udefrika_data_instructor.csv"
            row = []
            row=[str(id_inst),title,name,display_name,job_title,image_50x50,image_100x100,initials,url_instructor,str(1)]
            #print('Ip ',row)
            if result['price'] != 'Free':
              with open(data_users, 'a',encoding="utf-8") as data_users:
                writer = csv.writer(data_users , delimiter=";")
                writer.writerow(row)            
              data_users.close()
          except:
            break
        else:
          id_inst = ids_instructor.index(id)
        

      
      vendor = id_inst

      if price != 0:
        try:
          row_courses = []
          if id_udemy not in ids_courses:
            data_courses = "udefrika_data_course.csv"
            row_courses = [str(id_udemy),str(title_course),url_course,\
            str(price),str(user),str(category),image,language,\
            description,gift_url,headline,str(vendor),str(avg_rating),instruction_level]

            with open(data_courses, "a", encoding="utf-8") as data_courses:
              writer = csv.writer(data_courses, delimiter=";")
              writer.writerow(row_courses)
            data_courses.close()
            i+=1
            ids_courses.append(id_udemy)
        except:
          pass

  print("category: ",c," finished !")
  c+=1


