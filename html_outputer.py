# coding:utf8
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):  # 把每个dict存进去
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<head><meta charset="utf-8"></head>')  # 防乱码
        fout.write('<body>')
        # fout.write('<table>')
        # fout.write('<tr>'
        #            '<th>url</th>'
        #            '<th>title</th>'
        #            '<th>text</th>'
        #            '</tr>')
        # ascii
        for data in self.datas:
            fout.write('<p>title: %s</p>' % data['title'].encode('utf-8'))
            fout.write('<p>url: %s</p>' % (data['url']).encode('utf-8'))
            fout.write('<p>text: %s</p>' % data['summary'].encode('utf-8'))

        # fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
