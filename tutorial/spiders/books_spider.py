import scrapy


class BooksSpider(scrapy.Spider):
    name = "top100"
    start_urls = [
            'https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&limit=96&page=1'
        ]

    def parse(self, response):
        with open("books.txt","a",encoding="utf-8") as file:
            
            publishers = response.css("div.publisher span a.alt span::text").extract()
            authors = response.css("div.author span a.alt span::text").extract()
            books = response.css("div.name.ellipsis a span::text").extract() 

            i=0
            while (i<len(books)):
                file.write("Book: "+books[i] +"\n")
                file.write("Author: "+authors[i] +"\n")
                file.write("Publisher: "+publishers[i] +"\n")
                file.write("----------------------------------------------------------\n")
                i+=1
            file.close()
  