# Range-Scalp Bot

*Updated Fri Nov 13 02:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57682 | 50308 | 7374 (101) | 0 | $-15719.10 | -4.3% |
| **+10¢** | 43108 | 34496 | 8612 (133) | 0 | $-14663.38 | -5.4% |
| **+15¢** | 36145 | 26877 | 9268 (167) | 0 | $-13196.13 | -5.8% |
| **+20¢** | 32200 | 22474 | 9726 (217) | 0 | $-11568.20 | -5.7% |
| **+10¢ (15¢ stop)** | 70315 | 70187 | 128 (78) | 0 | $-25897.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 02:38 | +10 stop | HYPE | DOWN | 0.58 | 0.73 | 1.18 |
| 11-13 02:36 | +10 stop | NEAR | DOWN | 0.71 | 0.92 | 1.88 |
| 11-13 02:36 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.88 |
| 11-13 02:36 | +15 | NEAR | DOWN | 0.71 | 0.92 | 1.88 |
| 11-13 02:36 | +10 | NEAR | DOWN | 0.71 | 0.92 | 1.88 |
| 11-13 02:36 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-13 02:36 | +10 stop | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 02:36 | +10 | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 02:36 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 11-13 02:36 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 02:36 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-13 02:36 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-13 02:36 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-13 02:36 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-13 02:36 | +20 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-13 02:36 | +15 | ZEC | DOWN | 0.60 | 0.78 | 1.50 |
| 11-13 02:36 | +10 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-13 02:36 | +5 | ZEC | DOWN | 0.58 | 0.64 | 0.25 |
| 11-13 02:35 | +5 | HYPE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-13 02:34 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 11-13 02:34 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 02:34 | +20 | ETH | DOWN | 0.70 | 0.92 | 1.94 |
| 11-13 02:34 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-13 02:34 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 02:34 | +5 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-13 02:33 | +10 stop | HYPE | DOWN | 0.64 | 0.49 | -1.85 |
| 11-13 02:33 | +20 | HYPE | DOWN | 0.64 | 0.96 | 3.04 |
| 11-13 02:33 | +15 | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-13 02:33 | +10 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-13 02:33 | +5 | HYPE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-13 02:31 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 11-13 02:31 | +20 | XRP | DOWN | 0.69 | 0.91 | 2.02 |
| 11-13 02:31 | +15 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 11-13 02:31 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-13 02:31 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-13 02:31 | +5 | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 02:30 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-13 02:30 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 11-13 02:30 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 11-13 02:30 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
