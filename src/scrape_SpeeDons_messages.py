from chat_downloader import ChatDownloader
from tqdm import tqdm
import concurrent.futures

def get_chat_messages(chat):
    """Function to dump chat messages into JSON file"""
    for message in tqdm(chat):
        continue

def get_all_chats_messages(chats):
  """Function to get all chats messages, use multithreading to speed up process"""
  threads = min(MAX_THREADS, len(chats))

  with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(get_chat_messages, chats)

if __name__ == "__main__":

    MAX_THREADS = 30

    SPEEDONS_VODS = ["https://www.twitch.tv/videos/1456751131",
                "https://www.twitch.tv/videos/1458203401",
                "https://www.twitch.tv/videos/1458516561"]

    downloader = ChatDownloader()
    chats = []

    #get chats objects into a list, one for each VOD
    for i, vod in enumerate(SPEEDONS_VODS):
        chats.append(downloader.get_chat(url=vod, output=f"../data/chat_vod{i+1}.json")) 

    #get actual messages, takes 11 minutes on Google Colab
    print("Scrapping messages...")
    get_all_chats_messages(chats)
    print("Messages scrapped successfully!")
    
    #merge all files to get final SpeeDons chat messages file
    files=["../data/chat_vod1.json", "../data/chat_vod2.json", "../data/chat_vod3.json"]
    print("Merging files...")
    with open("../data/SpeeDons_chat.json", "w") as outfile:
        outfile.write("{}".format("\n".join([open(f, "r").read() for f in files])))
    print('Files merged successfully into ../data/SpeeDons_chat.json !')