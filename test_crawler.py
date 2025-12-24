from crawler import crawl_website

url = "https://docs.python.org/3/tutorial/index.html"  # replace with your real website
pages = crawl_website(url)

print("Total pages extracted:", len(pages))

if pages:
    print("First page content (500 chars):")
    print(pages[0][:500])
else:
    print("❌ No content extracted")
