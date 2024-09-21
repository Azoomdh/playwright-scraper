from playwright.async_api import async_playwright
import asyncio

async def main():
    browsers = ['chromium']
    async with async_playwright() as p:
        for browser_type in browsers:
            browser = await p[browser_type].launch(headless= False)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto('https://www.thegioididong.com/laptop')

            # thực hiện hàm tại đây
            
            listCate= await page.query_selector_all('.__cate_44')
            for cate in listCate:
                # lướt qua đối tượng
                await cate.hover() 
            #

            # thực hiện hàm tại đây
           
            await page.wait_for_timeout(1000)
            await browser.close()
        #
    #
#

asyncio.run(main())
