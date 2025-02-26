This tool analyzes the randomness in audio signals using the Hilbert transform. It processes audio samples to generate binary sequences based on signal variations and combines them using XOR operations to check if the generated sequences passes NIST randomness tests.

## Signal Processing
1. Takes an audio file as input
2. Applies Hilbert transform to create an analytical signal
3. Extracts three components:
   - Real part of the analytical signal
   - Imaginary part of the analytical signal
   - Instantaneous phase angle

## Binary Sequence Generation
For each component:
- Analyzes consecutive data points
- Writes '1' if the signal value increases
- Writes '0' if the signal value decreases
Lastly, takes the three binary sequences and performs XOR on corresponding chracters.

## My Results
- Performing this on a single audio file didn't produce good results. The final sequence failed at almost all NIST randomness tests. Sample1 and Sample2 demonstrate the result.
- Combining multiple audio files produced good results. I performed XOR operation on final binary sequences for each audio file, and tested with NIST test suite. The sequence has passed almost all tests.
