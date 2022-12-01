# DOWNLOAD PDF FILES WITH SCRAPY CRAWL SPIDER

Download all books from [Hindawi organization's website](https://www.hindawi.org/) in multiple formats.

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Scrapy 2.1.0+](https://scrapy.org/)

> Open terminal inside the project's folder

### Installing
```
pip install scrapy
```
### Running Project
```
scrapy crawl hindawi
```

### Additional
> To scrap another category change in <code>hindawi.py</code> <strong>both lines</strong> [`Line 11`](https://github.com/McCdama/scrapySpider/blob/0c3d4677b65d58f2fec507318bebcd99f69be080/scrapySpider/spiders/hindawi.py#L11) <strong>and</strong> [`Line 14`](https://github.com/McCdama/scrapySpider/blob/0c3d4677b65d58f2fec507318bebcd99f69be080/scrapySpider/spiders/hindawi.py#L14) to the desired link categotry.


> Supported extension formats are following: <strong>.kfx</strong>, <strong>.pdf</strong> and <strong>.epub</strong>

> To open <strong>.epub</strong> extension, download <strong>ADE [[Adobe Digital Edition](https://www.adobe.com/solutions/ebook/digital-editions/download.html)]</strong>

> To download different extension files, change the extension name in <code>hindawi.py</code> on [`Line 21`](https://github.com/McCdama/scrapySpider/blob/0c3d4677b65d58f2fec507318bebcd99f69be080/scrapySpider/spiders/hindawi.py#L21).
