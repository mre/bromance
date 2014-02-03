bromance
========

## ...a client for bro and TLDR

Manpages are lame? What you need are some use cases for a command?

![I know that feeling, bro](https://raw2.github.com/mre/bromance/master/hug.png)

TLDR and bro give me exactly that. Bromance.py is a friendly lookup tool for bro and TLDR.

# Example usage

    > python bromance.py curl

    ## Get The Contents Of A Web Page
    curl http://bropages.org

    ## Download A File And Write It To Another File Called Myfile.Html
    curl -o myfile.html http://bropages.org

    ## Send A Header With Curl
    curl --header "X-BeerIsInteresting: 1" www.bropages.org

    ## Get My External Ip Address 
    curl ifconfig.me/ip

    ## Get My Remote Host
    curl ifconfig.me/host

    ## Get My User Agent
    curl ifconfig.me/ua


Currently only command lookup is supported.
