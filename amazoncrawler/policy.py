from scrapy_proxy_pool.policy import BanDetectionPolicy


class MyPolicy(BanDetectionPolicy):
    def response_is_ban(self, request, response):
        # use default rules, but also consider HTTP 200 responses
        # a ban if there is 'captcha' word in response body.
        ban = super(MyPolicy, self).response_is_ban(request, response)
        # ban = ban or bool(response.css('#captchacharacters').extract_first())
        if b'captcha' in response.body:
            print("############ Captcha Found ############")
            ban = True
        return ban

    def exception_is_ban(self, request, exception):
        # override method completely: don't take exceptions in account
        return super(MyPolicy, self).exception_is_ban(request, exception)
