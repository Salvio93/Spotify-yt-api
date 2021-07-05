from apiclient.discovery import build
import sys, requests, Get_playlist_item

ACCESS_KEY = "AIzaSyDC45wmudZS6VvjdVJKCRhf_DF0ghn3et4"
youtube = build('youtube', 'v3', developerKey = ACCESS_KEY)


#fct to search in the youtube bar
#return: dic of the first items found
def search_item(q1,part1,type1,maxResults1):
    response = youtube.search().list(
        q = q1,
        part = part1,
        type = type1,
        maxResults = maxResults1 
    )
    json_rep = response.execute()
    return json_rep['items']

    

def end(q1,part1 = 'snippet',type1 = 'video',maxResults1 =5):
    test = {} #dictionary of url : duration
    yt_url = 'https://www.youtube.com/watch?v='

    youtube_item = search_item(q1,part1,type1,maxResults1)

    
    #set the dic of 5 youtube link : 5 duration
    for e in range(maxResults1):

        #list of url
        tmp = youtube_item[e]['id']['videoId']
        #find duration
        yt_dur = youtube.videos().list(part = 'contentDetails',id = tmp)
        duration = yt_dur.execute()['items'][0]['contentDetails']['duration']
        try:
            x = float(duration[2] + '.' +duration[4] + duration[5])
        except:
            x = -1

        test[yt_url + youtube_item[e]['id']['videoId']] = [x]
    print(test)
    
  
    
    count_list = frequenty_list(test)
    best_count,best_indx = most_frequent_val(count_list)

    list_test = list(test.keys())
    
    return list_test[best_indx]


#find biggest val in a list of int
def most_frequent_val(count_list):
    if count_list[0] == count_list[1] == count_list[2] == count_list[3] == count_list[4]:
        return 0,0
    best = count_list[0]
    for z in range(len(count_list)):
        if count_list[z] >= best:
            best = count_list[z]
            best_index = z
    return best, best_index
#fct to find most pertinent yt video 
def frequenty_list(dic):
    value_list = list(dic.values())
    
    count =[0,0,0,0,0]

    #for each unique value in value_list, count the frequency, and return the max
    for x in range(len(value_list)):
        for y in range(len(value_list)):
            if x!=y:
                if value_list[x][0] == value_list[y][0]:
                    count[x] +=1
                else:
                    if abs(value_list[x][0] - value_list[y][0]) <= 0.10:
                        count[x] += 0.5
                    
    return count
    


def ending():
    tmp1 = []
    spotif_item = Get_playlist_item.get_playlist_item('BE',15)
    print(spotif_item)
    for k, v in spotif_item.items():
        name = k + ' - ' + v
        lien = end(name)
        print("-----------------------------------")
        tmp1.append(lien)
        print(tmp1)


    return tmp1

