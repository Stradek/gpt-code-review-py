# gpt-code-review-py
It was interesting project, there are a lot of issues when it comes to actually using it on large scale. When sending large request to GPT to read data from code files, and if amount of data will reach or be close to tokens count limit(at the moment when I am writing this it is the case) it will leave no space for actually GPT responding to request and it - obviously - won't work properly. It could be resolved by implementing some kind of intelligent way of chunk processing or some other workarounds token limit.

I probably won't be developing it further. I am leaving this repository as a reference for others to look into as an archived(read-only) repository.
