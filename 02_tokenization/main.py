"""Simple tokenization script"""
import tiktoken

def main():
    """Main function"""
    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens = encoding.encode("""
    Hello, my name is Shah Jabir Taqi. I'm a Backend, DevSecOps Developer and Cybersecurity Researcher.
    I know C, C++, Python, JavaScript, Golang and Rust and I have some basic DevOps and Security knowledge also.
    """)
    print(f"Tokens: {tokens}")

if __name__ == "__main__":
    main()
