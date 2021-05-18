import typer
import time
import requests
from typing import Optional

app = typer.Typer()
timeout = 5


@app.command()
def url(url: str):
    start = time.time()
    try:
        if url[:8] == 'https://' or url[:7] == 'http://':
            print(url)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            data = requests.get(url, headers=headers)
            code = data.status_code
            code_int = isinstance(code, int)
            if code_int:
                if code == 200:
                    response = typer.style(f'Reachable [{code}]', fg=typer.colors.GREEN, bold=True)
                    typer.echo(response)
                else:
                    response1 = typer.style('Reachable', fg=typer.colors.GREEN, bold=True)
                    response2 = typer.style(f' [{code}]', fg=typer.colors.RED, bold=True)
                    typer.echo(response1 + response2)
            else:
                response = typer.style('Not Reachable', fg=typer.colors.RED, bold=True)
                typer.echo(response)
        else:
            url1 = 'https://' + url
            url2 = 'http://' + url
            try:
                print(url1)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
                data = requests.get(url1, headers=headers)
                code = data.status_code
                code_int = isinstance(code, int)
                if code_int:
                    if code == 200:
                        response = typer.style(f'Reachable [{code}]', fg=typer.colors.GREEN, bold=True)
                        typer.echo(response)
                    else:
                        response1 = typer.style('Reachable', fg=typer.colors.GREEN, bold=True)
                        response2 = typer.style(f' [{code}]', fg=typer.colors.RED, bold=True)
                        typer.echo(response1 + response2)
                else:
                    response = typer.style('Not Reachable', fg=typer.colors.RED, bold=True)
                    typer.echo(response)

            except Exception:
                print(url2)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
                data = requests.get(url2, headers=headers)
                code = data.status_code
                code_int = isinstance(code, int)
                if code_int:
                    if code == 200:
                        response = typer.style(f'Reachable [{code}]', fg=typer.colors.GREEN, bold=True)
                        typer.echo(response)
                    else:
                        response1 = typer.style('Reachable', fg=typer.colors.GREEN, bold=True)
                        response2 = typer.style(f'[{code}]', fg=typer.colors.RED, bold=True)
                        typer.echo(response1 + response2)
                else:
                    response = typer.style('Not Reachable', fg=typer.colors.RED, bold=True)
                    typer.echo(response)
    except Exception:
        response = typer.style('ConnectionError! Not Reachable', fg=typer.colors.RED, bold=True)
        typer.echo(response)
    end = time.time()
    print(f'\nScanning Completed within {end-start}s.')


@app.command()
def file(inputname: str, outputname: str, outputOption: bool = typer.Option(True, "--reachableurl", "-r")):
    start = time.time()
    try:
        with open(inputname, 'r') as file:
            with open(outputname, 'w') as r:
                for line in file:
                    if line.isspace() or len(line) == 0:
                        continue
                    else:
                        try:
                            if line[:8] == 'https://' or line[:7] == 'http://':
                                url = line[:-1]
                                print(url)
                                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
                                data = requests.get(url, headers=headers, timeout=timeout)
                                code = data.status_code
                                code_int = isinstance(code, int)
                                if code_int:
                                    r.write(str(url) + '\n')
                                    if code == 200:
                                        response = typer.style(f'Reachable [{code}]', fg=typer.colors.GREEN, bold=True)
                                        typer.echo(response)
                                    else:
                                        response1 = typer.style('Reachable', fg=typer.colors.GREEN, bold=True)
                                        response2 = typer.style(f' [{code}]', fg=typer.colors.RED, bold=True)
                                        typer.echo(response1 + response2)
                                else:
                                    if outputOption:
                                        r.write(str(url) + ', Not Reachable\n')
                                    response = typer.style('Not Reachable', fg=typer.colors.RED, bold=True)
                                    typer.echo(response)
                            else:
                                url1 = 'https://' + line[:-1]
                                url2 = 'http://' + line[:-1]
                                try:
                                    print(url1)
                                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
                                    data = requests.get(url1, headers=headers, timeout=timeout)
                                    code = data.status_code
                                    code_int = isinstance(code, int)
                                    if code_int:
                                        r.write(str(url1) + '\n')
                                        if code == 200:
                                            response = typer.style(f'Reachable [{code}]', fg=typer.colors.GREEN, bold=True)
                                            typer.echo(response)
                                        else:
                                            response1 = typer.style('Reachable', fg=typer.colors.GREEN, bold=True)
                                            response2 = typer.style(f' [{code}]', fg=typer.colors.RED, bold=True)
                                            typer.echo(response1 + response2)
                                    else:
                                        if outputOption:
                                            r.write(str(url1) + ', Not Reachable\n')
                                        response = typer.style('Not Reachable', fg=typer.colors.RED, bold=True)
                                        typer.echo(response)

                                except Exception:
                                    print(url2)
                                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
                                    data = requests.get(url2, headers=headers, timeout=timeout)
                                    code = data.status_code
                                    code_int = isinstance(code, int)
                                    if code_int:
                                        r.write(str(url2) + '\n')
                                        if code == 200:
                                            response = typer.style(f'Reachable [{code}]', fg=typer.colors.GREEN, bold=True)
                                            typer.echo(response)
                                        else:
                                            response1 = typer.style('Reachable', fg=typer.colors.GREEN, bold=True)
                                            response2 = typer.style(f' [{code}]', fg=typer.colors.RED, bold=True)
                                            typer.echo(response1 + response2)
                                    else:
                                        if outputOption:
                                            r.write(str(url2) + ', Not Reachable\n')
                                        response = typer.style('Not Reachable', fg=typer.colors.RED, bold=True)
                                        typer.echo(response)
                        except Exception:
                            if outputOption:
                                r.write(str(line[:-1]) + ', Not Reachable\n')
                                response = typer.style('ConnectionError! Not Reachable', fg=typer.colors.RED, bold=True)
                                typer.echo(response)
                end = time.time()
                print(f'\nScanning Completed within {end - start}s.')
            r.close()
        file.close()
    except Exception:
        response = typer.style('Invalid file or option', fg=typer.colors.RED, bold=True)
        typer.echo(response)


@app.command()
def manual():
    print("""Notes:
Enter one URL per line and ensure last line is EMPTY.
Input filename with extension (eg. 'Websites.txt').
Output file will be created with the filename given.
Default timeout is 5 seconds.

Commands Usage:
(file)
python status.py file <file to read> <file to output>
eg. python status.py file Hosts.txt Results.txt

if you want only reachable urls in output:
python status.py file <file to read> <file to output> -r/--reachableurl
eg. python status.py file Hosts.txt Results.txt --reachableurl
eg. python status.py file Hosts.txt Results.txt -r

(url)
python status.py url <url of website>
eg. python status.py url www.google.com
eg. python status.py url https://www.google.com
    """)


if __name__ == "__main__":
    title = typer.style("""
  _____ ____  ______    ___       _____ ______   ____  ______  __ __  _____
 / ___/|    ||      |  /  _]     / ___/|      | /    ||      ||  |  |/ ___/
(   \_  |  | |      | /  [_     (   \_ |      ||  o  ||      ||  |  (   \_ 
 \__  | |  | |_|  |_||    _]     \__  ||_|  |_||     ||_|  |_||  |  |\__  |
 /  \ | |  |   |  |  |   [_      /  \ |  |  |  |  _  |  |  |  |  :  |/  \ |
 \    | |  |   |  |  |     |     \    |  |  |  |  |  |  |  |  |     |\    |
  \___||____|  |__|  |_____|      \___|  |__|  |__|__|  |__|   \__,_| \___|
    """, fg=typer.colors.BRIGHT_BLUE, bold=True)
    typer.echo(title)
    description = typer.style('                         version 1.0\n                       ~Irfan Shah Jahan~', fg=typer.colors.BRIGHT_MAGENTA)
    typer.echo(description)
    app()
