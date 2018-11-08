import os


if __name__ == "__main__":
    with open("file_list.html", "w") as f:
        source_files = []
        f.write("<ul>\n")
        for c in range(4, 17):
            dir_name = "chapter_{:02d}".format(c)
            f.write("\t<li>{}\n\t\t<ul>\n".format(dir_name))

            for root, dirnames, filenames in os.walk(dir_name):
                for filename in filenames:
                    if filename.endswith(('.html')):
                        source_files.append(root+"/"+filename)
                        f.write("\t\t\t<li><a href=\"{}\">{}</a></li>\n".format(root+"/"+filename, filename))
            f.write("\t\t</ul>\n\t</li>\n")
        f.write("</ul>\n")