import os


def main(j, args, params, tags, tasklet):

    page = args.page
    params.result = page

    page.addCSS("/{}/.files/css/jquery.fancybox.css".format(args.doc.getSpaceName()))
    page.addJS("/{}/.files/js/jquery.fancybox.min.js".format(args.doc.getSpaceName()))
    page.addJS(jsContent='''
        $(document).ready(function() {
          $('.fancybox').fancybox({
            padding   : 0,
            maxWidth  : '100%',
            maxHeight : '100%',
            autoSize  : true,
            closeClick  : true,
            openEffect  : 'elastic',
            closeEffect : 'elastic'
          });
        });''')

    for video in args.cmdstr.splitlines():
        parts = video.split(':', 1)
        video_id = parts[0]
        if len(parts) > 1:
            video_title = parts[1]
        else:
            video_title = '&nbsp;'
        page.addMessage('''
            <article class="video">
                <figure>
                  <a class="fancybox fancybox.iframe" href="//www.youtube.com/embed/{video_id}?wmode=transparent">
                  <img class="videoThumb" src="//i1.ytimg.com/vi/{video_id}/mqdefault.jpg"></a>
                </figure>
                <h2 class="videoTitle">{video_title}</h2>
            </article>'''.format(video_id=video_id, video_title=video_title))

    return params


def match(j, args, params, tags, tasklet):
    return True

