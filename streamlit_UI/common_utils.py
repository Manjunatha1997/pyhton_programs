import os
import sys
from PIL import Image
# import imagehash
import cv2
import argparse
import shutil
import redis
from pymongo import MongoClient
# def identify_similar_img(frame1, frame2):

#     # hash0 = imagehash.average_hash(Image.open('./images/batch_1_3.jpg')) 
#     # hash1 = imagehash.average_hash(Image.open('./images/batch_1_38_affine.jpg')) 
#     hash0 = imagehash.average_hash(cv2_pil(frame1))
#     hash1 = imagehash.average_hash(cv2_pil(frame2))
#     cutoff = 5
#     print(hash0 , hash1  , hash0 - hash1 )
#     if hash0 - hash1 < cutoff:
#         print('images are similar')
#         similar_images = True
#     else:
#         print('images are not similar')
#         similar_images = False
#     return similar_images



def singleton(cls):
    """
    This is a decorator which helps to create only 
    one instance of an object in the particular process.
    This helps the preserve the memory and prevent unwanted 
    creation of objects.
    """
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton    
class RedisKeyBuilderWorkstation():
    def __init__(self):
        # self.wid = get_workstation_id('livis//workstation_settings//settings_workstation.json')
        self.workstation_name = "WS_01" #get_workstation_by_id(self.wid)
    def get_key(self, camera_id, identifier):
        return "{}_{}_{}".format(self.workstation_name, str(camera_id), identifier)


import pickle

@singleton
class CacheHelper():
    def __init__(self):
        # self.redis_cache = redis.StrictRedis(host="164.52.194.78", port="8080", db=0, socket_timeout=1)
        self.redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0, socket_timeout=1)
        
        print("REDIS CACHE UP!")

    def get_redis_pipeline(self):
        return self.redis_cache.pipeline()
    
    #should be {'key'  : 'value'} always
    def set_json(self, dict_obj):
        try:
            k, v = list(dict_obj.items())[0]
            v = pickle.dumps(v)
            return self.redis_cache.set(k, v)
        except redis.ConnectionError:
            return None

    def get_json(self, key):
        try:
            temp = self.redis_cache.get(key)
            #print(temp)\
            if temp:
                temp= pickle.loads(temp)
            return temp
        except redis.ConnectionError:
            return None
        return None

    def execute_pipe_commands(self, commands):
        #TBD to increase efficiency can chain commands for getting cache in one go
        return None

@singleton
class MongoHelper:
    try:
        client = None
        def __init__(self):
            if not self.client:
                self.client = MongoClient(host='localhost', port=27017)
            self.db = self.client['streamlit']

        def getDatabase(self):
            return self.db

        def getCollection(self, cname, create=False, codec_options=None):
            _DB = 'streamlit'
            DB = self.client[_DB]
            if cname in MONGO_COLLECTIONS:
                if codec_options:
                    return DB.get_collection(MONGO_COLLECTIONS[cname], codec_options=codec_options)
                return DB[MONGO_COLLECTIONS[cname]]
            else:
                return DB[cname]
    except:
        pass    