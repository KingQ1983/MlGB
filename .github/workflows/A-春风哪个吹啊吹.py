name: A-春风哪个吹啊吹

on:
  schedule:
    - cron: '1 22,23,0-15/1 * * *'
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        
      - name: 'Set up Python'
        uses: actions/setup-python@v1
        with:
          python-version: 3.7
         
      - name: 'Install requirements'
        run: pip install -r ./-/C.TXT
        
      - name: '-' 
        run: python3 ./-/spring_earn.py
        env:
            DJJ_TELE_COOKIE: ${{ secrets.DJJ_TELE_COOKIE }}
            XMLY_BARK_COOKIE: ${{ secrets.XMLY_BARK_COOKIE }}
            SPRING_EARN_BODY: ${{ secrets.SPRING_EARN_BODY }}
