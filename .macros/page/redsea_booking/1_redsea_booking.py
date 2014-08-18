import os


def main(j, args, params, tags, tasklet):

    page = args.page
    params.result = page

    pars = args.expandParamsAsDict()
    page.addJS('//redseacat.checkfront.com/lib/interface--30.js')

    if 'item_id' in pars:
      page.addJS(jsContent='''
          $(function() {{
              $('a.bookButton').on('click', function(e) {{
                  new CHECKFRONT.Widget ({{
                      host: 'redseacat.checkfront.com',
                      target: 'CHECKFRONT_WIDGET_01',
                      item_id: '{item_id}',
                      category_id: '{category_id}',
                      style: 'color: 000',
                      provider: 'droplet'
                  }}).render();
              }});
          }});
          '''.format(category_id=pars['category_id'], item_id=pars['item_id']))
    else:
        page.addJS(jsContent='''
          $(function() {{
              $('a.bookButton').on('click', function(e) {{
                  new CHECKFRONT.Widget ({{
                      host: 'redseacat.checkfront.com',
                      target: 'CHECKFRONT_WIDGET_01',
                      category_id: '{category_id}',
                      style: 'color: 000',
                      provider: 'droplet'
                  }}).render();
              }});
          }});
          '''.format(category_id=pars['category_id']))


    page.addMessage('''
        <a class="bookButton" href="#" data-toggle="modal" data-height=320 data-width=450 data-target="#myModal">Book Now</a>
           <div class="modal fade" id="myModal" tabindex="-1" role="dialog"  aria-labelledby="myModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                 <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                        <h4 class="modal-title" id="myModalLabel">Booking</h4>
                   </div>
                 <div class="modal-body">
                    <div id="CHECKFRONT_WIDGET_01"><p id="CHECKFRONT_LOADER" style="background: url('//redseacat.checkfront.com/images/loader.gif') left center no-repeat; padding: 5px 5px 5px 20px">Searching Availability...</p></div>
                 </div>
                </div><!-- /.modal-content -->
             </div><!-- /.modal-dialog -->
          </div><!-- /.modal -->
        ''')

    return params


def match(j, args, params, tags, tasklet):
    return True
