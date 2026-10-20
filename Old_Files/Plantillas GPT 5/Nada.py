        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Intereses')
        ry -= 12
        ry = draw_wrapped_text(c, rx, ry, PERSONA['Intereses Derecha'], max_width_chars=50, leading=10, size=9)
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Referencias Laborales')
        ry -= 12
        for ref in PERSONA['Referencias Laborales Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + ref, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Referencias Personales')
        ry -= 12
        for ref in PERSONA['Referencias Personales Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + ref, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Pasatiempos')
        ry -= 12
        for hobby in PERSONA['Pasatiempos Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + hobby, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Comidas Favoritas')
        ry -= 12
        for food in PERSONA['Comidas Favoritas Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + food, max_width_chars=50, leading=10, size=9)
            ry -= 4
        self.draw_footer(c, w, h)

    def draw_footer(self, c, w, h):
        footer_y = 50
        c.setFillColor(colors.black)
        c.setFont('Helvetica', 9)
        c.drawString(40, footer_y, PERSONA['Pie de Página'])
        c.line(40, footer_y - 5, w - 40, footer_y - 5)

if __name__ == '__main__':
    palette = {'header': (0.4, 0.1, 0.6), 'titles': (0.2, 0.05, 0.4), 'text': (0, 0, 0)}
    foto = foto4
    Template9(palette, page_size=LETTER).generar_pdf('CV_template_13.pdf', foto)
    print('Generado -> CV_template_13.pdf')