# Range-Scalp Bot

*Updated Fri Nov 20 15:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66327 | 57881 | 8446 (128) | 1 | $-17869.40 | -4.3% |
| **+10¢** | 49526 | 39651 | 9875 (170) | 1 | $-16642.04 | -5.3% |
| **+15¢** | 41533 | 30884 | 10649 (217) | 1 | $-14979.06 | -5.7% |
| **+20¢** | 36981 | 25797 | 11184 (273) | 1 | $-13273.42 | -5.7% |
| **+10¢ (15¢ stop)** | 80780 | 80614 | 166 (100) | 0 | $-29830.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 15:36 | +5 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 11-20 15:36 | +10 stop | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 11-20 15:36 | +10 stop | DOGE | DOWN | 0.43 | 0.58 | 1.14 |
| 11-20 15:36 | +5 | DOGE | DOWN | 0.44 | 0.58 | 1.04 |
| 11-20 15:35 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-20 15:35 | +10 stop | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
| 11-20 15:35 | +5 | DOGE | DOWN | 0.55 | 0.63 | 0.45 |
| 11-20 15:34 | +10 stop | XRP | DOWN | 0.70 | 0.48 | -2.53 |
| 11-20 15:34 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 11-20 15:34 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-20 15:31 | +5 | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-20 15:31 | +10 stop | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-20 15:31 | +20 | SOL | DOWN | 0.66 | 0.88 | 1.96 |
| 11-20 15:31 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-20 15:31 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-20 15:31 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 11-20 15:31 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.85 |
| 11-20 15:31 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.23 |
| 11-20 15:31 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 15:31 | +20 | BNB | DOWN | 0.69 | 0.93 | 2.20 |
| 11-20 15:31 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-20 15:31 | +10 | BNB | DOWN | 0.71 | 0.85 | 1.17 |
| 11-20 15:31 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.43 |
| 11-20 15:31 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-20 15:31 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.80 |
| 11-20 15:31 | +15 | HYPE | DOWN | 0.71 | 0.91 | 1.80 |
| 11-20 15:31 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-20 15:31 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-20 15:31 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.85 |
| 11-20 15:31 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-20 15:31 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-20 15:31 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.63 |
| 11-20 15:31 | +10 stop | ETH | DOWN | 0.69 | 0.54 | -1.83 |
| 11-20 15:31 | +20 | ETH | DOWN | 0.69 | 0.90 | 1.92 |
| 11-20 15:31 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 11-20 15:31 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.78 |
| 11-20 15:31 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-20 15:31 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-20 15:31 | +20 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 11-20 15:31 | +15 | XRP | DOWN | 0.63 | 0.79 | 1.31 |
