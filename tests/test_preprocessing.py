import unittest
import pandas as pd
from scripts.preprocessing import load_data, clean_data, normalize_data

class TestPreprocessing(unittest.TestCase):
    
    def setUp(self):
        # Create a simple dataset for testing
        data = {
            'A': [1, 2, 3, 4, np.nan],
            'B': [5, 6, 7, 8, 9],
            'C': [10, 11, 12, 13, 14]
        }
        self.df = pd.DataFrame(data)

    def test_load_data(self):
        # Test that the load_data function works correctly
        file_path = 'sample_data.csv'
        self.df.to_csv(file_path, index=False)  # Save test data to file
        loaded_df = load_data(file_path)
        self.assertEqual(loaded_df.shape, self.df.shape)
    
    def test_clean_data(self):
        # Test the clean_data function
        cleaned_df = clean_data(self.df)
        # After cleaning, there should be no NaN values
        self.assertFalse(cleaned_df.isnull().any().any())
    
    def test_normalize_data(self):
        # Test the normalize_data function
        normalized_df = normalize_data(self.df)
        # The mean of each column after normalization should be close to 0
        self.assertAlmostEqual(normalized_df['A'].mean(), 0, delta=0.1)
        self.assertAlmostEqual(normalized_df['B'].mean(), 0, delta=0.1)

if __name__ == "__main__":
    unittest.main()