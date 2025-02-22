import tkinter as tk
from tkinter import ttk
from pdf import create_pdf


list_courses = []


def add_course():
    list_courses.append([
        entry_name_course.get(),
        entry_date_course.get()
    ])

    # clear fields
    entry_name_course.delete(0, tk.END)
    entry_date_course.delete(0, tk.END)


def create_resume():
    personal_data = {
        'entry_name': entry_name.get(),
        'entry_email': entry_email.get(),
        'entry_city': entry_city.get(),
        'entry_age': entry_age.get(),
        'entry_address': entry_address.get(),
        'entry_phone': entry_phone.get(),
        'frame_experiences': text_experiences.get("1.0", tk.END),
        'entry_institution': entry_institution.get(),
        'courses': list_courses
    }

    create_pdf(
        entry_name=entry_name.get(),
        entry_email=entry_email.get(),
        entry_city=entry_city.get(),
        entry_age=entry_age.get(),
        entry_address=entry_address.get(),
        entry_phone=entry_phone.get(),
        frame_experiences=str(text_experiences.get("1.0", tk.END)),
        entry_institution=entry_institution.get(),
        courses=list_courses
    )

    # clear fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    text_experiences.delete("1.0", tk.END)
    entry_institution.delete(0, tk.END)

    print(personal_data)


root = tk.Tk()
root.title('seu curiculo')

# personal data
personal_data = ttk.LabelFrame(root, text='Informações Pessoais', padding=10)
personal_data.pack(fill='x', pady=5, padx=10)


ttk.Label(personal_data, text='Nome:').grid(
    row=0, column=0, sticky='w', padx=5, pady=5)
entry_name = ttk.Entry(personal_data, width=40)
entry_name.grid(row=0, column=1, padx=5, pady=5)


ttk.Label(personal_data, text="Email:").grid(
    row=1, column=0, sticky="w", padx=5, pady=5)
entry_email = ttk.Entry(personal_data, width=40)
entry_email.grid(row=1, column=1, padx=5, pady=5)


ttk.Label(personal_data, text="Cidade:").grid(
    row=2, column=0, sticky="w", padx=5, pady=5)
entry_city = ttk.Entry(personal_data, width=40)
entry_city.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(personal_data, text="Idade:").grid(
    row=3, column=0, sticky="w", padx=5, pady=5)
entry_age = ttk.Entry(personal_data, width=40)
entry_age.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(personal_data, text="Endereço:").grid(
    row=4, column=0, sticky="w", padx=5, pady=5)
entry_address = ttk.Entry(personal_data, width=40)
entry_address.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(personal_data, text="Telefone:").grid(
    row=5, column=0, sticky="w", padx=5, pady=5)
entry_phone = ttk.Entry(personal_data, width=40)
entry_phone.grid(row=5, column=1, padx=5, pady=5)

# Separator line
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=10)

# Frame para as experiências
frame_experiences = ttk.LabelFrame(root, text="Experiências", padding=10)
frame_experiences.pack(fill="x", padx=10, pady=5)

text_experiences = tk.Text(frame_experiences, width=50, height=5)
text_experiences.pack(padx=5, pady=5)

# Separator line
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=10)

# academic background
academic_background = ttk.LabelFrame(
    root, text='Formação Acadêmica', padding=10)
academic_background.pack(fill='x', pady=5, padx=10)

ttk.Label(academic_background, text='Nome da instituição').grid(
    row=0, column=0, sticky='w', padx=5, pady=5)
entry_institution = ttk.Entry(academic_background, width=40)
entry_institution.grid(row=0, column=1, padx=5, pady=5)

# Separator line
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=10)

# courses
courses = ttk.LabelFrame(
    root, text='Cursos', padding=10)
courses.pack(fill='x', pady=5, padx=10)

# criar um for
ttk.Label(courses, text='Nome do Curso').grid(
    row=0, column=0, sticky='w', padx=5, pady=5)
entry_name_course = ttk.Entry(courses, width=40)
entry_name_course.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(courses, text='Data do Curso').grid(
    row=1, column=0, sticky='w', padx=5, pady=5)
entry_date_course = ttk.Entry(courses, width=40)
entry_date_course.grid(row=1, column=1, padx=5, pady=5)

ttk.Button(courses, text='Adicionar', command=add_course).grid(
    row=2, column=0, sticky='w', padx=5, pady=5)

# Separator line
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=10)

# save
save_resume = ttk.LabelFrame(
    root, text='Criar Curriculo', padding=10)
save_resume.pack(fill='x', pady=5, padx=10)

tk.Button(save_resume, text='salva', bg="green", fg="white", command=create_resume).grid(
    row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
save_resume.grid_columnconfigure(0, weight=1)
root.mainloop()
