import streamlit as st
from ciphers import (
    caesar_cipher,
    aes_encrypt,
    aes_decrypt,
    base64_encode,
    base64_decode,
    sha256_hash
)
from ui_components import load_css

st.set_page_config(page_title="CipherSphere", layout="wide")
load_css()

if 'plain_text' not in st.session_state:
    st.session_state.plain_text = ""
if 'cipher_text' not in st.session_state:
    st.session_state.cipher_text = ""

def handle_encryption():

    plain_text = st.session_state.plain_text_input
    if not plain_text:
        st.warning("Please enter some plain text to encrypt.")
        return

    try:
        result = ""
        if st.session_state.algorithm == "Caesar Cipher":
            result = caesar_cipher(plain_text, st.session_state.shift, mode='encrypt')
        elif st.session_state.algorithm == "AES":
            if len(st.session_state.get('key', '')) not in [16, 24, 32]:
                st.error("AES key must be 16, 24, or 32 characters long.")
                return
            iv_b64, ct_b64 = aes_encrypt(plain_text, st.session_state.key)
            st.info(f"AES IV (save for decryption): {iv_b64}")
            result = ct_b64
        elif st.session_state.algorithm == "Base64":
            result = base64_encode(plain_text)
        elif st.session_state.algorithm == "SHA-256 Hash":
            result = sha256_hash(plain_text)

        st.session_state.cipher_text_input = result
    except Exception as e:
        st.error(f"Encryption Error: {e}")


def handle_decryption():

    cipher_text = st.session_state.cipher_text_input
    if not cipher_text:
        st.warning("Please enter some cipher text to decrypt.")
        return
    if st.session_state.algorithm == "SHA-256 Hash":
        st.error("Hashing is a one-way function and cannot be decrypted.")
        return

    try:
        result = ""
        if st.session_state.algorithm == "Caesar Cipher":
            result = caesar_cipher(cipher_text, st.session_state.shift, mode='decrypt')
        elif st.session_state.algorithm == "AES":
            if len(st.session_state.get('key', '')) not in [16, 24, 32]:
                st.error("AES key must be 16, 24, or 32 characters long.")
                return
            if not st.session_state.get('iv'):
                st.error("Please provide the Initialization Vector (IV) for AES decryption.")
                return
            result = aes_decrypt(st.session_state.iv, cipher_text, st.session_state.key)
        elif st.session_state.algorithm == "Base64":
            result = base64_decode(cipher_text)

        st.session_state.plain_text_input = result
    except Exception as e:
        st.error(f"Decryption Error: {e}")


st.title("CryptoCraft: The Modern Encryption Tool")
st.markdown("A sleek, secure, and powerful tool for all your cryptographic needs.")

with st.sidebar:
    st.header("Algorithm & Settings")

    st.selectbox(
        "Select Algorithm",
        ["Caesar Cipher", "AES", "Base64", "SHA-256 Hash"],
        key='algorithm',
        label_visibility="collapsed"
    )

    if st.session_state.algorithm == "Caesar Cipher":
        st.subheader("Caesar Cipher Settings")
        st.slider("Shift Value", 1, 25, 3, key='shift')
    elif st.session_state.algorithm == "AES":
        st.subheader("AES Settings")
        st.text_input("Encryption Key (16, 24, or 32 chars)", type="password", key='key')
        st.text_input("Initialization Vector (IV)", help="Needed for decryption only.", key='iv')

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Plain Text")
    st.text_area("Enter text to encrypt", height=300, key="plain_text_input", label_visibility="collapsed")

with col2:
    st.subheader("Cipher Text")
    st.text_area("Enter text to decrypt", height=300, key="cipher_text_input", label_visibility="collapsed")

btn_col1, btn_col2 = st.columns(2, gap="large")

with btn_col1:
    st.button("Encrypt", use_container_width=True, type="primary", on_click=handle_encryption)

with btn_col2:
    st.button("Decrypt", use_container_width=True, on_click=handle_decryption)

