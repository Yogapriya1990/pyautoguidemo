from playwright.async_api import async_playwright
import asyncio
import re

async def get_ttd_latest_news():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Open TTD Press Releases page
        await page.goto(
            "https://www.tirumala.org/PressReleases.aspx",
            wait_until="networkidle"
        )

        await page.wait_for_timeout(3000)

        print("\n🔔 Latest TTD Press Releases:\n")

        # 🎯 Target ONLY the main content area
        content = page.locator("#ContentPlaceHolder1")

        rows = content.locator("table tr")

        news_count = 0
        total = await rows.count()

        for i in range(total):
            text = (await rows.nth(i).inner_text()).strip()
            text = re.sub(r"\s+", " ", text)

            # Filter real news rows (date + text)
            if re.search(r"\d{2}-\d{2}-\d{4}", text) and len(text) > 40:
                print("•", text)
                news_count += 1

            if news_count == 5:
                break

        if news_count == 0:
            print("⚠️ No press releases found. Page structure may have changed.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(get_ttd_latest_news())
