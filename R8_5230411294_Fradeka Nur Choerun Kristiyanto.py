import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AgeCategoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Penentu Kategori Usia")
        self.root.geometry("500x600")
        self.create_widgets()

    def create_widgets(self):
        # Label judul
        title_label = tk.Label(self.root, text="Penentu Kategori Usia", font=("Arial", 16))
        title_label.pack(pady=10)

        # Label dan Entry untuk nama
        self.name_label = tk.Label(self.root, text="Nama:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.pack(pady=5)

        # Label dan Entry untuk usia
        self.age_label = tk.Label(self.root, text="Usia:")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self.root, width=40)
        self.age_entry.pack(pady=5)

        # Tombol untuk menentukan kategori usia
        self.check_button = tk.Button(self.root, text="Tentukan Kategori", command=self.check_age_category)
        self.check_button.pack(pady=10)

        # Tabel untuk menampilkan hasil
        self.tree = ttk.Treeview(self.root, columns=("Nama", "Usia", "Kategori"), show="headings", height=10)
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Usia", text="Usia")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.column("Nama", width=150)
        self.tree.column("Usia", width=100)
        self.tree.column("Kategori", width=150)
        self.tree.pack(pady=10)

        # Tombol untuk menghapus data
        self.delete_button = tk.Button(self.root, text="Hapus Data Terpilih", command=self.delete_selected_data)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Hapus Semua Data", command=self.clear_all_data)
        self.clear_button.pack(pady=5)

    def check_age_category(self):
        # Ambil input nama dan usia
        name = self.name_entry.get()
        age = self.age_entry.get()

        # Validasi input
        if not name or not age:
            messagebox.showerror("Error", "Nama dan Usia harus diisi!")
            return

        if not age.isdigit():
            messagebox.showerror("Error", "Usia harus berupa angka!")
            return

        age = int(age)

        # Tentukan kategori usia
        if age <= 12:
            category = "Anak-anak"
        elif 13 <= age <= 17:
            category = "Remaja"
        elif 18 <= age <= 59:
            category = "Dewasa"
        else:
            category = "Lanjut Usia"

        # Tambahkan hasil ke tabel
        self.tree.insert("", "end", values=(name, age, category))

        # Bersihkan input
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

    def delete_selected_data(self):
        # Ambil item yang dipilih
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Tidak ada data yang dipilih!")
            return

        # Hapus item yang dipilih
        for item in selected_item:
            self.tree.delete(item)

    def clear_all_data(self):
        # Konfirmasi sebelum menghapus semua data
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus semua data?")
        if confirm:
            for item in self.tree.get_children():
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCategoryApp(root)
    root.mainloop()
