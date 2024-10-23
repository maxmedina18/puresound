import argparse
import librosa
import numpy as np
import matplotlib.pyplot as plt

def load_audio(file_path):
    #function that loads audio file returns wave form and sample rate
    audio, sr = librosa.load(file_path, sr = 44100)
    return audio, sr

def process_audio(audio, sr):
    spectrogram = librosa.stft(audio, n_fft = 1024, hop_length=512)
    return np.abs(spectrogram)

def load_model():
    print("MODEL NOT YET MANUFACTURED")
    return None

def predict_stems(model, spectrogram):
    print("STEM PREDICTION SOON")
    return spectrogram

def spectrogram_to_audio(spectragram):
    return librosa.istft(spectragram, hop_length=512)

def save_output(output_path, audio, sr):
    librosa.output.write_wav(output_path, audio, sr)
    print(f"OUTPUT SAVED TO : {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Audio Separation using U-Net")
    parser.add_argument('--input', type=str, required=True, help="Path to input audio file")
    args = parser.parse_args()

    # Step 1: Load audio
    audio, sr = load_audio(args.input)

    # Step 2: Convert to spectrogram
    spectrogram = process_audio(audio, sr)

    # Step 3: Load the U-Net model
    model = load_model()

    # Step 4: Predict stems
    predicted_stems = predict_stems(model, spectrogram)

    # Step 5: Convert spectrogram back to audio
    separated_audio = spectrogram_to_audio(predicted_stems)

    # Step 6: Save the separated audio
    save_output("output.wav", separated_audio, sr)

if __name__ == "__main__":
    main()
