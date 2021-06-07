# Import the required modules
import os
import asyncio
import requests
from requests_html import HTML
from aiohttp import ClientSession


async def multi_page_scrape():
    '''Scraping the all comic pages'''
    
    for i in range(1,101): # we can scrape all the pages but here i'm scraping only 100 of the (total xkcd comic pages --> above 2300)
        url = f'https://xkcd.com/{i}/'
        async with ClientSession() as session:
            async with session.get(url) as resonse:
                resonse.raise_for_status
                html_content = await resonse.read()
                
                # saving the html content in Results folder
                
                with open(f'Results\multi\comic{i}.html','w') as f:
                    source = f.write(html_content.decode())

                with open(f'Results\multi\comic{i}.html','r') as f:
                    source = f.read()
                    html = HTML(html=source)

                # Comic-Title
                ctitle = html.find('#ctitle',first=True).text
                print(f'Comic-title --> {ctitle}')
                
                # Image-info
                comic_img = html.find('#comic img',first=True)
                # print(comic_img)
                img_link = 'https:'+comic_img.attrs['src']
                title = comic_img.attrs['title']
                print(f'Image-title --> {title}')

                # saving image in local
                try:
                    r = requests.get(img_link)
                    r.raise_for_status()
                    with open(f'Results/multi/comic/{ctitle}.jpg','wb') as f:
                        f.write(r.content)
                except Exception as e:
                    print('Image not saved in local.Due to ',e)


if __name__ == '__main__':

    # Running all web page
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(multi_page_scrape())

    print('Code Completed 🔥')
