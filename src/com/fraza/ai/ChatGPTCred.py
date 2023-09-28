import openai

"""
openai url: https://api.openai.com/v1/chat/completions

header dict:
{'X-OpenAI-Client-User-Agent': '{"bindings_version": "0.27.6", "httplib": "requests", "lang": "python", 
 "lang_version": "3.9.7", "platform": "macOS-10.16-x86_64-i386-64bit", "publisher": "openai", "uname": "Darwin 21.6.0 
 Darwin Kernel Version 21.6.0: Thu Mar  9 20:12:21 PST 2023; root:xnu-8020.240.18.700.8~1/RELEASE_ARM64_T6000 
 x86_64"}', 'User-Agent': 'OpenAI/v1 PythonBindings/0.27.6', 'Authorization': 'Bearer sk-
 KP1yAEb4BpZF0jZiybauT3BlbkFJoywVXt9wosliHuLclW50', 'Content-Type': 'application/json'}
 
"""

#openai.api_key = "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"
openai.api_key = "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"

openai.log = True