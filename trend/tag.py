import requests
from locker import base_url,app_access_token
from Plotting import plot_graph,plot_fig


def hash_tag_popularity():
    hash_tags = []    # To store hash_tags entered by user
    count = []        # Media counts respective to tags
    while True:
        choice = raw_input("1. Enter tags\n2. Default hash tags ")
        if choice == '1':
            nos = int(raw_input("How many hash_tags u want to search :"))
            print "Enter tags :"
            while (nos != 0):
                tag = raw_input("")
                hash_tags.append(tag)
                nos = nos - 1
            break
        elif choice == '2':
            hash_tags = ['python', 'nostalgic', 'programming']
            print "Default tags :", hash_tags
            break
        else:
            print "Invalid input. Re-enter"

    for temp in hash_tags:
        request_url = (base_url + 'tags/%s/?access_token=%s') % (temp, app_access_token)
        raw = requests.get(request_url).json()   # Requesting for response for a specific tag-id
        if raw['meta']['code'] == 200:
            if len(raw['data']):
                print "%s images is shared with the tag %s" % (raw['data']['media_count'], temp)
                count.append(raw['data']['media_count'])
            else:
                print "No images shared with this tag"
        else:
            print "Error code :%s" % raw['meta']['code']

    print "Following graph, showing most popular hash_tags"
    while True:
        scan = raw_input("\n1. Analyse the data in plot graph\n2. Analyse the data in line-graph\n3. Back")
        if scan == '1':
            plot_fig(hash_tags,count)
        elif scan == '2':
            plot_graph(hash_tags, count)
        elif scan == '3':
            break
        else:
            print "Invalid input"
