# gpt-code-review-py
It was interesting project, there are some issues when it comes to actually using in real project like game engine. 
When sending large request to GPT to read data from code files, and if amount of data will reach or be close to tokens count limit(at the moment when I am writing this it is the case) it will leave no space for actually GPT responding to request and it - obviously - won't work properly. It could be resolved by implementing some kind of intelligent way of chunk processing or some other workarounds token limit.
But there is also need for GPT to understand context of changes sent for review to GPT as other, unaffected parts of code base.
It also could be resolved in some way, but I don't want to explore it right now, as there are actual real efforts to make real, commertial(or open-source) tools out of it right now.

I probably won't be developing it further. I am leaving this repository as a reference for others to look into as an archived(read-only) repository.
