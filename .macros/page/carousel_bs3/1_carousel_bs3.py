import os


def main(j, args, params, tags, tasklet):

    page = args.page
    params.result = page

    images = args.cmdstr.splitlines()

    page.addMessage('''<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">''')

    for i, image in enumerate(images):
        active = 'active' if i == 0 else ''
        page.addMessage('<li data-target="#carousel-example-generic" data-slide-to="{}" class="{}"><img src="{}" alt=""></li>'.format(i, active, image))

    page.addMessage('''</ol>
          <div class="carousel-inner">''')

    for i, image in enumerate(images):
        active = 'active' if i == 0 else ''
        page.addMessage('''
            <div class="item {0}">
              <img src="{1}" alt="">
             </div>'''.format(active, image))

    page.addMessage('''
          </div>
          <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
            <span class="arrow-l"><img src="/images/$$space/arrow-l.png"></span>
          </a>
          <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
            <span class="arrow-r"><img src="/images/$$space/arrow-r.png"></span>
          </a>
        </div>''')

    return params


def match(j, args, params, tags, tasklet):
    return True

