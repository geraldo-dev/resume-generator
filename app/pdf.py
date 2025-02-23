from fpdf import FPDF


# Criar uma classe personalizada que herda de FPDF
class PDF(FPDF):
    def header(self):
        # Configurar o cabeçalho
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Currículo', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Configurar o rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


def create_pdf(
        entry_name, entry_age='',
        entry_city='',
        entry_email='',
        entry_phone='',
        entry_address='',
        frame_experiences='',
        entry_institution='',
        courses=[]):
    # Criar uma instância da classe PDF
    pdf = PDF()
    pdf.add_page()

    # Configurar a fonte e adicionar os dados do currículo
    pdf.set_font('Arial', '', 12)

    # Adicionar título
    pdf.cell(0, 10, 'Dados Pessoais', 0, 1, 'L')
    pdf.ln(5)

    # Adicionar informações pessoais
    pdf.cell(0, 10, f'Nome: {entry_name}', 0, 1)
    pdf.cell(0, 10, f'Idade: {entry_age}', 0, 1)
    pdf.cell(0, 10, f'Cidade: {entry_city}', 0, 1)
    pdf.cell(0, 10, f'Email: {entry_email}', 0, 1)
    pdf.cell(0, 10, f'Telefone: {entry_phone}', 0, 1)
    pdf.cell(0, 10, f'Endereço: {entry_address}', 0, 1)
    pdf.ln(10)

    # Adicionar seção de experiência profissional
    pdf.cell(0, 10, 'Experiência Profissional', 0, 1, 'L')
    pdf.ln(5)
    pdf.multi_cell(0, 10, frame_experiences)
    pdf.ln(10)

    # Adicionar seção de formação acadêmica
    pdf.cell(0, 10, 'Formação Acadêmica', 0, 1, 'L')
    pdf.ln(5)
    pdf.multi_cell(0, 10, entry_institution)

    # Adicionar seção de formação acadêmica
    pdf.cell(0, 10, 'Cursos', 0, 1, 'L')
    pdf.ln(5)
    for x in courses:
        pdf.multi_cell(0, 10, str(f'{x[0]} data {x[1]}'))

    # Salvar o PDF
    pdf.output('curriculo2.pdf')


print("Currículo gerado com sucesso: curriculo.pdf")
