# Range-Scalp Bot

*Updated Fri Oct 16 02:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18583 | 16140 | 2443 (28) | 0 | $-5643.38 | -4.8% |
| **+10¢** | 14016 | 11190 | 2826 (40) | 0 | $-5099.30 | -5.8% |
| **+15¢** | 11753 | 8711 | 3042 (59) | 0 | $-4613.41 | -6.3% |
| **+20¢** | 10438 | 7255 | 3183 (78) | 0 | $-4030.10 | -6.2% |
| **+10¢ (15¢ stop)** | 22888 | 22838 | 50 (29) | 0 | $-8841.71 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 02:46 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-16 02:46 | +20 | SOL | DOWN | 0.67 | 0.89 | 1.99 |
| 10-16 02:46 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.36 |
| 10-16 02:46 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.73 |
| 10-16 02:46 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.21 |
| 10-16 02:46 | +10 stop | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 10-16 02:46 | +20 | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 10-16 02:46 | +15 | XRP | DOWN | 0.63 | 0.81 | 1.52 |
| 10-16 02:46 | +10 | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 10-16 02:46 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
| 10-16 02:46 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 10-16 02:46 | +20 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 10-16 02:46 | +15 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 10-16 02:46 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 10-16 02:46 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 10-16 02:46 | +10 stop | NEAR | DOWN | 0.63 | 0.78 | 1.22 |
| 10-16 02:46 | +20 | NEAR | DOWN | 0.63 | 0.85 | 1.96 |
| 10-16 02:46 | +15 | NEAR | DOWN | 0.63 | 0.78 | 1.22 |
| 10-16 02:46 | +10 | NEAR | DOWN | 0.63 | 0.78 | 1.23 |
| 10-16 02:46 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.20 |
| 10-16 02:46 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 02:46 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.88 |
| 10-16 02:46 | +15 | ETH | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 02:46 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-16 02:46 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-16 02:46 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-16 02:46 | +20 | DOGE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-16 02:46 | +15 | DOGE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-16 02:46 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-16 02:46 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-16 02:32 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 10-16 02:32 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 10-16 02:32 | +10 stop | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 10-16 02:32 | +20 | NEAR | DOWN | 0.58 | 0.81 | 2.01 |
| 10-16 02:32 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 10-16 02:32 | +10 | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 10-16 02:32 | +5 | NEAR | DOWN | 0.58 | 0.65 | 0.36 |
| 10-16 02:32 | +5 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-16 02:32 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-16 02:32 | +20 | BTC | UP | 0.71 | 0.95 | 2.19 |
