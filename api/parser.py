from BeautifulSoup import BeautifulSoup as bs
import datetime
#from models import *

def get_attribute(obj, prop='menudate'):
    attrs = obj.attrs
    prop = prop.lower()
    if not attrs:
        return None
    for attr in attrs:
        if attr[0].lower() == prop:
            return attr[1]
    return None

f=open('684','r')

data = bs(f.read())

days = data.findAll('tblmenu')

# todo make this more modular. possibly recursive or functional
for day in days:
    date = get_attribute(day,'menudate')
    if date:
        date = datetime.datetime.strptime(date,'%m/%d/%Y').date()
    periods = day.findAll('tbldaypart')
    try:
        for period in periods:
            print "in periods now"
            # print period
            # bld -> breakfast, lunch or dinner (these are the options as well)
            bld = period.txtdaypartdescription.text.lower()
            meals = day.findAll('tblitem')
            try:
                for meal in meals:
                    meal_name = meal.txttitle.text
                    print meal_name
                    try:
                        attrs = meal.findAll('txtattribute')
                        attr_li = []
                        for at in attrs:
                            try:
                                attr_li.append(at.description.text)
                            except:
                                pass
                            print attr_li
                            # save stuff
                    except:
                        pass
            except:
                pass
    except:
        pass
