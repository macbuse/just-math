#! /home/gregmcshane/anaconda3/bin/python3.6 

import requests
import subprocess

import os, re, time
import json #serialise

class Voices():
    voices ={'K' : 'en-GB_KateV3Voice',
         'M' : 'en-US_MichaelV3Voice',
         'O' : 'en-US_OliviaV3Voice'
        }
    
    def __init__(self):
        if not os.path.isfile('script.json'):
            self.inventory = {}
        else:
            self.inventory = json.load(open('script.json','r'))
             
    def string2fn(self, xx):
        '''hash function
        strip punctuation
         return first 3 words with sep=_'''
        #strip punctuation - > lowercase
        u = re.sub(r'[^\w\s]','', xx).lower().split()
        #check and pad
        if len(u) < 3:
            u.extend(['blah']*3)
        return '_'.join(u[:3]) + '.mp3'

    def get_audio(self,to_say):

        actor, txt = to_say
        fn = self.string2fn(txt)

        print('Doing', fn)

        url = 'https://text-to-speech-demo.ng.bluemix.net/api/v3/synthesize'
        params = {'text' : txt,
                  'voice' : self.voices[actor],
                  'download' : 'true',
                  'accept' : 'audio/mp3'
                 }

        r = requests.get(url, params=params)

        with open('%s'%fn,'wb') as fp:
            fp.write(r.content)
            
    def add(self, txts):

        for tt in txts:
            actor, lines = tt
            fn = self.string2fn(lines)

            if fn in self.inventory and self.inventory[fn] == lines:
                print('skipping', fn)
                continue
            self.get_audio(tt)
            time.sleep(20)

        with open('script.json','w') as fp:
            actor, lines = list( zip(* txts))
            json.dump( { self.string2fn(x) : x for x in lines} , fp)
    
        print('DONE')
        
    def __repr__(self):
        return str('\n'.join(self.inventory.keys()))
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('usage: mk_slides.py file.md')
        sys.exit(1)
    fn = sys.argv[1]
    with open(fn,'r') as fp:
        md = fp.read()
        
    voices = Voices()
    print(voices)
    #delegate this
    string2fn = voices.string2fn
    
    #I have special tags for speach and changing font size in math
    #!![voice key](text) for speech 
    # voices key is one of M, K, O
    #percentage$...$ for resizing TeX fonts
    pp_audio = re.compile(r'!!\[(.*?)\]\((.*?)\)',re.DOTALL)
    pp_math =  re.compile(r'(\d+)(\$.*\$)',re.DOTALL)
    
    def audio_cb(match):
        wrapper = '<audio  data-autoplay ><source src="{}" ></audio>'
        return wrapper.format(string2fn(match.group(2)) )
    
    def math_cb(match):
        wrapper = '<div style="font-size: {}%">{}</div>'
        return wrapper.format(match.group(1), match.group(2))
    
    #make the html first as it is local
    xx = re.sub(pp_audio, audio_cb, md)
    md_with_tags = re.sub(pp_math, math_cb, xx)
    
    with open('tmp.md','w') as fp:
        fp.write(md_with_tags)
        
    #split this (past col 80) so that we can replace for -o later if we want
    pandoc_it = 'pandoc -t revealjs -s -o slides.html tmp.md -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/ -i'.split()
    
    subprocess.call(pandoc_it)
    
    #this has a lot of latency
    voices.add(pp_audio.findall(md))
