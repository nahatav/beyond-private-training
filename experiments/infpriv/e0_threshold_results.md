# E0: threshold-and-subtract under per-client normalisation

U=200, m_u=10, |V|=2000, d=384, c=0.5, k=4; eps=1.0, delta=1e-05, T=10 gives sigma=11.7973

| mode | noise | histogram_threshold | mass after clip-and-subtract | surviving bins | `_select_data` |
|---|---|---|---|---|---|
| `sample` | eps=inf | None | 4000.00 | 1912/2000 | ok |
| `sample` | eps=inf | 0 | 4000.00 | 1912/2000 | ok |
| `sample` | eps=inf | 1 | 2189.00 | 1384/2000 | ok |
| `sample` | eps=inf | 2 | 976.00 | 733/2000 | ok |
| `sample` | eps=inf | 4 | 114.50 | 110/2000 | ok |
| `sample` | eps=inf | 10 | 0.00 | 0/2000 | ValueError: probabilities contain NaN |
| `sample` | sigma=1 | None | 3926.60 | 1791/2000 | ValueError: probabilities are not non-negative |
| `sample` | sigma=1 | 0 | 4054.80 | 1791/2000 | ok |
| `sample` | sigma=1 | 1 | 2410.79 | 1435/2000 | ok |
| `sample` | sigma=1 | 2 | 1225.46 | 929/2000 | ok |
| `sample` | sigma=1 | 4 | 194.40 | 213/2000 | ok |
| `sample` | sigma=1 | 10 | 0.00 | 0/2000 | ValueError: probabilities contain NaN |
| `sample` | eps=1.0,T=10 | None | 3134.12 | 1106/2000 | ValueError: probabilities are not non-negative |
| `sample` | eps=1.0,T=10 | 0 | 11031.60 | 1106/2000 | ok |
| `sample` | eps=1.0,T=10 | 1 | 9960.26 | 1035/2000 | ok |
| `sample` | eps=1.0,T=10 | 2 | 8947.25 | 985/2000 | ok |
| `sample` | eps=1.0,T=10 | 4 | 7102.37 | 844/2000 | ok |
| `sample` | eps=1.0,T=10 | 10 | 3195.51 | 475/2000 | ok |
| `client` | eps=inf | None | 1012.75 | 1912/2000 | ok |
| `client` | eps=inf | 0 | 1012.75 | 1912/2000 | ok |
| `client` | eps=inf | 1 | 29.69 | 169/2000 | ok |
| `client` | eps=inf | 2 | 0.33 | 2/2000 | ok |
| `client` | eps=inf | 4 | 0.00 | 0/2000 | ValueError: probabilities contain NaN |
| `client` | eps=inf | 10 | 0.00 | 0/2000 | ValueError: probabilities contain NaN |
| `client` | sigma=1 | None | 939.35 | 1336/2000 | ValueError: probabilities are not non-negative |
| `client` | sigma=1 | 0 | 1383.18 | 1336/2000 | ok |
| `client` | sigma=1 | 1 | 398.65 | 623/2000 | ok |
| `client` | sigma=1 | 2 | 60.58 | 128/2000 | ok |
| `client` | sigma=1 | 4 | 0.73 | 3/2000 | ok |
| `client` | sigma=1 | 10 | 0.00 | 0/2000 | ValueError: probabilities contain NaN |
| `client` | eps=1.0,T=10 | None | 146.87 | 1006/2000 | ValueError: probabilities are not non-negative |
| `client` | eps=1.0,T=10 | 0 | 9390.30 | 1006/2000 | ok |
| `client` | eps=1.0,T=10 | 1 | 8413.09 | 951/2000 | ok |
| `client` | eps=1.0,T=10 | 2 | 7498.49 | 879/2000 | ok |
| `client` | eps=1.0,T=10 | 4 | 5884.64 | 740/2000 | ok |
| `client` | eps=1.0,T=10 | 10 | 2526.09 | 391/2000 | ok |
