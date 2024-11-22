import asyncio
from typing import List

from twikit import Tweet

from TwikiHelper import TwikitHelper


## create&update cookies.json via -> x.com -> developer options -> application -> storage -> cookies
##{"auth_token":"your_auth_token,"ct0":"your_ct0_value"}
async def main():
    helper = TwikitHelper(cookies_path='cookies.json')
    result:List[Tweet] = await helper.get_time_line(tweet_count=20)
    ##print(result)

    print(f"tweet is -> {result.__getitem__(0).text}")
    print(f"tweet owner is -> {result.__getitem__(0).user.screen_name}")




asyncio.run(main())
