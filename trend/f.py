
i = 1
id_s = []

gni_lat = 30.268556249048
gni_long =  77.022399902344

# Filter function(includes caption,like,comment,location,hash_tags or simply no of posts to download, filtering)
def cap():
    caption = raw_input("Please(result depends on your caption) :")
    return caption

def lik():
    likes = int(raw_input("Min likes the displayed should have :"))
    return likes

def comm():
    comments = int(raw_input("Minimum comments the post should have :"))
    return comments

def loc():
    location = raw_input("Search posts on the basis of location (Y/N):")
    if location == 'Y' or location == 'y':
        long = float(raw_input("Enter longitude :"))
        lat = float(raw_input("Enter latitude :"))
        return (long, lat)
def tagged():
    tags = raw_input("Enter tag(if none type None) :")
    return tags
def max_post():
    count = int(raw_input("Max posts you want to select ?"))
    return count

def filt(raw):
    print "\nChoose filter :"
    choice =raw_input("1.Caption\n2.No of Likes\n3.No of Comments\n4.Location\n5.Tags\n6.All Filters\n7.Max_posts\n8.Continue without filter\n")
    post = []
    if choice=='1':
        caption = cap()
        print caption
        for temp in raw['data']:
            print temp['caption']
            if temp!=None and temp['caption']!=None:
                if temp['caption']['text']==caption:
                    post.append(temp)
        if len(post) != 0:
            return post
        else:
            print "No post with this caption"
            return 0
    elif choice=='2':
        likes = lik()
        for temp in raw['data']:
            if temp['likes']['count']>=likes:
                post.append(temp)
        if len(post) != 0:
            return post
        else:
            print "No post greater than %d likes" % likes
            return 0
    elif choice=='3':
        comments = comm()
        for temp in raw['data']:
            if temp['comments']['count']>=comments:
                post.append(temp)
        if len(post)!=0:
            return post
        else:
            print "No post with this comment"
            return 0
    elif choice=='4':
        long,lat = loc()
        for temp in raw['data']:
            if temp!=None and temp['location']!=None:
                la = temp['location']['latitude']
                lo = temp['location']['longitude']
                if ("%.2f" % la) == ("%.2f" % lat):         # Float formatting for comparision
                    if ("%.2f" % lo) == ("%.2f" % long):
                        post.append(temp)
        if len(post) != 0:
            return post
        else:
            return 0
    elif choice=='5':
        tags = tagged()
        for temp in raw['data']:
            for tag in temp['tags']:
                if tag==tags:
                    post.append(temp)
        if len(post) != 0:
            return post
        else:
            return 0
    elif choice=='6':
        caption = cap()
        likes = lik()
        comments = comm()
        long, lat = loc()
        tags = tagged()
        count = max_post()
        for temp in raw['data']:
            if temp!=None and temp['caption']!=None and temp['location']!=None and len(temp['tags'])!=None:
                if count == 0:
                    if temp['caption']['text'] == caption and temp['likes']['count'] >= likes and temp['comments'][
                        'count'] >= comments and ("%.2f" % temp['location']['latitude']) == ("%.2f" % lat) and (
                        "%.2f" % temp['location']['longitude']) == ("%.2f" % long):
                        for tag in temp['tags']:
                            if tag == tags:
                                post.append(temp)
        if len(post)!=0:
            return post
        else:
            return 0
    elif choice=='7':
        # Controlling the no of times,the loop continues
        count = max_post()
        for temp in raw['data']:
            if temp!=None:
                if count == 0:
                    break
                post.append(temp)
                count = count - 1
        if len(post)!=0:
            return post
        else:
            return 0
    elif choice=='8':
        return raw['data']
    else:
        print "Invalid input. Sorry no 'try again' for filters.\nContinuing ---"






















































































